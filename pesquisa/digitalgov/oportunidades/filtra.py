import json, re, unicodedata, sys, collections
D = sys.argv[1]
def norm(s): return unicodedata.normalize('NFKD', (s or '').lower()).encode('ascii','ignore').decode()
its = json.load(open(f'{D}/abertas.json'))
OUT = []
for i in its:
    d = norm(i.get('description')) + ' ' + norm(i.get('title'))
    fim = (i.get('data_fim_recebimento_propostas') or '')[:10]
    if i.get('cancelado') or 'suspens' in norm(i.get('situacao_nome')): continue
    dig = re.search(r'digitaliz|gestao eletronica de document|\bged\b|gestao documental|gerenciamento eletronico de document|indexacao de document|arquivo (publico|morto|fisico)|tratamento arquivistic|arquivolog', d)
    sw = re.search(r'software|sistema (integrado )?de gestao|sistemas? de informac|plataforma (digital|web|tecnologic)|aplicativo|sistema informatizado|solucao tecnologica|fabrica de software|desenvolvimento de sistema', d) and \
         re.search(r'desenvolv|licen|locacao|cessao|implant|fornecimento|contratacao|prestacao|manutenc|sustentac', d)
    ruim = re.search(r'impressora|impressao|copiadora|multifuncional|outsourcing de impress|reprografi|fotovoltaic|climatiz|abastecimento de agua|videomonitor|cftv|combustivel|veiculo|gas medicinal|alimenta|merenda|medicamento|obra|pavimenta|engenharia civil|placa solar|ar condicionado|telefonia', d)
    if ruim and not dig: continue
    if not (dig or sw): continue
    cat = 'Digitalização de documentos' if dig else 'Desenvolvimento e licença de software'
    _, _, cnpj, ano, seq = i['item_url'].split('/')
    OUT.append(dict(cat=cat, orgao=i.get('orgao_nome'), unidade=i.get('unidade_nome'), cidade=i.get('municipio_nome'), uf=i.get('uf'), ibge=i.get('codigo_ibge'),
        esfera=i.get('esfera_nome'), modalidade=i.get('modalidade_licitacao_nome'), fim=i.get('data_fim_recebimento_propostas'), inicio=i.get('data_inicio_recebimento_propostas'),
        valor=i.get('valor_total_estimado'), objeto=(i.get('description') or '').strip(), srp=i.get('srp'), cnpj=cnpj, ano=ano, seq=seq,
        link=f'https://pncp.gov.br/app/editais/{cnpj}/{ano}/{seq}', origem=i.get('link_sistema_origem')))

json.dump(OUT, open(f'{D}/oportunidades.json','w'), ensure_ascii=False, indent=1)
print(len(OUT), collections.Counter(o['cat'] for o in OUT), collections.Counter(o['uf'] for o in OUT).most_common(8))
for o in OUT: print(o['cat'][:5], '|', o['cidade'], o['uf'], '|', (o['valor'] or 0), '|', o['objeto'][:110].replace('\n',' '))
