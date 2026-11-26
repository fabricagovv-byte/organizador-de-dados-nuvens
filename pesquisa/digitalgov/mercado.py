import json, subprocess, sys, time, urllib.parse
D, out, maxp = sys.argv[1], sys.argv[3], int(sys.argv[4])
q = 'digitaliza\u00e7\u00e3o documentos'
def get(url):
    for k in range(8):
        r = subprocess.run(['curl','-sS','-m','60','-A','Mozilla/5.0',url], capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            try: return json.loads(r.stdout)
            except Exception: pass
        time.sleep(3 + k*2)
    return None
items = []; total = None
for p in range(1, maxp+1):
    d = get(f'https://pncp.gov.br/api/search/?q={urllib.parse.quote(q)}&tipos_documento=edital&ordenacao=-data&pagina={p}&tam_pagina=50')
    if d is None: print('pagina falhou', p, flush=True); continue
    total = d.get('total'); its = d.get('items', [])
    if not its: break
    if (its[-1].get('data_publicacao_pncp') or '9999') < '2024-01-01':
        items += [{k: i.get(k) for k in ['ano','uf','esfera_nome','poder_nome','orgao_nome','orgao_cnpj','unidade_nome','municipio_nome','modalidade_licitacao_nome','data_publicacao_pncp','valor_global','valor_total_estimado','valor_total_homologado','situacao_nome','description','item_url','srp']} for i in its]
        print('chegou em 2023', p, flush=True); break
    keep = ['ano','uf','esfera_nome','poder_nome','orgao_nome','orgao_cnpj','unidade_nome','municipio_nome','modalidade_licitacao_nome','data_publicacao_pncp','valor_global','valor_total_estimado','valor_total_homologado','situacao_nome','description','item_url','srp']
    items += [{k: i.get(k) for k in keep} for i in its]
    if p % 10 == 0:
        print(p, len(items), flush=True)
        json.dump({'total': total, 'items': items}, open(f'{D}/{out}', 'w'), ensure_ascii=False)
    time.sleep(.5)
json.dump({'total': total, 'items': items}, open(f'{D}/{out}', 'w'), ensure_ascii=False)
print('fim', total, len(items), flush=True)
