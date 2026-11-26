# "Águas de Minas": como tratar a poluição das águas mineiras. Páginas 1080x1350.
CSS = '''
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,800;1,700&family=IBM+Plex+Mono:wght@500&display=swap">
<style>
/* Água limpa contra água suja: fundo claro azulado, azul-profundo como tinta, turquesa como esperança, ocre-lama como alerta. */
:root{
  --paper:#F5F9FA; --grid:rgba(10,50,70,.05); --ink:#0B2A3A; --muted:#4F6672; --line:rgba(11,42,58,.13);
  --azul:#0B5E8E; --azul-bg:#DCEEF6; --turq:#17A3A0; --turq-bg:#D7F1EF; --lama:#B5652A; --lama-bg:#F6E3D3; --verm:#C0392B; --card:#FFFFFF;
  --fh:"Anton", "Impact", "Arial Narrow", sans-serif; --fb:"Poppins", "Segoe UI", Arial, sans-serif; --fm:"IBM Plex Mono", monospace;
}
@page{ size:1080px 1350px; margin:0 }
*{box-sizing:border-box; margin:0; padding:0}
body{font-family:var(--fb); color:var(--ink); -webkit-print-color-adjust:exact; print-color-adjust:exact; background:var(--paper)}
.p{width:1080px; height:1350px; position:relative; overflow:hidden; page-break-after:always; break-after:page;
   background-color:var(--paper);
   background-image:linear-gradient(var(--grid) 1px, transparent 1px), linear-gradient(90deg, var(--grid) 1px, transparent 1px);
   background-size:36px 36px; padding:110px 90px 0}
.p:last-child{page-break-after:auto}
.H{font-family:var(--fh); font-weight:400; text-transform:uppercase}
.H > span{display:block; line-height:1.0}
.azul{color:var(--azul)} .turq{color:var(--turq)} .lama{color:var(--lama)} .ink{color:var(--ink)}
p{font-size:22px; line-height:1.48}
.card{background:var(--card); border-radius:18px; padding:26px 30px; box-shadow:0 1px 0 rgba(11,42,58,.06), 0 12px 30px -20px rgba(11,42,58,.45); border:1px solid rgba(11,42,58,.06)}
.dark{background:var(--ink); color:#fff; border:0}
.num{font-family:var(--fh); font-weight:400; line-height:.95; font-variant-numeric:tabular-nums}
.small{font-size:17px; color:var(--muted); line-height:1.4}
.eyebrow{font-family:var(--fm); font-size:17px; letter-spacing:.12em; text-transform:uppercase; color:var(--turq)}
.top{position:absolute; left:90px; right:90px; top:44px; display:flex; justify-content:space-between; font-size:17px; color:var(--muted)}
.top b{color:var(--ink); font-weight:800}
.wave{position:absolute; left:0; right:0; bottom:0; height:70px}
.foot{position:absolute; left:90px; right:90px; bottom:40px; display:flex; justify-content:space-between; font-size:15px; color:var(--muted); z-index:2}
ul.dot{list-style:none; display:grid; gap:11px}
ul.dot li{position:relative; padding-left:30px; font-size:21px; line-height:1.42}
ul.dot li::before{content:""; position:absolute; left:2px; top:.42em; width:13px; height:13px; border-radius:50% 0 50% 50%; transform:rotate(-45deg); background:var(--turq)}
table{border-collapse:collapse; width:100%; font-size:18px}
th{font-family:var(--fm); font-weight:500; font-size:14px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); text-align:left; padding:10px; border-bottom:2px solid var(--ink)}
td{padding:9px 10px; border-bottom:1px solid var(--line); vertical-align:top}
.pill{display:inline-block; font-weight:700; font-size:15px; padding:5px 12px; border-radius:999px}
.ico{width:64px; height:64px; border-radius:16px; display:grid; place-items:center}
</style>'''

WAVE = '<svg class="wave" viewBox="0 0 1080 70" preserveAspectRatio="none"><path d="M0 30 C 180 5, 360 55, 540 30 S 900 5, 1080 30 L1080 70 L0 70 Z" fill="#DCEEF6"/><path d="M0 46 C 200 26, 380 66, 560 46 S 900 26, 1080 46 L1080 70 L0 70 Z" fill="#BFE1EE"/></svg>'
N = [0]
def pg(inner, secao, fonte=''):
    N[0] += 1
    return (f'<section class="p"><div class="top"><span><b>Águas de Minas</b> · como tratar a poluição</span><span>{secao}</span></div>'
            f'{inner}{WAVE}<div class="foot"><span>{fonte}</span><span>{N[0]:02d}</span></div></section>')
def head(eye, l1, l2, c1='ink', c2='azul', size=92):
    return f'<p class="eyebrow">{eye}</p><h2 class="H" style="font-size:{size}px; margin-top:14px"><span class="{c1}">{l1}</span><span class="{c2}">{l2}</span></h2>'
# ícone de gota
def gota(cor, bg):
    return f'<div class="ico" style="background:{bg}"><svg viewBox="0 0 24 24" width="34" height="34"><path d="M12 2 C 12 2, 5 10, 5 15 a7 7 0 0 0 14 0 C 19 10, 12 2, 12 2 Z" fill="{cor}"/></svg></div>'

P = []

# 1 CAPA
N[0] += 1
P.append('''<section class="p" style="padding:0; background:#0B2A3A; background-image:none">
  <svg viewBox="0 0 1080 1350" style="position:absolute; inset:0" aria-hidden="true">
    <defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0B2A3A"/><stop offset="1" stop-color="#0B5E8E"/></linearGradient></defs>
    <rect width="1080" height="1350" fill="url(#g)"/>
    <path d="M0 860 C 200 800, 380 920, 560 860 S 900 780, 1080 850 L1080 1350 L0 1350 Z" fill="#B5652A" opacity=".9"/>
    <path d="M0 930 C 220 880, 420 990, 620 930 S 920 870, 1080 920 L1080 1350 L0 1350 Z" fill="#8B7A4E" opacity=".9"/>
    <path d="M0 1010 C 240 960, 440 1060, 660 1005 S 940 950, 1080 995 L1080 1350 L0 1350 Z" fill="#17A3A0"/>
    <path d="M0 1090 C 260 1040, 460 1130, 700 1080 S 960 1030, 1080 1070 L1080 1350 L0 1350 Z" fill="#5CC8D8"/>
    <path d="M0 1170 C 260 1130, 480 1210, 720 1165 S 960 1120, 1080 1150 L1080 1350 L0 1350 Z" fill="#DCEEF6"/>
  </svg>
  <p class="eyebrow" style="position:absolute; left:90px; top:110px; color:#5CC8D8">Pesquisa · Minas Gerais · novembro de 2026</p>
  <h1 class="H" style="position:absolute; left:90px; top:160px; font-size:150px; color:#fff"><span>Águas</span><span style="color:#5CC8D8">de Minas</span></h1>
  <p style="position:absolute; left:94px; top:500px; width:760px; font-size:30px; line-height:1.4; color:#DCEEF6">Como tratar a poluição dos rios mineiros: causas, rios críticos, soluções que funcionam e um plano até 2033.</p>
  <p style="position:absolute; left:94px; top:690px; font-size:20px; color:#9FC6D6">Da lama ao rio limpo</p>
</section>''')

# 2 PANORAMA
iqa = [('Excelente',1.4,'#17A3A0'),('Bom',37.4,'#5CC8D8'),('Médio',44.1,'#E7C35A'),('Ruim',17.0,'#B5652A'),('Muito ruim',0.1,'#C0392B')]
bar = ''.join(f'<span style="width:{max(v,0.6)}%; background:{c}; display:block; height:100%; border-right:3px solid #fff"></span>' for n,v,c in iqa)
leg = ''.join(f'<div style="display:grid; grid-template-columns:18px 1fr auto; gap:12px; align-items:center; font-size:20px; padding:7px 0; border-bottom:1px solid var(--line)"><span style="width:16px; height:16px; border-radius:4px; background:{c}"></span><span>{n}</span><b>{str(v).replace(".",",")}%</b></div>' for n,v,c in iqa)
P.append(pg(f'''{head('Panorama','Como estão','os rios mineiros')}
  <div class="card" style="margin-top:30px">
    <p class="eyebrow" style="color:var(--muted)">Índice de Qualidade da Água · pontos monitorados pelo IGAM em 2023</p>
    <div style="display:flex; height:54px; border-radius:12px; overflow:hidden; margin-top:16px">{bar}</div>
    <div style="margin-top:14px">{leg}</div>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px">
    <div class="card"><p class="num lama" style="font-size:70px">54%</p><p style="font-size:19px; margin-top:6px">das amostras de rios fora do limite legal em 2020, por esgoto doméstico e industrial</p></div>
    <div class="card"><p class="num azul" style="font-size:70px">53,7%</p><p style="font-size:19px; margin-top:6px">da população com esgoto tratado em 2021, embora a coleta chegue a 87,6%</p></div>
  </div>
  <div class="card dark" style="margin-top:16px"><p style="font-size:21px"><b style="color:#5CC8D8">A conta não fecha:</b> muito esgoto é coletado, mas uma parte grande vai para o rio sem tratamento. É a principal causa de água ruim em Minas, segundo o IGAM.</p></div>''',
  'Panorama', 'IGAM (monitoramento 2023 e 2020); Governo de Minas/SNIS (2021)'))

# 3 FONTES DE POLUIÇÃO
fontes = [('Esgoto doméstico','A maior causa. Coliformes, matéria orgânica e nutrientes que tiram o oxigênio da água.','#C0392B','#F7DDD9'),
          ('Mineração','Rejeitos, sedimentos e metais. Barragens de rejeito são o maior risco de desastre.','#B5652A','#F6E3D3'),
          ('Agropecuária','Agrotóxicos, adubo e esterco levados pela chuva; pasto sem mata ciliar causa erosão.','#8B7A4E','#EFE9D9'),
          ('Indústria','Siderurgia, alimentos, curtumes e química. Efluente fora do padrão ou sem fiscalização.','#0B5E8E','#DCEEF6'),
          ('Lixo e drenagem urbana','Lixões, entulho e a primeira chuva que lava ruas e leva tudo ao córrego.','#4F6672','#E3E9EC'),
          ('Erosão e assoreamento','Solo exposto vira lama no rio, o rio fica raso e esquenta.','#17A3A0','#D7F1EF')]
fc = ''.join(f'<div class="card" style="display:grid; grid-template-columns:64px 1fr; gap:18px; padding:22px 26px">{gota(c,b)}<div><p class="H" style="font-size:32px">{t}</p><p style="font-size:18.5px; margin-top:4px; color:var(--muted)">{d}</p></div></div>' for t,d,c,b in fontes)
P.append(pg(f'''{head('Diagnóstico','De onde vem','a poluição','ink','lama')}
  <div style="display:grid; gap:13px; margin-top:30px">{fc}</div>''', 'Causas', 'IGAM; SEMAD'))

# 4 RIOS CRÍTICOS
rios = [('Rio das Velhas','Grande BH','Esgoto dos ribeirões Arrudas e Onça. É o principal manancial da região metropolitana e está melhorando aos poucos.'),
        ('Rio Paraopeba','Brumadinho, Betim, Ibirité','Rejeito da barragem de 2019 e esgoto urbano. O ribeirão Ibirité teve um dos piores resultados de 2023.'),
        ('Rio Doce','Mariana até o mar','Lama da barragem de Fundão em 2015, que percorreu cerca de 660 km até o Espírito Santo.'),
        ('Rio Piracicaba','Vale do Aço','Siderurgia, mineração e esgoto das cidades industriais.'),
        ('Bacias do Leste','Itapemirim e Itaúnas','Piores médias de IQA em 2023; o ribeirão São Pedro, em Medina, teve um dos piores pontos.')]
rt = ''.join(f'<tr><td style="width:250px"><b style="font-size:20px">{a}</b><br><span style="color:var(--muted); font-size:16px">{b}</span></td><td>{c}</td></tr>' for a,b,c in rios)
P.append(pg(f'''{head('Onde dói mais','Rios','críticos','ink','lama')}
  <div class="card" style="margin-top:30px; padding:16px 24px"><table><thead><tr><th>Rio</th><th>Por que é crítico</th></tr></thead><tbody>{rt}</tbody></table></div>
  <div class="card" style="margin-top:16px; background:var(--turq-bg); border:0"><p style="font-size:20px"><b class="turq">Notícia boa:</b> o IGAM registra recuperação progressiva no rio das Velhas e melhora na bacia do São Francisco. Tratar esgoto dá resultado.</p></div>''',
  'Rios críticos', 'IGAM; Governo de Minas'))

# 5 DESASTRES
P.append(pg(f'''{head('Lições','Mariana e','Brumadinho','ink','lama')}
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:30px">
    <div class="card" style="border-top:8px solid var(--lama)"><p class="eyebrow" style="color:var(--lama)">5 de novembro de 2015</p><p class="H" style="font-size:44px; margin-top:8px">Mariana</p>
      <ul class="dot" style="margin-top:12px"><li>Barragem de Fundão (Samarco, Vale e BHP)</li><li>19 mortes</li><li>Lama no rio Doce até o mar</li></ul>
      <p class="num lama" style="font-size:56px; margin-top:18px">R$ 170 bi</p><p style="font-size:18px">novo acordo de reparação, assinado em outubro de 2024, a ser pago ao longo de 20 anos</p></div>
    <div class="card" style="border-top:8px solid var(--verm)"><p class="eyebrow" style="color:var(--verm)">25 de janeiro de 2019</p><p class="H" style="font-size:44px; margin-top:8px">Brumadinho</p>
      <ul class="dot" style="margin-top:12px"><li>Barragem da mina Córrego do Feijão (Vale)</li><li>270 mortes</li><li>Rejeito no rio Paraopeba</li></ul>
      <p class="num" style="font-size:56px; margin-top:18px; color:var(--verm)">R$ 37,7 bi</p><p style="font-size:18px">acordo de reparação assinado em 2021</p></div>
  </div>
  <div class="card dark" style="margin-top:16px"><p style="font-size:21px"><b style="color:#5CC8D8">O que mudou:</b> a lei estadual "Mar de Lama Nunca Mais" (Lei 23.291/2019) proibiu novas barragens alteadas a montante e obrigou a desmontar as existentes.</p></div>''',
  'Desastres', 'Governo de Minas; Agência Minas; Planalto'))

# 6 TRATAR ESGOTO
tec = [('Grandes cidades','Rede coletora completa e estação com tratamento avançado que também remove nitrogênio e fósforo.'),
       ('Cidades médias','Reatores anaeróbios com pós-tratamento: baratos de operar e muito usados em Minas.'),
       ('Cidades pequenas','Lagoas de estabilização e jardins filtrantes (wetlands), que usam plantas para limpar a água.'),
       ('Zona rural','Fossa séptica biodigestora da Embrapa: trata o esgoto da casa e gera adubo.'),
       ('Ligações erradas','Programa "caça-esgoto": achar casas ligadas na rede de chuva e corrigir.')]
tt = ''.join(f'<div class="card" style="padding:20px 26px; display:grid; grid-template-columns:230px 1fr; gap:20px"><p class="H azul" style="font-size:30px">{a}</p><p style="font-size:19px">{b}</p></div>' for a,b in tec)
P.append(pg(f'''{head('Solução 1 · a mais importante','Tratar','o esgoto','ink','turq')}
  <div style="display:grid; gap:12px; margin-top:28px">{tt}</div>
  <div class="card" style="margin-top:14px; background:var(--azul-bg); border:0"><p style="font-size:20px"><b class="azul">Meta da lei:</b> o Marco do Saneamento (Lei 14.026/2020) exige 99% da população com água e 90% com coleta e tratamento de esgoto até 2033.</p></div>''',
  'Esgoto', 'Lei 14.026/2020; IGAM; Embrapa'))

# 7 MINERAÇÃO
mn = [('Desmontar barragens a montante','Cumprir a lei estadual com prazo, fiscalização e transparência.'),
      ('Empilhamento a seco','Filtrar o rejeito e empilhar, sem barragem de lama.'),
      ('Rejeito vira produto','Areia, blocos, tijolos e pigmentos feitos do rejeito.'),
      ('Monitoramento 24 horas','Sensores, radar por satélite e sirenes testadas nas comunidades.'),
      ('Recuperar o rio','Retirar sedimento, replantar margens e monitorar metais na água e nos peixes.')]
mt = ''.join(f'<div class="card" style="padding:20px 26px; display:grid; grid-template-columns:44px 1fr; gap:16px"><p class="num lama" style="font-size:44px">{i+1}</p><div><p class="H" style="font-size:29px">{a}</p><p style="font-size:18.5px; color:var(--muted); margin-top:3px">{b}</p></div></div>' for i,(a,b) in enumerate(mn))
P.append(pg(f'''{head('Solução 2','Mineração','mais segura','ink','lama')}
  <div style="display:grid; gap:12px; margin-top:28px">{mt}</div>''', 'Mineração', 'Lei estadual 23.291/2019; ANM'))

# 8 CAMPO E CIDADE
P.append(pg(f'''{head('Soluções 3 e 4','No campo','e na cidade','ink','turq')}
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:30px">
    <div class="card"><p class="H turq" style="font-size:38px">No campo</p>
      <ul class="dot" style="margin-top:14px"><li><b>Mata ciliar</b> nas margens e nascentes, como manda o Código Florestal.</li><li><b>Plantio direto</b> e curvas de nível contra a erosão.</li><li>Uso correto de <b>agrotóxicos</b> e devolução das embalagens.</li><li><b>Pagamento ao produtor</b> que protege a água (programas como o Produtor de Água, da ANA).</li><li>Esterco de pocilgas e currais em <b>biodigestor</b>.</li></ul></div>
    <div class="card"><p class="H azul" style="font-size:38px">Na cidade</p>
      <ul class="dot" style="margin-top:14px"><li><b>Fim dos lixões</b> e coleta seletiva.</li><li><b>Parques lineares</b> que devolvem espaço ao córrego.</li><li>Calçadas e jardins que <b>absorvem a chuva</b>.</li><li>Fiscalização do <b>efluente industrial</b>.</li><li>Ponto de coleta de <b>óleo de cozinha</b>.</li></ul></div>
  </div>
  <div class="card dark" style="margin-top:16px"><p style="font-size:21px"><b style="color:#5CC8D8">Por que importa:</b> mata ciliar e solo coberto reduzem a lama no rio, e a água chega mais limpa à estação de tratamento.</p></div>''',
  'Campo e cidade', 'Código Florestal; ANA'))

# 9 TECNOLOGIA
P.append(pg(f'''{head('Solução 5','Tecnologia para','vigiar a água','ink','azul')}
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:28px">
    <div class="card"><p class="H azul" style="font-size:30px">Sensores no rio</p><p style="font-size:18.5px; margin-top:6px; color:var(--muted)">Oxigênio, turbidez, pH e temperatura medidos a cada 15 minutos, com alerta automático.</p></div>
    <div class="card"><p class="H azul" style="font-size:30px">Satélite</p><p style="font-size:18.5px; margin-top:6px; color:var(--muted)">Imagens gratuitas do Sentinel-2 mostram mancha de lama, turbidez e algas nos reservatórios.</p></div>
    <div class="card"><p class="H azul" style="font-size:30px">Denúncia pelo celular</p><p style="font-size:18.5px; margin-top:6px; color:var(--muted)">Foto e localização de esgoto, lixo ou peixe morto, direto para o órgão responsável.</p></div>
    <div class="card"><p class="H azul" style="font-size:30px">Painel aberto</p><p style="font-size:18.5px; margin-top:6px; color:var(--muted)">A população vê a qualidade do rio da sua cidade, como já faz o IGAM nos relatórios anuais.</p></div>
  </div>
  <div class="card dark" style="margin-top:16px">
    <p class="eyebrow" style="color:#5CC8D8">Ideia de startup</p>
    <p class="H" style="font-size:44px; margin-top:8px">Sistema Águas de Minas</p>
    <p style="font-size:20px; margin-top:8px">Junta sensores, satélite e denúncias num só mapa, como o Foco Amazônia faz com o fogo. Compradores: prefeituras, Copasa e serviços municipais, comitês de bacia, mineradoras e indústrias que precisam provar que não poluem.</p>
  </div>''', 'Tecnologia', 'Copernicus; IGAM'))

# 10 QUEM FAZ O QUÊ
quem = [('Governo do Estado','IGAM monitora, FEAM e SEMAD licenciam e fiscalizam, e o Estado financia saneamento.'),
        ('Prefeituras','Plano municipal de saneamento, contrato com a empresa de água e esgoto e fim dos lixões.'),
        ('Copasa e serviços municipais','Obras de rede e estações de tratamento.'),
        ('Comitês de bacia','Planejam a bacia e aplicam o dinheiro da cobrança pelo uso da água.'),
        ('Empresas','Tratar efluentes, desmontar barragens e recuperar áreas.'),
        ('Ministério Público','Cobra na Justiça quem polui e acompanha os acordos.'),
        ('Cidadão','Ligar o esgoto certo, não jogar lixo nem óleo, denunciar.')]
qt = ''.join(f'<tr><td style="width:300px"><b>{a}</b></td><td>{b}</td></tr>' for a,b in quem)
P.append(pg(f'''{head('Responsabilidades','Quem faz','o quê')}
  <div class="card" style="margin-top:30px; padding:16px 24px"><table style="font-size:19px"><thead><tr><th>Quem</th><th>Papel</th></tr></thead><tbody>{qt}</tbody></table></div>''', 'Papéis'))

# 11 PLANO ATÉ 2033
fases = [('2027','Diagnóstico e projetos','Mapa de todas as ligações de esgoto, lixões e pontos críticos. Projetos das estações que faltam.','#0B5E8E'),
         ('2028–2030','Obras prioritárias','Estações nas bacias do Velhas, Paraopeba, Doce e Piracicaba; fim dos lixões restantes.','#17A3A0'),
         ('2030–2032','Tratamento avançado','Remoção de nutrientes nas grandes estações; saneamento rural com biodigestores.','#5CC8D8'),
         ('2033','Meta da lei','90% de esgoto coletado e tratado; rios monitorados em tempo real.','#0B2A3A')]
ft = ''.join(f'<div style="display:grid; grid-template-columns:200px 1fr; gap:20px; align-items:stretch"><div style="background:{c}; color:#fff; border-radius:14px; display:grid; place-items:center; padding:16px"><p class="H" style="font-size:38px; text-align:center">{a}</p></div><div class="card" style="padding:20px 26px"><p class="H" style="font-size:30px">{b}</p><p style="font-size:19px; color:var(--muted); margin-top:4px">{d}</p></div></div>' for a,b,d,c in fases)
P.append(pg(f'''{head('Caminho','Plano até','2033','ink','turq')}
  <div style="display:grid; gap:16px; margin-top:30px">{ft}</div>
  <div class="card" style="margin-top:18px; background:var(--turq-bg); border:0"><p style="font-size:20px"><b class="turq">Dinheiro já existe em parte:</b> os acordos de Mariana e Brumadinho, a cobrança pelo uso da água e os contratos de saneamento podem financiar boa parte das obras.</p></div>''',
  'Plano', 'Lei 14.026/2020'))

# 12 CADA UM
P.append(pg(f'''{head('Você também trata a água','O que cada','pessoa pode fazer','ink','azul')}
  <div class="card" style="margin-top:30px">
    <ul class="dot" style="gap:16px">
      <li style="font-size:23px">Confira se o esgoto da sua casa vai para a <b>rede de esgoto</b>, e não para a de chuva.</li>
      <li style="font-size:23px">Guarde o <b>óleo de cozinha</b> em garrafa e leve a um ponto de coleta.</li>
      <li style="font-size:23px">Não jogue <b>lixo nem entulho</b> em córregos e terrenos.</li>
      <li style="font-size:23px">Na roça, <b>proteja a nascente</b> com cerca e mata.</li>
      <li style="font-size:23px"><b>Denuncie</b> esgoto a céu aberto, lixão ou peixe morto à prefeitura ou ao órgão ambiental.</li>
      <li style="font-size:23px">Participe do <b>comitê da sua bacia</b>: as reuniões são abertas.</li>
    </ul>
  </div>
  <p class="H" style="font-size:58px; margin-top:34px; line-height:1.05; text-align:center"><span class="ink">Rio limpo começa</span><span class="turq">na nossa casa</span></p>''', 'Cidadão'))

# 13 FONTES
P.append(pg(f'''{head('Referências','Fontes','e dados','ink','azul', 80)}
  <div class="card" style="margin-top:30px">
    <ul class="dot" style="gap:15px">
      <li style="font-size:19px">IGAM: "Qualidade das águas do Estado mantém estabilidade" (monitoramento de 2023) e notícias sobre o rio das Velhas e a bacia do São Francisco.</li>
      <li style="font-size:19px">Estado de Minas (jan/2021): esgoto contamina mais da metade das amostras de rios de Minas Gerais.</li>
      <li style="font-size:19px">Governo de Minas / Agência Minas: coleta e tratamento de esgoto em 2021 (dados do SNIS).</li>
      <li style="font-size:19px">Agência Minas e Planalto: novo acordo de Mariana, R$ 170 bilhões (out/2024).</li>
      <li style="font-size:19px">Acordo de Brumadinho (2021) e Lei estadual 23.291/2019 ("Mar de Lama Nunca Mais").</li>
      <li style="font-size:19px">Lei federal 14.026/2020 (Marco Legal do Saneamento) e Código Florestal (Lei 12.651/2012).</li>
      <li style="font-size:19px">Embrapa (fossa séptica biodigestora), ANA (Programa Produtor de Água), Copernicus (Sentinel-2).</li>
    </ul>
  </div>
  <div class="card" style="margin-top:16px"><p style="font-size:19px">O SNIS foi substituído pelo SINISA em 2024, e o dado estadual mais recente de esgoto tratado que encontrei é de 2021. Confira os números atualizados no Panorama da SEMAD e no painel do IGAM antes de publicar.</p></div>''', 'Fontes'))

html = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Águas de Minas</title>' + CSS + '</head><body>' + ''.join(P) + '</body></html>'
open('aguas-de-minas.html','w').write(html)
print('ok', len(P))
