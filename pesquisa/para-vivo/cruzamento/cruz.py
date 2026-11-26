# Cruzamento de dados atuais no Pará: malária (Sespa, boletim 12/2025) x focos de calor (NASA FIRMS, 19-26/11/2026) x insumos.
import json, io, contextlib, re
with contextlib.redirect_stdout(io.StringIO()):
    import par
CSS, FLAG, STRIPE = par.CSS, par.FLAG, par.STRIPE
fmt = par.fmt
D = '../cruz-dl'
F = json.load(open(f'{D}/focos_pa.json'))
FC = F['cnt']; FT = F['total']
geo = json.load(open(f'{D}/mun-pa.json'))
MUN = {}
for f in geo['features']:
    g = f['geometry']
    rings = [p[0] for p in g['coordinates']] if g['type']=='MultiPolygon' else [g['coordinates'][0]]
    MUN[f['properties']['name']] = rings

# Sespa, Boletim nº 12/2025: casos por local provável de infecção, jan-dez
MAL = [('Jacareacanga',9687,7623),('Itaituba',5797,4204),('Oeiras do Pará',589,1535),('Bagre',2575,887),('Altamira',453,721),
       ('Breves',520,696),('Anajás',2222,573),('Almeirim',295,326),('Oriximiná',280,124),('Cametá',6,123)]
MILD = {'Oeiras do Pará','Cametá','Santa Cruz do Arari','Santarém','Altamira','Jacareacanga'}
AREA = [('Garimpo',9748,6842,'#E8692C'),('Rural',9297,5987,'#B8902A'),('Área indígena',4703,4330,'#D9202F'),('Urbana',543,337,'#0071CE')]
for n,_,_ in MAL: assert n in FC, n

N = [0]
def pg(inner, secao, fonte=''):
    N[0] += 1
    return (f'<section class="p">{STRIPE}<div class="top"><span><b>Pará Vivo</b> · cruzamento de dados atuais</span><span>{secao}</span></div>'
            f'{inner}<div class="foot"><span>{fonte}</span><span>{N[0]:02d}</span></div></section>')
head = par.head
pct = lambda a,b: (b-a)/a*100
sg = lambda v: ('+' if v>0 else '−') + f'{abs(v):.0f}%'
P = []

# 1 CAPA
N[0] += 1
P.append(f'''<section class="p" style="padding:0">
  <div style="position:absolute; left:0; right:0; top:0; height:520px">{FLAG}</div>
  <div style="position:absolute; left:0; right:0; top:520px; height:10px; background:var(--ink)"></div>
  <div style="position:absolute; left:90px; right:90px; top:590px">
    <p class="eyebrow">Atualização · 26 de novembro de 2026</p>
    <h1 class="H" style="font-size:128px; margin-top:12px"><span class="ink">Cruzamento</span><span class="azul">de dados</span><span class="verm" style="font-size:84px; margin-top:6px">Malária × fogo × insumos</span></h1>
    <p style="font-size:23px; margin-top:22px; max-width:860px">Os números mais recentes da Sespa cruzados com os focos de calor desta semana, município por município.</p>
  </div>
  <p style="position:absolute; left:90px; bottom:50px; font-size:16px; color:var(--muted)">Complemento do plano Pará Vivo</p>
</section>''')

# 2 MÉTODO
P.append(pg(f'''{head('Como foi feito','Três fontes,','um cruzamento','ink','azul')}
  <div style="display:grid; gap:14px; margin-top:28px">
    <div class="card" style="border-left:8px solid var(--verm)"><p class="H" style="font-size:32px">Malária · Sespa</p><p style="font-size:18px; color:var(--muted); margin-top:4px">Boletim Epidemiológico nº 12/2025: casos de janeiro a dezembro de 2024 e 2025 por município e por tipo de local de infecção, óbitos e envio de testes, remédios e mosquiteiros.</p></div>
    <div class="card" style="border-left:8px solid var(--lar)"><p class="H" style="font-size:32px">Focos de calor · NASA</p><p style="font-size:18px; color:var(--muted); margin-top:4px">Sensor VIIRS do satélite NOAA-20, dados abertos do FIRMS de {F["dates"][0][8:]}/11 a {F["dates"][-1][8:]}/11/2026, confiança nominal e alta. Baixados hoje.</p></div>
    <div class="card" style="border-left:8px solid var(--azul)"><p class="H" style="font-size:32px">Municípios · IBGE</p><p style="font-size:18px; color:var(--muted); margin-top:4px">Limites dos 144 municípios do Pará. Cada foco foi atribuído ao município onde caiu.</p></div>
  </div>
  <div class="card dark" style="margin-top:16px"><p style="font-size:19px"><b style="color:#F6B9BF">Cuidado na leitura:</b> foco de calor não é sinônimo de garimpo nem de malária. O cruzamento aponta <b>onde olhar primeiro</b>; a confirmação vem do campo.</p></div>''', 'Método'))

# 3 PANORAMA MALÁRIA
P.append(pg(f'''{head('Malária 2025','O Pará caiu','28%','ink','mata')}
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:28px">
    <div class="card"><p class="eyebrow" style="color:var(--muted)">Casos confirmados</p><p class="num verm" style="font-size:72px; margin-top:8px; white-space:nowrap">17.514</p><p style="font-size:17px; color:var(--muted)">em 2024: 24.297</p><p style="font-size:17px; margin-top:2px"><b class="mata">−27,9%</b> em 2025</p></div>
    <div class="card"><p class="eyebrow" style="color:var(--muted)">Exames feitos</p><p class="num azul" style="font-size:72px; margin-top:8px; white-space:nowrap">155.602</p><p style="font-size:17px; color:var(--muted)">em 2024: 164.994</p><p style="font-size:17px; margin-top:2px"><b>−5,7%</b> em 2025</p></div>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; margin-top:14px">
    <div class="card"><p class="num verm" style="font-size:54px">67,5%</p><p style="font-size:16px; margin-top:6px">dos casos de 2025 em só dois municípios: Jacareacanga e Itaituba</p></div>
    <div class="card"><p class="num verm" style="font-size:54px">96%</p><p style="font-size:16px; margin-top:6px">dos casos em 10 municípios</p></div>
    <div class="card"><p class="num ink" style="font-size:54px">2</p><p style="font-size:16px; margin-top:6px">mortes em 2025, ambas atendidas em Belém</p></div>
  </div>
  <div class="card" style="margin-top:14px; background:var(--mata-bg); border:0"><p style="font-size:19px"><b class="mata">Leitura cruzada:</b> os casos caíram 28%, mas os exames caíram só 6%. A queda não veio de testar menos: menos pessoas testadas deram positivo.</p></div>''',
  'Malária', 'Sespa, Boletim Epidemiológico de Malária nº 12/2025'))

# 4 MUNICÍPIOS: SOBE E DESCE
mx = 9687
rows = ''
for n,a,b in MAL:
    v = pct(a,b); up = b > a; c = '#D9202F' if up else '#2E7D4F'
    rows += (f'<div style="display:grid; grid-template-columns:190px 1fr 90px; gap:12px; align-items:center; padding:7px 0; border-bottom:1px solid var(--line)">'
             f'<span style="font-size:17px; font-weight:700">{n}</span>'
             f'<div style="display:grid; gap:3px"><span style="height:11px; width:{max(a/mx*100,.6):.1f}%; background:#C8C8C0; border-radius:0 3px 3px 0"></span><span style="height:11px; width:{max(b/mx*100,.6):.1f}%; background:{c}; border-radius:0 3px 3px 0"></span></div>'
             f'<span style="text-align:right; font-weight:800; color:{c}">{sg(v) if a>20 else "×"+str(round(b/a))}</span></div>')
P.append(pg(f'''{head('Onde subiu e onde caiu','Dez municípios,','dois caminhos','ink','verm')}
  <div class="card" style="margin-top:26px; padding:16px 24px">
    <div style="display:flex; gap:20px; font-size:15px; margin-bottom:8px"><span><i style="display:inline-block; width:14px; height:10px; background:#C8C8C0; margin-right:6px"></i>2024</span><span><i style="display:inline-block; width:14px; height:10px; background:#2E7D4F; margin-right:6px"></i>2025 caiu</span><span><i style="display:inline-block; width:14px; height:10px; background:#D9202F; margin-right:6px"></i>2025 subiu</span></div>
    {rows}
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:14px">
    <div class="card" style="background:var(--mata-bg); border:0"><p style="font-size:18px"><b class="mata">Caíram:</b> Jacareacanga, Itaituba, Bagre, Anajás e Oriximiná, de 20.561 para 13.411 casos (−35%).</p></div>
    <div class="card" style="background:var(--verm-bg); border:0"><p style="font-size:18px"><b class="verm">Subiram:</b> Oeiras do Pará (surto no fim de 2024), Altamira, Breves, Almeirim e Cametá (de 6 para 123).</p></div>
  </div>''', 'Municípios', 'Sespa, Boletim nº 12/2025'))

# 5 LOCAL DE INFECÇÃO
mxa = 9748
ar = ''.join(f'<div style="display:grid; grid-template-columns:170px 1fr 120px 80px; gap:12px; align-items:center; padding:9px 0; border-bottom:1px solid var(--line)"><span style="font-size:18px; font-weight:700">{n}</span><div style="display:grid; gap:4px"><span style="height:13px; width:{a/mxa*100:.1f}%; background:#C8C8C0; border-radius:0 3px 3px 0"></span><span style="height:13px; width:{b/mxa*100:.1f}%; background:{c}; border-radius:0 3px 3px 0"></span></div><span style="text-align:right; font-variant-numeric:tabular-nums">{fmt(a)} → <b>{fmt(b)}</b></span><span style="text-align:right; font-weight:800; color:{"#D9202F" if pct(a,b)>-15 else "#2E7D4F"}">{sg(pct(a,b))}</span></div>' for n,a,b,c in AREA)
P.append(pg(f'''{head('Onde a pessoa se infecta','Garimpo lidera,','aldeia não melhora','ink','verm')}
  <div class="card" style="margin-top:26px; padding:16px 24px"><p class="eyebrow" style="color:var(--muted)">Casos por local provável de infecção · 2024 (cinza) e 2025</p>{ar}</div>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; margin-top:14px">
    <div class="card"><p class="num lar" style="font-size:54px">39%</p><p style="font-size:16px; margin-top:6px">dos casos de 2025 vieram do garimpo</p></div>
    <div class="card"><p class="num verm" style="font-size:54px">25%</p><p style="font-size:16px; margin-top:6px">vieram de áreas indígenas</p></div>
    <div class="card"><p class="num ink" style="font-size:54px">−8%</p><p style="font-size:16px; margin-top:6px">foi a queda nas aldeias, contra −30% no garimpo e −36% na zona rural</p></div>
  </div>
  <div class="card dark" style="margin-top:14px"><p style="font-size:19px"><b style="color:#F6B9BF">Conclusão do cruzamento:</b> as terras indígenas ficaram para trás. Elas precisam de ação própria, com DSEI, lideranças e agentes indígenas.</p></div>''',
  'Local de infecção', 'Sespa, Boletim nº 12/2025, Tabela 4'))

# 6 INSUMOS x NECESSIDADE
ins = ''
for n,a,b in MAL[:8]:
    tem = n in MILD
    ins += (f'<tr><td><b>{n}</b></td><td class="r">{fmt(b)}</td><td class="r" style="color:{"#D9202F" if b>a else "#2E7D4F"}">{sg(pct(a,b)) if a>20 else "×"+str(round(b/a))}</td>'
            f'<td><span class="pill" style="background:{"var(--mata-bg)" if tem else "var(--verm-bg)"}; color:{"var(--mata)" if tem else "var(--verm)"}; font-size:13px">{"recebeu" if tem else "não consta"}</span></td></tr>')
P.append(pg(f'''{head('Insumos x necessidade','Mosquiteiro foi','para onde precisa?','ink','azul')}
  <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin-top:26px">
    <div class="card"><p class="num azul" style="font-size:52px">13.600</p><p style="font-size:16px; margin-top:6px">mosquiteiros enviados em 2025</p></div>
    <div class="card"><p class="num azul" style="font-size:52px">46.200</p><p style="font-size:16px; margin-top:6px">testes rápidos distribuídos</p></div>
    <div class="card"><p class="num azul" style="font-size:52px">3.560</p><p style="font-size:16px; margin-top:6px">doses de tafenoquina (dose única para vivax)</p></div>
  </div>
  <div class="card" style="margin-top:14px; padding:14px 22px"><table style="font-size:17px"><thead><tr><th>Município</th><th class="r">Casos 2025</th><th class="r">Variação</th><th>Mosquiteiros 2025</th></tr></thead><tbody>{ins}</tbody></table></div>
  <div class="card dark" style="margin-top:14px"><p style="font-size:19px"><b style="color:#F6B9BF">Lacuna encontrada:</b> pela lista do boletim, Itaituba (2º em casos), Bagre, Breves (em alta) e Anajás não aparecem entre os destinos de mosquiteiros em 2025. Vale confirmar com a Sespa e priorizá-los.</p></div>''',
  'Insumos', 'Sespa, Boletim nº 12/2025: casos (Tabela 2) e mosquiteiros (Quadro 1)'))

# 7 MAPA: FOCOS x MALÁRIA
X0,X1,Y0,Y1 = -59.2,-45.8,-10.1,2.8
W=860; H=int(W*(Y1-Y0)/(X1-X0))
px=lambda x:(x-X0)/(X1-X0)*W; py=lambda y:(Y1-y)/(Y1-Y0)*H
mpaths = ''.join('<path d="' + ''.join('M'+' L'.join(f'{px(a):.1f},{py(b):.1f}' for a,b in r[::3])+'Z' for r in rs) + '"/>' for rs in MUN.values())
G=0.2; grid={}
for x,y in F['pts']:
    k=(int((x+60)//G), int((y+11)//G)); grid[k]=grid.get(k,0)+1
ramp=['#F6D2B5','#F2A774','#E8692C','#C24A12','#8E2F06']; th=[1,4,12,30,70]
def cor(n):
    c=ramp[0]
    for t,col in zip(th,ramp):
        if n>=t: c=col
    return c
cw_=G/(X1-X0)*W; ch_=G/(Y1-Y0)*H
cells=''.join(f'<rect x="{px(-60+i*G):.1f}" y="{py(-11+(j+1)*G):.1f}" width="{cw_:.1f}" height="{ch_:.1f}" fill="{cor(n)}"/>' for (i,j),n in sorted(grid.items(), key=lambda kv:kv[1]))
bub=''
def cent(rs):
    r=max(rs,key=len); xs=[p[0] for p in r]; ys=[p[1] for p in r]; return sum(xs)/len(xs), sum(ys)/len(ys)
for n,a,b in MAL:
    x,y = cent(MUN[n]); rr = 6 + (b/7623)**.5*34
    bub += f'<circle cx="{px(x):.1f}" cy="{py(y):.1f}" r="{rr:.1f}" fill="none" stroke="#D9202F" stroke-width="3.5"/><circle cx="{px(x):.1f}" cy="{py(y):.1f}" r="{rr:.1f}" fill="#D9202F" fill-opacity=".12"/>'
lb = {'Jacareacanga':(0,52),'Itaituba':(0,-40),'Oeiras do Pará':(70,-6),'Bagre':(-50,14),'Altamira':(0,-26),'Breves':(-60,0),'Anajás':(0,-24),'Almeirim':(0,-24),'Oriximiná':(0,-18),'Cametá':(56,18)}
for n,a,b in MAL:
    x,y = cent(MUN[n]); dx,dy = lb[n]
    bub += f'<text x="{px(x)+dx:.1f}" y="{py(y)+dy:.1f}" text-anchor="middle" font-family="Poppins" font-size="15" font-weight="800" fill="#1E2230" stroke="#FAFAF8" stroke-width="4" paint-order="stroke">{n}</text>'
mapa = f'<svg viewBox="-10 -10 {W+20} {H+20}" style="height:640px; width:auto; max-width:100%; display:block; margin:0 auto"><g fill="#F1EFEA" stroke="#C9C6BE" stroke-width=".7">{mpaths}</g>{cells}{bub}</svg>'
P.append(pg(f'''{head('O mapa do cruzamento','Fogo desta semana','e malária de 2025','ink','lar', 80)}
  <div class="card" style="margin-top:20px; padding:12px">{mapa}</div>
  <div style="display:flex; gap:26px; flex-wrap:wrap; margin-top:12px; font-size:15px">
    <span>Focos de calor por quadrado (≈ 22 km): {"".join(f'<i style="display:inline-block; width:16px; height:12px; background:{c}; margin:0 3px 0 8px; vertical-align:middle"></i>{t}+' for t,c in zip(th,ramp))}</span>
    <span><i style="display:inline-block; width:14px; height:14px; border-radius:50%; border:3px solid #D9202F; vertical-align:middle; margin-right:6px"></i>Casos de malária em 2025 (tamanho proporcional)</span>
  </div>''', 'Mapa', f'NASA FIRMS (VIIRS NOAA-20), {F["dates"][0][8:]} a {F["dates"][-1][8:]}/11/2026; Sespa; limites IBGE'))

# 8 TABELA CRUZADA
def sinal(n,a,b):
    f = FC[n]
    if b>a and f>=300: return ('Alerta duplo','#D9202F')
    if b>a: return ('Malária em alta','#E8692C')
    if f>=300: return ('Fogo alto','#B8902A')
    return ('Acompanhar','#5C6170')
tc = ''.join((lambda s: f'<tr><td><b>{n}</b></td><td class="r">{fmt(b)}</td><td class="r" style="color:{"#D9202F" if b>a else "#2E7D4F"}">{sg(pct(a,b)) if a>20 else "×"+str(round(b/a))}</td><td class="r">{fmt(FC[n])}</td><td><span class="pill" style="background:{s[1]}; color:#fff; font-size:13px">{s[0]}</span></td></tr>')(sinal(n,a,b)) for n,a,b in MAL)
topf = sorted(FC.items(), key=lambda kv:-kv[1])[:8]
tf = ''.join(f'<tr><td><b>{n}</b></td><td class="r">{fmt(v)}</td><td class="r">{v/FT*100:.1f}%</td></tr>' for n,v in topf)
P.append(pg(f'''{head('Tabela cruzada','Malária e fogo','por município','ink','verm', 84)}
  <div class="card" style="margin-top:22px; padding:12px 22px"><table style="font-size:16.5px"><thead><tr><th>Município</th><th class="r">Malária 2025</th><th class="r">Variação</th><th class="r">Focos 7 dias</th><th>Sinal</th></tr></thead><tbody>{tc}</tbody></table></div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:14px; align-items:start">
    <div class="card" style="padding:12px 20px"><p class="eyebrow" style="color:var(--muted)">Mais focos na semana</p><table style="font-size:15.5px; margin-top:4px"><tbody>{tf}</tbody></table></div>
    <div class="card dark"><p class="num" style="font-size:56px; color:#F6B9BF">{fmt(FT)}</p><p style="font-size:16px; margin-top:6px; color:#C9CDD6">focos de calor no Pará em 8 dias ({F["dates"][0][8:]} a {F["dates"][-1][8:]}/11/2026)</p><p style="font-size:15px; margin-top:12px">Alerta duplo = malária subiu em 2025 e o município teve 300 focos ou mais na semana.</p></div>
  </div>''', 'Tabela', 'Sespa (malária); NASA FIRMS (focos)'))

# 9 CONCLUSÕES E AJUSTES
alerta = [n for n,a,b in MAL if b>a and FC[n]>=300]
P.append(pg(f'''{head('O que os dados dizem','Cinco conclusões','e ajustes no plano','ink','azul', 80)}
  <div style="display:grid; gap:12px; margin-top:24px">
    <div class="card" style="border-left:8px solid var(--verm)"><p class="H" style="font-size:28px">1 · Tapajós segue o centro</p><p style="font-size:17px; color:var(--muted); margin-top:4px">Jacareacanga e Itaituba têm 2 de cada 3 casos. O polo Tapajós continua prioridade máxima.</p></div>
    <div class="card" style="border-left:8px solid var(--lar)"><p class="H" style="font-size:28px">2 · Novas frentes no Marajó e no Tocantins</p><p style="font-size:17px; color:var(--muted); margin-top:4px">Oeiras do Pará, Cametá e Breves subiram. <b>Ajuste:</b> criar um polo Baixo Tocantins e reforçar o polo Marajó.</p></div>
    <div class="card" style="border-left:8px solid var(--ouro)"><p class="H" style="font-size:28px">3 · Alerta duplo: {", ".join(alerta) if alerta else "nenhum"}</p><p style="font-size:17px; color:var(--muted); margin-top:4px">Malária em alta e muito fogo nesta semana. Visita de campo para entender o que está abrindo a floresta.</p></div>
    <div class="card" style="border-left:8px solid var(--azul)"><p class="H" style="font-size:28px">4 · Mosquiteiros fora do alvo</p><p style="font-size:17px; color:var(--muted); margin-top:4px">Itaituba, Bagre, Breves e Anajás não aparecem nos envios de 2025. <b>Ajuste:</b> mandar para eles os 10.000 mosquiteiros do plano.</p></div>
    <div class="card" style="border-left:8px solid var(--mata)"><p class="H" style="font-size:28px">5 · Aldeias precisam de plano próprio</p><p style="font-size:17px; color:var(--muted); margin-top:4px">Casos em área indígena caíram só 8%. <b>Ajuste:</b> metade dos agentes do polo Tapajós deve ser indígena.</p></div>
  </div>''', 'Conclusões'))

# 10 FONTES E REPETIÇÃO
P.append(pg(f'''{head('Fontes e como repetir','Dados abertos,','atualização semanal','ink','azul', 80)}
  <div class="card" style="margin-top:26px"><ul class="dot" style="gap:12px">
    <li style="font-size:18px">Sespa, Boletim Epidemiológico de Malária nº 12/2025 (janeiro a dezembro de 2024 e 2025), saude.pa.gov.br.</li>
    <li style="font-size:18px">NASA FIRMS, focos VIIRS do NOAA-20, América do Sul, últimos 7 dias, baixados em 26/11/2026.</li>
    <li style="font-size:18px">Limites municipais do IBGE, base pública geodata-br.</li>
  </ul></div>
  <div class="card" style="margin-top:14px"><p class="H azul" style="font-size:30px">Como atualizar</p><p style="font-size:18px; color:var(--muted); margin-top:6px">O programa que conta os focos por município está salvo no repositório. Basta baixar os dados da semana e rodar de novo; com o próximo boletim da Sespa, trocar a tabela de casos. É o começo do sistema Fonte Brasil e do Foco Amazônia funcionando com dados reais.</p></div>
  <div class="card" style="margin-top:14px; background:var(--verm-bg); border:0"><p style="font-size:18px"><b class="verm">Limites:</b> foco de calor mostra fogo, não garimpo nem malária. Os dados da Sespa estão sujeitos a alteração. As conclusões indicam onde agir primeiro e devem ser confirmadas em campo.</p></div>''', 'Fontes'))

html = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Cruzamento de Dados Pará</title>' + CSS + '</head><body>' + ''.join(P) + '</body></html>'
open('cruzamento-para.html','w').write(html)
print('ok', len(P), {n:FC[n] for n,_,_ in MAL}, alerta)
