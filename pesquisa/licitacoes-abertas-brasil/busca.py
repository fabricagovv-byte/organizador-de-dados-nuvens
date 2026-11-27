import json, subprocess, sys, time, urllib.parse
D = sys.argv[1]
QS = ['digitalização de documentos', 'digitalização acervo', 'gestão eletrônica de documentos', 'gestão documental', 'unidade de serviço técnico', 'UST', 'pontos de função', 'ponto de função', 'fábrica de software', 'sprint desenvolvimento', 'sustentação de software', 'manutenção de software', 'sustentação de sistemas', 'desenvolvimento de sistemas']
def get(url):
    for k in range(4):
        r = subprocess.run(['curl','-sS','-m','30','-A','Mozilla/5.0',url], capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            try: return json.loads(r.stdout)
            except Exception: pass
        time.sleep(3 + k*3)
allit = {}
for q in QS:
    for p in range(1, 5):
        d = get(f'https://pncp.gov.br/api/search/?q={urllib.parse.quote(q)}&tipos_documento=edital&ordenacao=-data&status=recebendo_proposta&pagina={p}&tam_pagina=50')
        if not d: print('falhou', q, p, flush=True); continue
        its = d.get('items', [])
        for i in its: i['_q'] = q; allit.setdefault(i['item_url'], i)
        json.dump(list(allit.values()), open(f'{D}/busca.json','w'), ensure_ascii=False)
        print(q, p, d.get('total'), len(its), len(allit), flush=True)
        if len(its) < 50: break
        time.sleep(1)
json.dump(list(allit.values()), open(f'{D}/busca.json','w'), ensure_ascii=False)
print('fim', len(allit), flush=True)
