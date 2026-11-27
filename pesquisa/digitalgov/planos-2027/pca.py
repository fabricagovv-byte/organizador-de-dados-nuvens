import json, subprocess, sys, time, re, unicodedata
D = sys.argv[1]; ANO = sys.argv[2]
def norm(s): return unicodedata.normalize('NFKD', (s or '').lower()).encode('ascii','ignore').decode()
def get(url):
    for k in range(5):
        r = subprocess.run(['curl','-sS','-m','90','-A','Mozilla/5.0','-w','\n%{http_code}',url], capture_output=True, text=True)
        body, _, code = r.stdout.rpartition('\n')
        if code == '404': return 404
        if code == '200' and body.strip():
            try: return json.loads(body)
            except Exception: pass
        time.sleep(6 + k*6)
    return None
src = json.load(open(f'{D}/../dgov-dl/mercado.json'))['items']
orgs = {}
for i in src:
    if i.get('orgao_cnpj') and re.search(r'digitaliz|gestao eletronica de documentos|\bged\b', norm(i.get('description'))): orgs[i['orgao_cnpj']] = (i.get('orgao_nome'), i.get('uf'), i.get('esfera_nome'))
RX = r'digitaliz|gestao eletronica de documento|\bged\b|arquivo|acervo|indexa|microfilm'
out = {'ano': ANO, 'orgaos': [], 'itens': []}
for n, (cnpj, (nome, uf, esf)) in enumerate(orgs.items()):
    c = get(f'https://pncp.gov.br/api/pncp/v1/orgaos/{cnpj}/pca/{ANO}/consolidado')
    time.sleep(1.5)
    if c in (404, None):
        out['orgaos'].append(dict(cnpj=cnpj, nome=nome, uf=uf, esfera=esf, tem_pca=(c != 404 and c is not None) or False, status='sem PCA' if c == 404 else 'falha'))
    else:
        out['orgaos'].append(dict(cnpj=cnpj, nome=nome, uf=uf, esfera=esf, tem_pca=True, itens=c.get('quantidade'), valor=c.get('valorTotal')))
        for seq in range(1, 6):
            achou = False
            for pag in range(1, 11):
                its = get(f'https://pncp.gov.br/api/pncp/v1/orgaos/{cnpj}/pca/{ANO}/{seq}/itens?pagina={pag}&tamanhoPagina=200')
                time.sleep(1.5)
                if its in (404, None) or not its: break
                achou = True
                for it in its:
                    t = norm(' '.join(str(it.get(k) or '') for k in ('descricao','grupoContratacaoNome','classificacaoSuperiorNome','pdmDescricao')))
                    if re.search(RX, t) and not re.search(r'impress|copiadora|multifuncional', t):
                        out['itens'].append(dict(cnpj=cnpj, orgao=nome, uf=uf, desc=it.get('descricao'), grupo=it.get('grupoContratacaoNome'), classe=it.get('classificacaoSuperiorNome'),
                            classe_cod=it.get('classificacaoSuperiorCodigo'), qtd=it.get('quantidade'), un=it.get('unidadeFornecimento'), valor=it.get('valorTotal'), data=it.get('dataDesejada'), unidade=it.get('nomeUnidade')))
                if len(its) < 200: break
            if not achou: break
    if n % 10 == 0:
        print(n, len(orgs), sum(1 for o in out['orgaos'] if o['tem_pca']), len(out['itens']), flush=True)
        json.dump(out, open(f'{D}/pca{ANO}.json', 'w'), ensure_ascii=False)
json.dump(out, open(f'{D}/pca{ANO}.json', 'w'), ensure_ascii=False)
print('fim', len(orgs), sum(1 for o in out['orgaos'] if o['tem_pca']), len(out['itens']), flush=True)
