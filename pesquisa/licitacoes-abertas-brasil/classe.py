import json, re, unicodedata, sys
D = sys.argv[1]
def norm(s): return unicodedata.normalize('NFKD', (s or '').lower()).encode('ascii','ignore').decode()
CATS = [
 ('dig',  r'digitaliza\w*\s+(\w+\s+){0,4}(document|acervo|processo|arquiv|prontuari|livro|imagem de document)|gestao eletronica de document|gerenciamento eletronico de document|gestao documental|\bged\b|indexacao de document|microfilm|tratamento (tecnico )?arquivist|organizacao (\w+ ){0,3}(arquivo|acervo|document)'),
 ('ust',  r'\bust\b|\busts\b|unidades? de servicos? tecnicos?'),
 ('pf',   r'pontos? de funcao|\bpfs?\b.{0,40}(software|sistema)|function point'),
 ('sprint', r'\bsprints?\b|fabrica de software|desenvolvimento,? (\w+,? ){0,4}(de |do |dos |da )?(software|sistemas?|aplicativ|aplicac|portal|plataforma|solucoes? (tecnologic|digit|de ti))|metodologia agil'),
 ('sust', r'sustentac\w*|manutenc\w*(,? \w+){0,6},? (de |do |dos |da |das )?(software|sistemas?|solucao|plataforma|aplicac|portal)|(software|sistemas? (informatizad|integrad|de gestao)|solucao integrada)(.{0,200})manutenc|sustentacao (\w+ ){0,3}(software|sistemas?|aplicac|solucoes|ambiente)|manutencao (corretiva|evolutiva|adaptativa|perfectiva)(,? \w+){0,4} (de |do |dos |das )?(software|sistemas?|aplicac|solucoes)|manutencao (de|do|dos) (software|sistemas? (de informac|informatizad|web|legad|corporativ))'),
]
FORA = r'aquisicao de (scanner|computador|equipamento|notebook|impressora|mobiliari)|outsourcing de impress|locacao de (impressora|multifuncion)|ar condicionado|climatiza|elevador|fotovoltaic|abastecimento de agua|esgot|veicul|pavimenta|obra|engenharia civil|medicament|alimenta|combustiv|raio[- ]?x|radiolog|tomograf|eletrocardio|pacs\b|laudo|livros? didatic|material didatic|cft?v|videomonitor|camera'
DURO = r'residuos|veicul|automotiv|jornais|microgeracao|energia eletrica|medidores|firewall|xdr|ciberneti|rastreamento|scanner de diagnostico|microsoft|adobe|autodesk|red hat|jetbrains|redis|solarwinds|liferay|oracle|vmware|telessaude|cftv|videomonitor|catraca|controle fisico de acesso|telefonia|rede sem fio|pecas e acessorios|maquinas rotativas|etiquetas de seguranca|backup|aquisicao de softwares e licencas|licencas de uso de software de engenharia|impressao|impressoras|copias|reprograf|outsourcing|materia(l|is) de expediente|captacao de recursos|inventario fisico|avaliacao patrimonial|licencas? (oficiais |de uso )?(de |dos )?softwares|subscricao|locacao de equipamentos'
a = json.load(open(f'{D}/busca.json'))
out = []
for i in a:
    t = norm((i.get('title') or '') + ' ' + (i.get('description') or ''))
    cats = [k for k, rx in CATS if re.search(rx, t)]
    if not cats: continue
    if re.search(DURO, t): continue
    if re.search(FORA, t) and not re.search(r'digitaliza\w* de document|software|sistema de gestao|ust\b|pontos? de funcao', t): continue
    fim = (i.get('data_fim_vigencia') or '')[:16]
    if fim and fim[:10] < '2026-11-27': continue
    out.append(dict(cats=cats, cat=cats[0], orgao=i['orgao_nome'], unidade=i.get('unidade_nome'), cidade=i.get('municipio_nome'), uf=i.get('uf'), ibge=i.get('codigo_ibge'),
        esfera=i.get('esfera_nome'), modalidade=i.get('modalidade_licitacao_nome'), fim=fim, valor=i.get('valor_global') or 0, objeto=(i.get('description') or '').strip(),
        cnpj=i['orgao_cnpj'], ano=i['ano'], seq=i['numero_sequencial'], link='https://pncp.gov.br/app/editais/' + i['item_url'].replace('/compras/','').strip('/'), q=i.get('_q'), sit=i.get('situacao_nome')))
json.dump(out, open(f'{D}/cand.json','w'), ensure_ascii=False)
from collections import Counter
print(len(a), 'candidatos', len(out), Counter(o['cat'] for o in out))
