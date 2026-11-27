import json, subprocess, time, sys, re, unicodedata, os
D = sys.argv[1]
def norm(s): return unicodedata.normalize('NFKD', (s or '').lower()).encode('ascii','ignore').decode()
def get(url):
    for k in range(5):
        r = subprocess.run(['curl','-sS','-m','90','-A','Mozilla/5.0','-w','\n%{http_code}',url], capture_output=True, text=True)
        body, _, code = r.stdout.rpartition('\n')
        if code in ('404','400'): return 404
        if code == '200' and body.strip():
            try: return json.loads(body)
            except Exception: pass
        time.sleep(5 + k*5)
    return None
cons = json.load(open(f'{D}/consorcios_contatos.json'))
out_f = f'{D}/cons_pca.json'
out = json.load(open(out_f)) if os.path.exists(out_f) else {'feitos': [], 'pcas': [], 'itens': []}
RX = r'digitaliz|indexa|gestao documental|gestao eletronica de document|\bged\b|arquivolog|tratamento documental|guarda de document|documento - guarda|microfilm'
for n, c in enumerate(cons):
    for ano in ('2026', '2027'):
        key = c['cnpj'] + ano
        if key in out['feitos']: continue
        cc = get(f"https://pncp.gov.br/api/pncp/v1/orgaos/{c['cnpj']}/pca/{ano}/consolidado"); time.sleep(1.2)
        if isinstance(cc, dict):
            out['pcas'].append(dict(cnpj=c['cnpj'], ano=ano, itens=cc.get('quantidade'), valor=cc.get('valorTotal')))
            for seq in range(1, 4):
                got = False
                for pag in range(1, 6):
                    its = get(f"https://pncp.gov.br/api/pncp/v1/orgaos/{c['cnpj']}/pca/{ano}/{seq}/itens?pagina={pag}&tamanhoPagina=200"); time.sleep(1.2)
                    if not isinstance(its, list) or not its: break
                    got = True
                    for it in its:
                        t = norm(' '.join(str(it.get(k) or '') for k in ('descricao','grupoContratacaoNome','classificacaoSuperiorNome')))
                        if re.search(RX, t) and not re.search(r'impress|copiadora|multifuncional', t):
                            out['itens'].append(dict(cnpj=c['cnpj'], ano=ano, desc=it.get('descricao') or it.get('grupoContratacaoNome'), classe=it.get('classificacaoSuperiorNome'), qtd=it.get('quantidade'), un=it.get('unidadeFornecimento'), valor=it.get('valorTotal'), data=it.get('dataDesejada')))
                    if len(its) < 200: break
                if not got: break
        out['feitos'].append(key)
    if n % 5 == 0:
        json.dump(out, open(out_f,'w'), ensure_ascii=False); print(n, len(cons), len(out['pcas']), len(out['itens']), flush=True)
json.dump(out, open(out_f,'w'), ensure_ascii=False)
print('fim', len(out['pcas']), len(out['itens']), flush=True)
