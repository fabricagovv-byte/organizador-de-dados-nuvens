import json, subprocess, time, sys, re
D = sys.argv[1]
def get(url):
    for k in range(8):
        r = subprocess.run(['curl','-sS','-m','60','-A','Mozilla/5.0',url], capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            try: return json.loads(r.stdout)
            except Exception: pass
        time.sleep(3 + k*3)
    return None
orgs = {}
for q in ['consorcio intermunicipal', 'consorcio']:
    for p in range(1, 21):
        d = get(f'https://pncp.gov.br/api/search/?q={q.replace(" ","%20")}&tipos_documento=edital&ufs=MG&ordenacao=-data&pagina={p}&tam_pagina=50')
        if not d: print('falhou', q, p, flush=True); continue
        its = d.get('items', [])
        for i in its:
            if i.get('uf') == 'MG' and re.search(r'CONSORCIO|CONSÓRCIO|ASSOCIACAO PUBLICA|CIS[A-Z]', (i.get('orgao_nome') or '').upper()):
                o = orgs.setdefault(i['orgao_cnpj'], dict(cnpj=i['orgao_cnpj'], nome=i['orgao_nome'], cidade=i.get('municipio_nome'), ibge=i.get('codigo_ibge'), editais=0, ultimo=''))
                o['editais'] += 1; o['ultimo'] = max(o['ultimo'], (i.get('data_publicacao_pncp') or '')[:10])
        print(q, p, d.get('total'), len(its), len(orgs), flush=True)
        json.dump(list(orgs.values()), open(f'{D}/consorcios_mg.json','w'), ensure_ascii=False, indent=1)
        if len(its) < 50: break
        time.sleep(.8)
json.dump(list(orgs.values()), open(f'{D}/consorcios_mg.json','w'), ensure_ascii=False, indent=1)
print('fim', len(orgs))
