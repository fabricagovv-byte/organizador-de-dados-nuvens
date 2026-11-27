import json, subprocess, time, sys, urllib.parse, re, unicodedata
D = sys.argv[1]
def norm(s): return unicodedata.normalize('NFKD', (s or '').lower()).encode('ascii','ignore').decode()
def get(url):
    for k in range(8):
        r = subprocess.run(['curl','-sS','-m','60','-A','Mozilla/5.0',url], capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            try: return json.loads(r.stdout)
            except Exception: pass
        time.sleep(3 + k*3)
    return None
cons = {c['cnpj'] for c in json.load(open(f'{D}/consorcios_contatos.json'))}
QS = ['digitalização', 'gestão documental', 'gestão eletrônica de documentos', 'GED documentos', 'arquivo documentos organização']
achados = {}
for q in QS:
    for tipo in ('edital', 'ata'):
        for p in range(1, 31):
            d = get(f'https://pncp.gov.br/api/search/?q={urllib.parse.quote(q)}&tipos_documento={tipo}&ufs=MG&ordenacao=-data&pagina={p}&tam_pagina=50')
            if not d: print('falhou', q, tipo, p, flush=True); break
            its = d.get('items', [])
            for i in its:
                if i.get('orgao_cnpj') in cons:
                    t = norm(i.get('description'))
                    if re.search(r'digitaliz|gestao documental|gestao eletronica de document|\bged\b|arquivolog|tratamento documental|gerenciamento eletronico de document', t):
                        achados[i['item_url'] + tipo] = dict(cnpj=i['orgao_cnpj'], orgao=i['orgao_nome'], tipo=tipo, titulo=i.get('title'), data=(i.get('data_publicacao_pncp') or '')[:10],
                            objeto=(i.get('description') or '').strip(), situacao=i.get('situacao_nome'), modalidade=i.get('modalidade_licitacao_nome'), url='https://pncp.gov.br/app/' + ('editais' if tipo == 'edital' else 'atas') + i['item_url'].replace('/compras', ''))
            print(q, tipo, p, d.get('total'), len(its), len(achados), flush=True)
            json.dump(list(achados.values()), open(f'{D}/cons_compras.json','w'), ensure_ascii=False, indent=1)
            if len(its) < 50: break
            time.sleep(.8)
print('fim', len(achados), flush=True)
