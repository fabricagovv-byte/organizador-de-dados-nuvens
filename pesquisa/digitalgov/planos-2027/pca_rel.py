import json, re, csv, io, contextlib, unicodedata
with contextlib.redirect_stdout(io.StringIO()):
    import relatorio as R
d = json.load(open('../pca-dl/pca2027.json'))
def norm(s): return unicodedata.normalize('NFKD', (s or '').lower()).encode('ascii','ignore').decode()
brl = R.brl; fmt = R.fmt
def cat(i):
    t = norm(' '.join([i['desc'] or '', i['grupo'] or '', i['classe'] or '']))
    if re.search(r'digitaliz|indexa|gestao de documenta', t) and not re.search(r'mobiliario|canetas', t): return 'Digitalização e gestão de documentos'
    if re.search(r'documento\s*-\s*guarda|guarda de documento|custodia de documento', t): return 'Guarda de documentos'
    if 'acervo' in t and re.search(r'higieniza|inventario|catalog|recupera|conserva', t) and not re.search(r'pintura|aplicacao:|capacitacao', t): return 'Organização e preservação de acervo'
    if re.search(r'locacao de imovel|imovel destinado', t): return 'Aluguel de imóvel para arquivo'
    if re.search(r'caixa|pasta', t): return 'Material de arquivo em papel'
    return None
IT = [dict(i, cat=cat(i)) for i in d['itens']]
IT = [i for i in IT if i['cat']]
lidos = len(d['orgaos']); com = [o for o in d['orgaos'] if o['tem_pca']]
dig = [i for i in IT if i['cat'] in ('Digitalização e gestão de documentos','Guarda de documentos','Organização e preservação de acervo')]
sinal = [i for i in IT if i['cat'] in ('Aluguel de imóvel para arquivo','Material de arquivo em papel')]
tot_dig = sum(i['valor'] or 0 for i in dig)
porg = {}
for i in dig: porg.setdefault((i['orgao'], i['uf']), []).append(i)
# planilha
with open('Planos-2027-digitalizacao.csv','w',newline='',encoding='utf-8-sig') as f:
    w = csv.writer(f, delimiter=';'); w.writerow(['Órgão','UF','Categoria','Descrição','Quantidade','Unidade','Valor previsto (R$)','Data desejada','Classe do catálogo'])
    for i in IT: w.writerow([i['orgao'], i['uf'], i['cat'], (i['desc'] or i['grupo'] or '').strip(), i['qtd'], i['un'], f"{(i['valor'] or 0):.2f}".replace('.',','), (i['data'] or '')[:10], i['classe']])
N = [0]
def pg(inner, secao, fonte=''):
    N[0] += 1
    return (f'<section class="p">{R.STRIPE}<div class="top"><span><b>DigitalGov</b> · planos de contratação 2027</span><span>{secao}</span></div>'
            f'{inner}<div class="foot"><span>{fonte}</span><span>{N[0]:02d}</span></div></section>')
head = R.head
P = []
N[0] += 1
P.append(f'''<section class="p" style="padding:0; background:var(--ink); background-image:none">
  <div style="position:absolute; left:90px; right:90px; top:300px; color:#fff">
    <p class="eyebrow" style="color:#7FA6F0">Plano de Contratações Anual (PCA) 2027 · PNCP</p>
    <h1 class="H" style="font-size:126px; margin-top:16px"><span>Quem vai</span><span style="color:#7FE0A8">digitalizar</span><span>em 2027</span></h1>
    <p style="font-size:24px; margin-top:24px; max-width:860px; color:#D5DCEA">O que os órgãos públicos escreveram no plano do ano que vem: digitalização, guarda de documentos, acervos e sinais de papel acumulado.</p>
  </div>
  <p style="position:absolute; left:90px; bottom:50px; color:#8C97AE; font-size:16px; font-family:var(--fm); letter-spacing:.1em">CONSULTA DE 27 DE NOVEMBRO DE 2026</p>
</section>''')
P.append(pg(f'''{head('Resumo','O que os planos','mostram','ink','verde')}
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; margin-top:26px">
    <div class="card"><p class="num azul" style="font-size:60px">{lidos}</p><p style="font-size:16px; margin-top:6px">órgãos que compram digitalização tiveram o plano de 2027 consultado</p></div>
    <div class="card"><p class="num azul" style="font-size:60px">{len(com)}</p><p style="font-size:16px; margin-top:6px">já publicaram o plano de 2027 no PNCP</p></div>
    <div class="card"><p class="num verde" style="font-size:60px">{len(porg)}</p><p style="font-size:16px; margin-top:6px">planejaram digitalização, guarda ou tratamento de acervo</p></div>
  </div>
  <div class="card dark" style="margin-top:16px"><p class="eyebrow" style="color:#7FE0A8">Valor previsto em digitalização e documentos</p><p class="num" style="font-size:80px; margin-top:8px">{brl(tot_dig)}</p><p style="font-size:17px; color:#C9CDD6; margin-top:6px">somando os itens desses órgãos para 2027</p></div>
  <div class="card" style="margin-top:16px; background:var(--lar-bg); border:0"><p style="font-size:19px"><b class="lar">Importante:</b> {lidos-len(com)} dos {lidos} órgãos ainda não publicaram o plano de 2027, a maioria prefeituras. Muitos municípios publicam no início do ano ou não usam o PNCP para isso. Quem ainda não planejou pode ser convencido agora.</p></div>''', 'Resumo', 'PNCP: consolidado e itens do PCA 2027 de cada órgão'))
blocos = []
for (o,u), its in sorted(porg.items(), key=lambda kv: -sum(i['valor'] or 0 for i in kv[1])):
    rows = f'<tr style="background:rgba(19,32,58,.04)"><td colspan="3"><b>{o.title()}</b> · {u}</td><td class="r"><b>{brl(sum(i["valor"] or 0 for i in its))}</b></td></tr>'
    for i in its:
        q = f'{fmt(i["qtd"])} {i["un"] if i["un"] and i["un"] != "-" else ""}'.strip() if i['qtd'] else '—'
        rows += f'<tr><td style="font-size:14.5px">{(i["desc"] or i["grupo"] or "").strip()[:95]}</td><td style="font-size:13px; color:var(--muted)">{i["cat"]}</td><td class="r" style="font-size:14px">{q}</td><td class="r" style="font-size:14.5px">{brl(i["valor"] or 0)}</td></tr>'
    blocos.append((rows, len(its)+1))
paginas = [[]]; cont = 0
for r_, n_ in blocos:
    if cont + n_ > 15 and paginas[-1]: paginas.append([]); cont = 0
    paginas[-1].append(r_); cont += n_
for k, pgr in enumerate(paginas):
    P.append(pg(f'''{head('Itens planejados','Digitalização',f'no plano de 2027 · {k+1}/{len(paginas)}','ink','azul', 80)}
  <div class="card" style="margin-top:22px; padding:12px 20px"><table><thead><tr><th>Descrição no plano</th><th>Tipo</th><th class="r">Quantidade</th><th class="r">Valor previsto</th></tr></thead><tbody>{''.join(pgr)}</tbody></table></div>''', 'Itens', 'PNCP, PCA 2027; quantidade e valor como informados pelo órgão'))
srows = ''.join(f'<tr><td><b>{i["orgao"].title()}</b> · {i["uf"]}</td><td style="font-size:14.5px">{(i["desc"] or i["classe"] or "").strip()[:70]}</td><td class="r">{fmt(i["qtd"] or 0)}</td><td class="r">{brl(i["valor"] or 0)}</td></tr>' for i in sorted(sinal, key=lambda x: -(x['valor'] or 0))[:10])
alug = sum(i['valor'] or 0 for i in sinal if i['cat'] == 'Aluguel de imóvel para arquivo')
P.append(pg(f'''{head('Sinais de oportunidade','Quem ainda','vive no papel','ink','lar', 84)}
  <div class="card" style="margin-top:22px; padding:12px 20px"><table><thead><tr><th>Órgão</th><th>Item planejado</th><th class="r">Qtd.</th><th class="r">Valor</th></tr></thead><tbody>{srows}</tbody></table></div>
  <div class="card dark" style="margin-top:14px"><p style="font-size:19px"><b style="color:#7FE0A8">Argumento de venda:</b> Viçosa do Ceará planeja gastar {brl(alug)} por ano só com aluguel de imóveis para guardar arquivo, além de milhares de pastas e caixas. Digitalizar libera esses imóveis e paga parte do projeto.</p></div>''', 'Sinais', 'PNCP, PCA 2027'))
P.append(pg(f'''{head('Como usar','Próximos','passos','ink','verde')}
  <div style="display:grid; gap:12px; margin-top:26px">
    <div class="card" style="border-left:8px solid var(--verde)"><p class="H" style="font-size:30px">1 · Ligar para quem já planejou</p><p style="font-size:18px; color:var(--muted); margin-top:4px">Viçosa do Ceará, Ministério das Relações Exteriores e Ministério da Ciência, Tecnologia e Inovações já têm verba prevista. Apresentar a DigitalGov antes do edital e responder às cotações de preço.</p></div>
    <div class="card" style="border-left:8px solid var(--azul)"><p class="H" style="font-size:30px">2 · Converter quem guarda papel</p><p style="font-size:18px; color:var(--muted); margin-top:4px">Órgãos que planejam caixas, pastas e aluguel de arquivo são clientes de digitalização em potencial.</p></div>
    <div class="card" style="border-left:8px solid var(--lar)"><p class="H" style="font-size:30px">3 · Chegar antes do plano</p><p style="font-size:18px; color:var(--muted); margin-top:4px">A maioria das prefeituras ainda não publicou o plano de 2027. Visitar agora para que a digitalização entre no plano.</p></div>
  </div>
  <div class="card" style="margin-top:14px; background:var(--lar-bg); border:0"><p style="font-size:17.5px"><b class="lar">Limites:</b> foram lidos {lidos} dos 221 órgãos da lista, porque o PNCP limita as consultas. A consulta nacional de planos por tipo de serviço (classe 1682, digitalização e indexação) retornou erro no servidor do PNCP durante esta pesquisa. A planilha anexa traz todos os itens encontrados.</p></div>''', 'Próximos passos'))
html = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Planos 2027 Digitalização</title>' + R.CSS + '</head><body>' + ''.join(P) + '</body></html>'
open('pca2027.html','w').write(html)
print('ok', lidos, len(com), len(porg), tot_dig, alug, len(IT))
