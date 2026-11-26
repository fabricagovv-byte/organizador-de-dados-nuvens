# Relatório "Malária no Amapá" em páginas 1080x1350, no estilo dos posts da ibradep.
FLAG = open('bandeira-amapa.svg').read().replace('height="700" width="1000"', 'viewBox="0 0 1000 700" style="width:100%; height:100%; display:block"')

CSS = '''
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,800;1,700;1,800&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Papel quadriculado branco, títulos condensados em caixa alta: lima, grafite e laranja. Cores do Amapá como apoio. */
:root{
  --paper:#FBFBF8; --grid:rgba(30,40,30,.06); --ink:#2B2B2B; --muted:#5E615C;
  --lima:#C2C930; --laranja:#E8692C; --verde:#3F8A2E; --card:#F1F1EE;
  --ap-azul:#002580; --ap-verde:#00994C; --ap-amarelo:#F3E718;
  --fh:"Anton", "Impact", "Arial Narrow", sans-serif; --fb:"Poppins", "Segoe UI", Arial, sans-serif; --fm:"IBM Plex Mono", monospace;
}
@page{ size:1080px 1350px; margin:0 }
*{box-sizing:border-box; margin:0; padding:0}
body{font-family:var(--fb); color:var(--ink); -webkit-print-color-adjust:exact; print-color-adjust:exact; background:var(--paper)}
.p{width:1080px; height:1350px; position:relative; overflow:hidden; page-break-after:always; break-after:page;
   background-color:var(--paper);
   background-image:linear-gradient(var(--grid) 1px, transparent 1px), linear-gradient(90deg, var(--grid) 1px, transparent 1px);
   background-size:36px 36px; padding:90px 96px}
.p:last-child{page-break-after:auto}
.hash{font-family:var(--fb); font-weight:800; font-size:24px; letter-spacing:.01em; text-align:center}
.hash span{font-weight:500}
.H{font-family:var(--fh); font-weight:400; text-transform:uppercase; line-height:.9; letter-spacing:-.005em}
.H > span{display:block; line-height:.93} .H > br{display:none} p.H{line-height:1.08}
.lima{color:var(--lima)} .lar{color:var(--laranja)} .ink{color:var(--ink)} .verde{color:var(--verde)}
p{font-size:26px; line-height:1.45}
.lead{font-size:28px; font-weight:500}
.box{background:var(--card); border-radius:14px; padding:30px 36px}
.num{font-family:var(--fh); font-weight:400; line-height:.95}
.small{font-size:20px; color:var(--muted); line-height:1.4}
.foot{position:absolute; left:96px; right:96px; bottom:52px; display:flex; justify-content:space-between; align-items:center; font-size:18px; color:var(--muted)}
.foot b{color:var(--ink)}
ul.dot{list-style:none; display:grid; gap:14px}
ul.dot li{position:relative; padding-left:32px; font-size:25px; line-height:1.4}
ul.dot li::before{content:""; position:absolute; left:4px; top:.55em; width:12px; height:12px; background:var(--laranja); transform:rotate(45deg)}
.tag{display:inline-block; font-weight:700; font-size:18px; padding:6px 14px; border-radius:6px; background:var(--ink); color:#fff; letter-spacing:.02em}
.mono{font-family:var(--fm)}
.flagbar{position:absolute; left:0; right:0; top:0; height:16px; display:flex}
.flagbar i{flex:1}
</style>'''

def foot(n, fonte=''):
    return f'<div class="foot"><span>{fonte}</span><span><b>#AmapáNoCombateÀMalária</b> · {n:02d}</span></div>'

FB = '<div class="flagbar"><i style="background:var(--ap-azul)"></i><i style="background:var(--ap-verde)"></i><i style="background:var(--ap-amarelo)"></i></div>'

pages = []

# 1 CAPA com a bandeira
pages.append(f'''<section class="p" style="padding:0">
  <div style="position:absolute; left:0; right:0; top:0; height:756px">{FLAG}</div>
  <div style="position:absolute; left:0; right:0; top:756px; bottom:0; padding:56px 96px 0">
    <p class="hash" style="text-align:left"><b>#AMAPÁ</b><span>NO</span><b>COMBATE</b><span>À</span><b>MALÁRIA</b></p>
    <h1 class="H" style="font-size:150px; margin-top:14px"><span class="ink">Malária</span> <span class="lar">no Amapá</span></h1>
    <p class="lead" style="margin-top:22px; max-width:860px">Dados cruzados, causas locais, época de maior risco, o que fazer e como criar campanhas que funcionam.</p>
    <p class="small" style="margin-top:22px">Pesquisa · novembro de 2026</p>
  </div>
</section>''')

# 2 Números
pages.append(f'''<section class="p">{FB}
  <p class="hash"><b>#AMAPÁ</b><span>NO</span><b>COMBATE</b><span>À</span><b>MALÁRIA</b></p>
  <h2 class="H" style="font-size:120px; margin-top:26px; text-align:center"><span class="lima">A malária</span><br><span class="ink">em números</span></h2>
  <div style="margin-top:56px; display:grid; grid-template-columns:1fr 1fr; gap:22px">
    <div class="box"><p class="num lar" style="font-size:104px">112.204</p><p style="font-size:23px; margin-top:8px">casos no Amapá de 2014 a 2024</p></div>
    <div class="box"><p class="num lar" style="font-size:104px">91%</p><p style="font-size:23px; margin-top:8px">por <i>Plasmodium vivax</i>, o tipo que volta meses depois se o tratamento não for completo</p></div>
    <div class="box"><p class="num ink" style="font-size:104px">6.413</p><p style="font-size:23px; margin-top:8px">casos em 2024, o dobro de 2022 (3.094)</p></div>
    <div class="box"><p class="num verde" style="font-size:104px">−16,8%</p><p style="font-size:23px; margin-top:8px">de casos no 1º trimestre de 2025: 1.017 contra 1.222 em 2024</p></div>
  </div>
  <div class="box" style="margin-top:22px; background:var(--ink); color:#fff"><p style="font-size:25px"><b style="color:var(--lima)">Macapá caiu 82%</b> entre 2024 e 2025 (de 660 para 120 casos notificados, segundo a vigilância municipal). Prova de que ação organizada funciona.</p></div>
  {foot(2, 'SIVEP-Malária via Oliveira et al. (2025); Ministério da Saúde; Prefeitura de Macapá')}
</section>''')

# 3 Série histórica
serie = [(2014,14721),(2015,15381),(2016,13501),(2017,16566),(2018,16337),(2019,11659),(2020,3794),(2021,4416),(2022,3094),(2023,6322),(2024,6413)]
mx = 17000; ch = 560
bars = ''
for i,(a,v) in enumerate(serie):
    h = v/mx*ch; x = 30 + i*80
    cor = '#E8692C' if a >= 2023 else ('#B9B9B2' if a in (2020,2021,2022) else '#2B2B2B')
    bars += f'<rect x="{x}" y="{ch-h+20:.0f}" width="56" height="{h:.0f}" rx="4" fill="{cor}"/>'
    bars += f'<text x="{x+28}" y="{ch+52}" text-anchor="middle" font-family="Poppins" font-size="19" fill="#5E615C">{a}</text>'
    if a in (2017, 2022, 2024):
        bars += f'<text x="{x+28}" y="{ch-h+8:.0f}" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="20" fill="#2B2B2B">{v:,}</text>'.replace(',', '.')
grid = ''.join(f'<line x1="20" x2="900" y1="{ch-v/mx*ch+20:.0f}" y2="{ch-v/mx*ch+20:.0f}" stroke="rgba(30,40,30,.12)"/><text x="910" y="{ch-v/mx*ch+26:.0f}" font-family="Poppins" font-size="16" fill="#5E615C">{v//1000} mil</text>' for v in (0,5000,10000,15000))
pages.append(f'''<section class="p">{FB}
  <p class="hash"><b>#AMAPÁ</b><span>NO</span><b>COMBATE</b><span>À</span><b>MALÁRIA</b></p>
  <h2 class="H" style="font-size:96px; margin-top:22px"><span class="ink">Caiu, mas</span><br><span class="lar">voltou a subir</span></h2>
  <p class="lead" style="margin-top:20px">Casos de malária por ano no Amapá</p>
  <svg viewBox="0 0 980 640" style="width:800px; margin-top:10px">{grid}{bars}</svg>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:22px; margin-top:20px">
    <div class="box"><p style="font-size:22px"><b>Cinza (2020–2022):</b> a queda coincide com a pandemia, quando menos gente foi testada. Parte dela pode ser subnotificação.</p></div>
    <div class="box"><p style="font-size:22px"><b class="lar">Laranja (2023–2024):</b> os casos dobraram em relação a 2022. O alerta voltou.</p></div>
  </div>
  {foot(3, 'SIVEP-Malária, casos autóctones, via Oliveira et al. (2025)')}
</section>''')

# 4 Municípios
mun = [('Calçoene',17911),('Mazagão',15864),('Santana',15467),('Pedra Branca do Amapari',14390),('Porto Grande',12965),('Oiapoque',11355),('Macapá',10374),('Serra do Navio',6510),('Tartarugalzinho',3449),('Laranjal do Jari',1748),('Ferreira Gomes',1447),('Vitória do Jari',351),('Pracuúba',129),('Cutias',98),('Itaubal',73),('Amapá',73)]
rows = ''.join(
    f'<div style="display:grid; grid-template-columns:330px 1fr 120px; gap:16px; align-items:center; font-size:20px">'
    f'<span style="font-weight:{700 if i<3 else 500}">{n}</span>'
    f'<span style="height:24px; background:rgba(30,40,30,.07); border-radius:0 5px 5px 0; overflow:hidden"><span style="display:block; height:100%; width:{max(v/17911*100,.6):.1f}%; background:{"#E8692C" if i<3 else "#2B2B2B"}; border-radius:0 5px 5px 0"></span></span>'
    f'<span style="text-align:right; font-variant-numeric:tabular-nums">{v:,}</span></div>'.replace(',', '.') for i,(n,v) in enumerate(mun))
pages.append(f'''<section class="p">{FB}
  <p class="hash"><b>#AMAPÁ</b><span>NO</span><b>COMBATE</b><span>À</span><b>MALÁRIA</b></p>
  <h2 class="H" style="font-size:96px; margin-top:22px"><span class="ink">Onde a malária</span><br><span class="lar">mais aparece</span></h2>
  <p class="lead" style="margin-top:16px">Casos por município, soma de 2014 a 2024</p>
  <div style="display:grid; gap:9px; margin-top:24px">{rows}</div>
  <div class="box" style="margin-top:22px; padding:22px 30px"><p style="font-size:21px"><b class="lar">Calçoene, Mazagão e Santana</b> somam 44% dos casos. Os 7 primeiros municípios concentram 88%: é ali que a campanha precisa começar.</p></div>
  {foot(4, 'SIVEP-Malária via Oliveira et al. (2025)')}
</section>''')

# 5 Quem
pages.append(f'''<section class="p">{FB}
  <p class="hash"><b>#AMAPÁ</b><span>NO</span><b>COMBATE</b><span>À</span><b>MALÁRIA</b></p>
  <h2 class="H" style="font-size:108px; margin-top:26px"><span class="lima">Quem mais</span><br><span class="ink">pega malária</span></h2>
  <div style="margin-top:46px; display:grid; grid-template-columns:repeat(3,1fr); gap:20px">
    <div class="box"><p class="num lar" style="font-size:88px">63%</p><p style="font-size:22px; margin-top:6px">são homens</p></div>
    <div class="box"><p class="num lar" style="font-size:88px">30%</p><p style="font-size:22px; margin-top:6px">trabalham na roça ou no garimpo</p></div>
    <div class="box"><p class="num lar" style="font-size:88px">8,6%</p><p style="font-size:22px; margin-top:6px">são indígenas, bem acima do peso deles na população</p></div>
  </div>
  <div class="box" style="margin-top:22px">
    <p style="font-size:24px; font-weight:700">Profissões com mais casos (2014–2024)</p>
    <div style="display:grid; gap:14px; margin-top:18px">
      <div style="display:grid; grid-template-columns:240px 1fr 90px; gap:14px; align-items:center; font-size:22px"><span>Agricultura</span><span style="height:22px; background:rgba(30,40,30,.07)"><span style="display:block; height:100%; width:100%; background:#2B2B2B"></span></span><span style="text-align:right">16,9%</span></div>
      <div style="display:grid; grid-template-columns:240px 1fr 90px; gap:14px; align-items:center; font-size:22px"><span>Garimpo</span><span style="height:22px; background:rgba(30,40,30,.07)"><span style="display:block; height:100%; width:77.8%; background:#E8692C"></span></span><span style="text-align:right">13,1%</span></div>
      <div style="display:grid; grid-template-columns:240px 1fr 90px; gap:14px; align-items:center; font-size:22px"><span>Trabalho doméstico</span><span style="height:22px; background:rgba(30,40,30,.07)"><span style="display:block; height:100%; width:54.1%; background:#2B2B2B"></span></span><span style="text-align:right">9,1%</span></div>
    </div>
  </div>
  <div class="box" style="margin-top:22px; background:var(--ink); color:#fff"><p style="font-size:24px"><b style="color:var(--lima)">88% dos casos foram achados porque a pessoa procurou o posto.</b> Só 12% vieram de busca ativa. Ir até garimpos, roças e aldeias encontra quem ainda não foi diagnosticado.</p></div>
  {foot(5, 'SIVEP-Malária via Oliveira et al. (2025)')}
</section>''')

# 6 Causas locais
causas = [
  ('Garimpo', 'Cavas e poças paradas viram criadouro. Calçoene (Lourenço) lidera os casos do estado.'),
  ('Roça e desmatamento', 'Abrir mata para plantar aproxima as pessoas do mosquito, sobretudo em assentamentos.'),
  ('Beira de rio e várzea', 'Mazagão, Santana e ressacas de Macapá têm água parada perto das casas.'),
  ('Fronteira e migração', 'Oiapoque recebe gente da Guiana Francesa e de garimpos de outros estados, que traz o parasita.'),
  ('Aldeias indígenas', 'Oiapoque e Pedra Branca têm incidência muito maior entre indígenas e acesso difícil ao exame.'),
  ('Diagnóstico tardio', 'Quem mora longe demora a testar e a tratar. Tratamento incompleto faz o vivax voltar.'),
]
cards = ''.join(f'<div class="box" style="padding:24px 28px"><p class="H lar" style="font-size:40px">{t}</p><p style="font-size:21px; margin-top:8px">{d}</p></div>' for t,d in causas)
pages.append(f'''<section class="p">{FB}
  <p class="hash"><b>#AMAPÁ</b><span>NO</span><b>COMBATE</b><span>À</span><b>MALÁRIA</b></p>
  <h2 class="H" style="font-size:108px; margin-top:26px"><span class="ink">Por que acontece</span><br><span class="lar">aqui no Amapá</span></h2>
  <p class="lead" style="margin-top:16px">Causas locais, cruzando municípios, profissões e território</p>
  <div style="margin-top:34px; display:grid; grid-template-columns:1fr 1fr; gap:18px">{cards}</div>
  <div class="box" style="margin-top:18px; background:var(--ink); color:#fff"><p style="font-size:23px"><b style="color:var(--lima)">O transmissor</b> é o mosquito-prego (<i>Anopheles darlingi</i>), que pica mais <b>ao entardecer e ao amanhecer</b> e se cria em água limpa e parada.</p></div>
  {foot(6, 'Oliveira et al. (2025); Ministério da Saúde; estudos em Oiapoque')}
</section>''')

# 7 Calendário de risco
meses = ['JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']
chuva = [3,4,5,5,4,3,2,1,1,1,1,2]
risco = [1,1,1,1,2,3,3,3,3,2,1,1]
cores_r = {1:'#D9D9D2',2:'#F2B48E',3:'#E8692C'}
cal = ''.join(
    f'<div style="display:grid; gap:8px; justify-items:center">'
    f'<span style="width:48px; height:{chuva[i]*24}px; background:#5AA0D6; border-radius:4px 4px 0 0; align-self:end"></span>'
    f'<span style="width:62px; height:62px; border-radius:10px; background:{cores_r[risco[i]]}"></span>'
    f'<span style="font-weight:700; font-size:18px">{m}</span></div>' for i,m in enumerate(meses))
pages.append(f'''<section class="p">{FB}
  <p class="hash"><b>#AMAPÁ</b><span>NO</span><b>COMBATE</b><span>À</span><b>MALÁRIA</b></p>
  <h2 class="H" style="font-size:108px; margin-top:26px"><span class="ink">Quando os casos</span><br><span class="lar">crescem</span></h2>
  <div class="box" style="margin-top:40px; padding:36px">
    <div style="display:grid; grid-template-columns:repeat(12,1fr); align-items:end; height:250px">{cal}</div>
    <div style="display:flex; gap:28px; margin-top:26px; font-size:19px; flex-wrap:wrap">
      <span><i style="display:inline-block; width:18px; height:18px; background:#5AA0D6; vertical-align:middle; margin-right:8px"></i>Chuva (inverno amazônico)</span>
      <span><i style="display:inline-block; width:18px; height:18px; background:#E8692C; vertical-align:middle; margin-right:8px"></i>Risco maior</span>
      <span><i style="display:inline-block; width:18px; height:18px; background:#F2B48E; vertical-align:middle; margin-right:8px"></i>Risco subindo</span>
    </div>
  </div>
  <div style="display:grid; gap:12px; margin-top:20px">
    <div class="box"><p style="font-size:23px"><b class="lar">Junho a setembro:</b> as chuvas param, os rios baixam e deixam poças e remansos de água limpa. É quando o mosquito mais se multiplica.</p></div>
    <div class="box"><p style="font-size:23px"><b>Garimpo:</b> o risco vale o ano todo, porque as cavas ficam cheias de água em qualquer mês.</p></div>
    <div class="box"><p style="font-size:23px"><b class="verde">Hora de agir:</b> abril e maio, antes do pico. Campanha depois que os casos sobem chega tarde.</p></div>
  </div>
  <p class="small" style="margin-top:14px; font-size:18px">Padrão observado na Amazônia. Confirme com os dados mensais do SIVEP-Malária de cada município antes de fixar o calendário.</p>
  {foot(7, 'Padrão amazônico; INMET (chuvas); SIVEP-Malária')}
</section>''')

# 8 O que fazer — população
pages.append(f'''<section class="p">{FB}
  <p class="hash"><b>#AMAPÁ</b><span>NO</span><b>COMBATE</b><span>À</span><b>MALÁRIA</b></p>
  <h2 class="H" style="font-size:96px; margin-top:26px; text-align:center"><span class="lima">O que fazer se tiver</span><br><span class="ink" style="font-size:118px">sintomas de</span><br><span class="lar" style="font-size:190px">malária?</span></h2>
  <p style="text-align:center; font-size:26px; margin-top:16px">SENTIU <b>FEBRE ALTA, CALAFRIOS E MUITO CANSAÇO?</b> NÃO IGNORE!</p>
  <div class="box" style="margin-top:26px">
    <ul class="dot">
      <li>Vá logo a um <b>posto de saúde</b>. O exame é gratuito no SUS.</li>
      <li>Faça o <b>teste</b>: o resultado sai no mesmo dia.</li>
      <li>Tome o remédio <b>até o fim</b>, mesmo se melhorar. O vivax volta se o tratamento parar.</li>
    </ul>
  </div>
  <div class="box" style="margin-top:20px">
    <p style="font-size:24px; font-weight:700">Para se proteger</p>
    <ul class="dot" style="margin-top:12px">
      <li>Durma em <b>mosquiteiro</b>, de preferência impregnado.</li>
      <li>Use <b>repelente</b> e roupa comprida ao entardecer e ao amanhecer.</li>
      <li>Coloque <b>tela</b> em portas e janelas.</li>
    </ul>
  </div>
  <p class="H" style="text-align:center; font-size:44px; margin-top:28px; font-style:italic">Quanto mais cedo tratar, menor o risco de complicações!</p>
  {foot(8, 'Ministério da Saúde')}
</section>''')

# 9 O que fazer — gestão
acoes = [
  ('Busca ativa', 'Equipes com teste rápido em garimpos, roças, ramais e aldeias, não só no posto.'),
  ('Tratar até o fim', 'Acompanhar cada paciente com vivax até a última dose. A tafenoquina, de dose única, já é usada no SUS com teste prévio de G6PD.'),
  ('Microplanejamento', 'Mapa de casos por localidade, semana a semana, para mandar as equipes aonde o caso nasceu.'),
  ('Controle do mosquito', 'Mosquiteiros impregnados, borrifação nas casas de maior risco e manejo de criadouros.'),
  ('Saúde indígena', 'Ações com DSEI e lideranças, em português e nas línguas locais.'),
  ('Fronteira', 'Troca de dados com a Guiana Francesa e atendimento ao migrante sem barreira.'),
]
cards = ''.join(f'<div class="box" style="padding:24px 28px"><p class="H ink" style="font-size:38px">{t}</p><p style="font-size:21px; margin-top:8px">{d}</p></div>' for t,d in acoes)
pages.append(f'''<section class="p">{FB}
  <p class="hash"><b>#AMAPÁ</b><span>NO</span><b>COMBATE</b><span>À</span><b>MALÁRIA</b></p>
  <h2 class="H" style="font-size:108px; margin-top:26px"><span class="lar">O que gestores</span><br><span class="ink">podem fazer</span></h2>
  <div style="margin-top:40px; display:grid; grid-template-columns:1fr 1fr; gap:18px">{cards}</div>
  <div class="box" style="margin-top:18px; background:var(--ink); color:#fff"><p style="font-size:23px"><b style="color:var(--lima)">Meta:</b> o Amapá tem plano estadual para eliminar a malária até 2035, alinhado à meta nacional. O Brasil teve em 2025 cerca de 118 mil casos, o menor número em quase 50 anos.</p></div>
  {foot(9, 'Ministério da Saúde; Governo do Amapá')}
</section>''')

# 10 Como criar campanhas
publicos = [
  ('Garimpeiros', 'Teste rápido no barranco, mensagem curta por áudio de WhatsApp e rádio.'),
  ('Agricultores', 'Agente na feira e no ramal; cartaz no comércio e na igreja.'),
  ('Indígenas', 'Feita com as lideranças, nas línguas locais e com agentes indígenas.'),
  ('Ribeirinhos', 'Rádio comunitária, barco da saúde e aviso no porto.'),
  ('Escolas', 'Alunos levam o recado para casa: mosquiteiro e febre = posto.'),
  ('Fronteira', 'Material em português, francês e crioulo em Oiapoque.'),
]
rows = ''.join(f'<div style="display:grid; grid-template-columns:240px 1fr; gap:20px; padding:9px 0; border-bottom:1px solid rgba(30,40,30,.12)"><b class="H lar" style="font-size:30px">{a}</b><span style="font-size:20px">{b}</span></div>' for a,b in publicos)
pages.append(f'''<section class="p">{FB}
  <p class="hash"><b>#AMAPÁ</b><span>NO</span><b>COMBATE</b><span>À</span><b>MALÁRIA</b></p>
  <h2 class="H" style="font-size:88px; margin-top:22px"><span class="ink">Como criar</span><br><span class="lima">campanhas que funcionam</span></h2>
  <div style="display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-top:26px">
    <div class="box" style="padding:20px"><p class="H lar" style="font-size:30px">1 · Onde</p><p style="font-size:19px; margin-top:6px">Os 7 municípios e localidades com mais casos</p></div>
    <div class="box" style="padding:20px"><p class="H lar" style="font-size:30px">2 · Quem</p><p style="font-size:19px; margin-top:6px">Um público por vez, com mensagem própria</p></div>
    <div class="box" style="padding:20px"><p class="H lar" style="font-size:30px">3 · Quando</p><p style="font-size:19px; margin-top:6px">Abril e maio, antes do pico</p></div>
    <div class="box" style="padding:20px"><p class="H lar" style="font-size:30px">4 · Medir</p><p style="font-size:19px; margin-top:6px">Testes feitos, tempo até o tratamento, casos</p></div>
  </div>
  <div class="box" style="margin-top:16px; padding:8px 30px">{rows}</div>
  <div class="box" style="margin-top:14px; padding:22px 30px; background:var(--ink); color:#fff"><p style="font-size:20px"><b style="color:var(--lima)">Regra de ouro:</b> uma mensagem só por peça. Sintoma, posto, exame, tratamento completo. Linguagem simples e pessoas da própria comunidade.</p></div>
  {foot(10)}
</section>''')

# 11 Calendário de campanha
etapas = [
  ('JAN–MAR','Preparar','Mapear localidades, treinar agentes, produzir materiais e estocar testes e mosquiteiros.','#B9B9B2'),
  ('ABR–MAI','Lançar','Campanha no 25 de abril, Dia Mundial da Malária. Mosquiteiros e busca ativa antes do pico.','#C2C930'),
  ('JUN–SET','Intensificar','Pico de risco: teste rápido em garimpos e roças, rádio diário, alerta por WhatsApp.','#E8692C'),
  ('OUT–DEZ','Avaliar','Comparar casos com o ano anterior, ouvir a comunidade e ajustar o plano seguinte.','#3F8A2E'),
]
et = ''.join(f'<div style="display:grid; grid-template-columns:190px 1fr; gap:24px; align-items:start"><div style="background:{c}; color:{"#fff" if c in ("#E8692C","#3F8A2E") else "#2B2B2B"}; border-radius:12px; padding:20px; text-align:center"><p class="H" style="font-size:34px">{m}</p></div><div class="box" style="padding:20px 26px"><p class="H" style="font-size:40px">{t}</p><p style="font-size:22px; margin-top:6px">{d}</p></div></div>' for m,t,d,c in etapas)
pages.append(f'''<section class="p">{FB}
  <p class="hash"><b>#AMAPÁ</b><span>NO</span><b>COMBATE</b><span>À</span><b>MALÁRIA</b></p>
  <h2 class="H" style="font-size:108px; margin-top:26px"><span class="ink">Calendário</span><br><span class="lar">da campanha</span></h2>
  <div style="display:grid; gap:20px; margin-top:46px">{et}</div>
  <div class="box" style="margin-top:28px; background:var(--ink); color:#fff"><p style="font-size:23px"><b style="color:var(--lima)">Canais:</b> Instagram e WhatsApp nas cidades; rádio comunitária, carro de som e barco no interior; agentes de saúde em todo lugar.</p></div>
  {foot(11)}
</section>''')

# 12-14 Modelos de posts
def post(n, topo, meio, fim, linha, itens, rodape):
    lis = ''.join(f'<li>{x}</li>' for x in itens)
    return f'''<section class="p">
  <p class="hash" style="margin-top:20px"><b>#AMAPÁ</b><span>NO</span><b>COMBATE</b><span>À</span><b>MALÁRIA</b></p>
  <h2 class="H" style="text-align:center; margin-top:28px"><span class="lima" style="font-size:118px">{topo}</span><br><span class="ink" style="font-size:150px">{meio}</span><br><span class="lar" style="font-size:210px">{fim}</span></h2>
  <p style="text-align:center; font-size:27px; margin-top:20px">{linha}</p>
  <div class="box" style="margin-top:30px"><ul class="dot">{lis}</ul></div>
  <p class="H" style="text-align:center; font-size:46px; margin-top:34px; font-style:italic">{rodape}</p>
  <p style="position:absolute; left:0; right:0; bottom:60px; text-align:center; font-size:18px; color:var(--muted)">Modelo de post para campanha · {n:02d}</p>
</section>'''
pages.append(post(12, 'Trabalha no', 'garimpo ou', 'na roça?', 'O MOSQUITO DA MALÁRIA PICA <b>AO ENTARDECER E AO AMANHECER.</b>',
  ['Use <b>repelente</b> e roupa comprida nesses horários.', 'Durma sempre no <b>mosquiteiro</b>.', 'Teve <b>febre</b>? Faça o <b>teste rápido</b> no mesmo dia.'], 'Malária tem tratamento gratuito no SUS!'))
pages.append(post(13, 'Melhorou?', 'Não pare o', 'remédio!', 'A MALÁRIA VIVAX <b>VOLTA</b> SE O TRATAMENTO FICAR PELA METADE.',
  ['Tome <b>todas as doses</b>, no horário certo.', 'Volte ao <b>posto</b> no dia marcado.', 'Sentiu algo diferente? <b>Avise a equipe</b>.'], 'Tratamento completo protege você e sua família!'))
pages.append(post(14, 'Chegou a', 'época da', 'seca!', 'ENTRE <b>JUNHO E SETEMBRO</b> OS RIOS BAIXAM E O MOSQUITO SE ESPALHA.',
  ['Elimine <b>água parada</b> perto de casa.', 'Coloque <b>tela</b> nas janelas.', 'Receba o <b>agente de saúde</b>: ele leva o teste até você.'], 'Prevenir agora evita casos depois!'))

# 15 Fontes
pages.append(f'''<section class="p">{FB}
  <h2 class="H" style="font-size:100px; margin-top:20px"><span class="ink">Fontes</span></h2>
  <div class="box" style="margin-top:36px">
    <ul class="dot" style="gap:18px">
      <li style="font-size:21px">OLIVEIRA et al. "Malária no Amapá 2014–2024: análise epidemiológica dos casos notificados". Revista Núcleo do Conhecimento, ago/2025. Dados do SIVEP-Malária.</li>
      <li style="font-size:21px">Ministério da Saúde. "Amapá reduz 16,8% dos casos de malária no primeiro trimestre de 2025", abr/2025.</li>
      <li style="font-size:21px">Ministério da Saúde e Agência Gov. Malária no Brasil em 2025: menor número de casos em quase 50 anos.</li>
      <li style="font-size:21px">Nota Informativa nº 4/2025 CEMA/DEDT/SVSA/MS: migração de casos ligada ao garimpo.</li>
      <li style="font-size:21px">Prefeitura de Macapá, via A Gazeta do Amapá: redução de 82% nos casos entre 2024 e 2025.</li>
      <li style="font-size:21px">Governo do Amapá: plano estadual de eliminação da malária até 2035; municípios em emergência em 2022.</li>
      <li style="font-size:21px">Bandeira do Amapá: Wikimedia Commons.</li>
    </ul>
  </div>
  <div class="box" style="margin-top:22px"><p style="font-size:21px">Números de fontes diferentes usam períodos e métodos diferentes. Antes de publicar uma campanha, confira os dados mais recentes no SIVEP-Malária e na Superintendência de Vigilância em Saúde do Amapá.</p></div>
  {foot(15)}
</section>''')

# 16 Dedicatória
pages.append(f'''<section class="p" style="padding:0; background:#3F8A2E; background-image:none">
  <div style="position:absolute; left:0; right:0; top:0; height:300px">{FLAG}</div>
  <div style="position:absolute; left:96px; right:96px; top:420px; color:#fff">
    <p class="hash" style="text-align:left; color:#fff"><b>#AMAPÁ</b><span>NO</span><b>COMBATE</b><span>À</span><b>MALÁRIA</b></p>
    <p style="font-size:30px; margin-top:60px; font-weight:500">Pesquisa elaborada</p>
    <h2 class="H" style="font-size:150px; margin-top:14px; color:#fff">De Arthur Miguel</h2>
    <h2 class="H" style="font-size:150px; margin-top:6px; color:#E2F27A">para a ibradep</h2>
    <p style="font-size:26px; margin-top:44px; max-width:820px; line-height:1.5">Com o compromisso de levar informação, prevenção e cuidado a cada comunidade do Amapá.</p>
  </div>
  <p style="position:absolute; left:96px; bottom:70px; color:#fff; font-size:20px">Novembro de 2026</p>
</section>''')

html = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Malária no Amapá</title>' + CSS + '</head><body>' + ''.join(pages) + '</body></html>'
open('malaria-amapa.html', 'w').write(html)
print('ok', len(pages))
