# Análise do mercado de digitalização de documentos no PNCP (editais 2024-2026).
import json, re, unicodedata, sys, collections, datetime
D = sys.argv[1] if len(sys.argv) > 1 else '../dgov-dl'
raw = json.load(open(f'{D}/mercado.json'))['items']
def norm(s): return unicodedata.normalize('NFKD', (s or '').lower()).encode('ascii','ignore').decode()
seen = set(); IT = []
for i in raw:
    k = i.get('item_url')
    if k in seen: continue
    seen.add(k)
    d = norm(i.get('description'))
    if not re.search(r'digitaliz|gestao eletronica de documentos|\bged\b', d): continue
    dt = (i.get('data_publicacao_pncp') or '')[:10]
    if not dt or dt < '2024-01-01': continue
    i['_d'] = d; i['_dt'] = dt; i['_ano'] = dt[:4]; i['_mes'] = dt[5:7]
    IT.append(i)

def tipo_orgao(i):
    n = norm(i.get('orgao_nome')) + ' ' + norm(i.get('unidade_nome'))
    if 'camara' in n: return 'Câmaras municipais'
    if 'consorcio' in n: return 'Consórcios'
    if re.search(r'tribunal|justica|ministerio publico|defensoria', n): return 'Justiça, MP e tribunais'
    if re.search(r'universidade|instituto federal|escola|educacao', n): return 'Educação'
    if re.search(r'saude|hospital|fundo municipal de saude', n): return 'Saúde'
    if re.search(r'saae|servico autonomo|agua e esgoto|saneamento', n): return 'Saneamento (SAAE)'
    if re.search(r'previdencia|instituto de previd|ipsm|iprev|rpps', n): return 'Previdência'
    if re.search(r'municipio|prefeitura', n): return 'Prefeituras'
    if re.search(r'estado|secretaria de estado|governo do', n): return 'Governos estaduais'
    return 'Outros órgãos'

TEMAS = [('Software de gestão de documentos (GED)', r'software|sistema|licenc|plataforma|gestao eletronica|\bged\b'),
         ('Organização de arquivo físico', r'organiza|arquivolog|higieniza|acervo|arquivo'),
         ('Indexação e OCR', r'indexa|ocr|reconhecimento'),
         ('LGPD', r'lgpd|protecao de dados'),
         ('Validade legal e certificação digital', r'validade|certifica|assinatura|icp|10\.278'),
         ('Guarda e custódia de documentos', r'guarda|custodia|armazenamento'),
         ('Microfilmagem', r'microfilm')]

def agg():
    A = {}
    anos = collections.Counter(i['_ano'] for i in IT); A['anos'] = dict(anos)
    meses = collections.defaultdict(collections.Counter)
    for i in IT: meses[i['_ano']][i['_mes']] += 1
    A['meses'] = {a: dict(c) for a, c in meses.items()}
    hoje = max(i['_dt'] for i in IT); A['ultima'] = hoje
    lim = hoje[5:]  # mesmo período do ano
    A['ytd'] = {a: sum(1 for i in IT if i['_ano'] == a and i['_dt'][5:] <= lim) for a in ('2024','2025','2026')}
    def by(fn, ano='2026'):
        return collections.Counter(fn(i) for i in IT if i['_ano'] == ano)
    A['esfera'] = {a: dict(by(lambda i: i.get('esfera_nome') or 'n/d', a)) for a in ('2025','2026')}
    A['tipo'] = {a: dict(by(tipo_orgao, a)) for a in ('2025','2026')}
    A['uf'] = {a: dict(by(lambda i: i.get('uf') or 'n/d', a)) for a in ('2025','2026')}
    A['mod'] = {a: dict(by(lambda i: i.get('modalidade_licitacao_nome') or 'n/d', a)) for a in ('2025','2026')}
    A['srp'] = {a: sum(1 for i in IT if i['_ano'] == a and i.get('srp')) for a in ('2025','2026')}
    A['temas'] = {a: {t: sum(1 for i in IT if i['_ano'] == a and re.search(rx, i['_d'])) for t, rx in TEMAS} for a in ('2025','2026')}
    vals = collections.defaultdict(list)
    for i in IT:
        v = i.get('valor_total_estimado') or i.get('valor_global')
        if isinstance(v, (int, float)) and 0 < v < 5e8: vals[i['_ano']].append(v)
    A['valores'] = {a: dict(n=len(v), soma=sum(v), mediana=sorted(v)[len(v)//2] if v else 0) for a, v in vals.items()}
    # MG: municípios que compraram em 2024/2025 e ainda não em 2026 (oportunidade de renovação)
    mg = collections.defaultdict(set)
    for i in IT:
        if i.get('uf') == 'MG': mg[i['_ano']].add(i.get('orgao_nome'))
    A['mg'] = {a: len(s) for a, s in mg.items()}
    A['mg_renovar'] = sorted((mg['2024'] | mg['2025']) - mg['2026'])
    A['n'] = len(IT)
    return A

if __name__ == '__main__':
    A = agg()
    print(json.dumps({k: v for k, v in A.items() if k != 'mg_renovar'}, ensure_ascii=False, indent=1)[:4000])
    print('renovar MG:', len(A['mg_renovar']))
