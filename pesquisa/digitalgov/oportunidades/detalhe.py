import json, subprocess, sys, time, os
D = sys.argv[1]
def get(url):
    for k in range(6):
        r = subprocess.run(['curl','-sS','-m','45','-A','Mozilla/5.0','-w','\n%{http_code}',url], capture_output=True, text=True)
        body, _, code = r.stdout.rpartition('\n')
        if code in ('404','400'): return None
        if code == '200' and body.strip():
            try: return json.loads(body)
            except Exception: pass
        time.sleep(3 + k*3)
    return None
ops = json.load(open(f'{D}/oportunidades.json'))
cache_f = f'{D}/detalhes.json'
cache = json.load(open(cache_f)) if os.path.exists(cache_f) else {}
t0 = time.time()
for n, o in enumerate(ops):
    k = o['link']
    if k in cache: continue
    if time.time() - t0 > 520: break
    base = f"{o['cnpj']}/compras/{o['ano']}/{o['seq']}"
    det = get(f'https://pncp.gov.br/api/consulta/v1/orgaos/{base}')
    its = get(f'https://pncp.gov.br/api/pncp/v1/orgaos/{base}/itens?pagina=1&tamanhoPagina=30') or []
    cache[k] = dict(det=det, itens=[dict(n=i.get('numeroItem'), desc=i.get('descricao'), qtd=i.get('quantidade'), un=i.get('unidadeMedida'), vt=i.get('valorTotal'), vu=i.get('valorUnitarioEstimado'), me=i.get('materialOuServicoNome')) for i in its])
    if n % 10 == 0:
        json.dump(cache, open(cache_f,'w'), ensure_ascii=False); print(n, len(cache), flush=True)
    time.sleep(.6)
json.dump(cache, open(cache_f,'w'), ensure_ascii=False)
print('feito', len(cache), 'de', len(ops), flush=True)
