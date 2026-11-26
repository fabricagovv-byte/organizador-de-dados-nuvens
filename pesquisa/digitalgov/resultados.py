import json, subprocess, sys, time
D = sys.argv[1]
def get(url):
    for k in range(3):
        r = subprocess.run(['curl','-sS','-m','60','-A','Mozilla/5.0',url], capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            try: return json.loads(r.stdout)
            except Exception: return None
        time.sleep(2)
    return None
d = json.load(open(f'{D}/dg.json'))
out = []
for it in d['items']:
    _, _, cnpj, ano, seq = it['item_url'].split('/')
    base = f'https://pncp.gov.br/api/pncp/v1/orgaos/{cnpj}/compras/{ano}/{seq}'
    itens = get(base + '/itens?pagina=1&tamanhoPagina=200') or []
    proc = dict(orgao=it['orgao_nome'], uf=it['uf'], ano=ano, mod=it['modalidade_licitacao_nome'], data=it['data_publicacao_pncp'][:10], sit=it['situacao_nome'], obj=(it.get('description') or '')[:220], url='https://pncp.gov.br/app/editais/'+cnpj+'/'+ano+'/'+seq, itens=[])
    for i in itens:
        res = []
        if i.get('temResultado'):
            res = get(f"{base}/itens/{i['numeroItem']}/resultados") or []
        proc['itens'].append(dict(n=i['numeroItem'], desc=(i.get('descricao') or '')[:120], qtd=i.get('quantidade'), est=i.get('valorTotal'),
            res=[dict(forn=r.get('nomeRazaoSocialFornecedor'), ni=r.get('niFornecedor'), val=r.get('valorTotalHomologado'), unit=r.get('valorUnitarioHomologado'), data=(r.get('dataResultado') or '')[:10]) for r in res]))
        time.sleep(.3)
    out.append(proc)
    print(proc['orgao'], len(proc['itens']), 'itens', file=sys.stderr)
json.dump(out, open(f'{D}/resultados.json','w'), ensure_ascii=False, indent=1)
