import json, subprocess, time, sys, os
D = sys.argv[1]
cons = json.load(open(f'{D}/consorcios_mg.json'))
out_f = f'{D}/consorcios_contatos.json'
done = {c['cnpj']: c for c in json.load(open(out_f))} if os.path.exists(out_f) else {}
for n, c in enumerate(cons):
    if c['cnpj'] in done: continue
    r = None
    for k in range(4):
        p = subprocess.run(['curl','-sS','-m','40','-A','DigitalGovReport/1.0','https://brasilapi.com.br/api/cnpj/v1/' + c['cnpj']], capture_output=True, text=True)
        try: r = json.loads(p.stdout); break
        except Exception: time.sleep(4 + k*4)
    if r and r.get('cnpj'):
        c.update(fantasia=r.get('nome_fantasia'), municipio=r.get('municipio'), tel1=r.get('ddd_telefone_1'), tel2=r.get('ddd_telefone_2'), email=r.get('email'),
                 endereco=f"{r.get('logradouro') or ''}, {r.get('numero') or ''} - {r.get('bairro') or ''}", cep=r.get('cep'), situacao=r.get('descricao_situacao_cadastral'), uf_rf=r.get('uf'))
    done[c['cnpj']] = c
    if n % 10 == 0:
        json.dump(list(done.values()), open(out_f,'w'), ensure_ascii=False, indent=1); print(n, len(done), flush=True)
    time.sleep(1.2)
json.dump(list(done.values()), open(out_f,'w'), ensure_ascii=False, indent=1)
print('fim', len(done), sum(1 for c in done.values() if c.get('tel1')), flush=True)
