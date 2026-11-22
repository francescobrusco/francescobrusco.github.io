# Genera le pagine del sito personale in italiano e in inglese.
# Uso, dalla cartella del repository:  python strumenti/genera.py
# Pagine prodotte: index.html, libri/index.html, en/index.html, en/books/index.html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DISCO = (ROOT / 'strumenti' / 'disco.svg').read_text(encoding='utf-8')
RICERCA = 'https://francescobrusco.github.io/produzione_discografica_italiana_1965_1999/'

# ---------- libri (dal più recente) ----------
LIBRI = [
    dict(isbn13='9788892774834', isbn='8892774832', slug='altro-libro-sui-beatles-eredita-libro-francesco-brusco',
         titolo='Un altro libro sui Beatles', sottotitolo='Eredità culturali tra Penny Lane e il metaverso',
         editore='Arcana', it='Roma 2026', en='Rome 2026'),
    dict(isbn13='9788816417496', isbn='9788816417496', slug='voce-del-padrone-suoni-racconti-libro-francesco-brusco',
         titolo='La voce del padrone', sottotitolo='Suoni e racconti dagli studi di registrazione',
         editore='Jaca Book', it='Milano 2022', en='Milan 2022'),
    dict(isbn13='9788857574172', isbn='9788857574172', slug='guccini-frammenti-di-discorso-musicale-ebook-francesco-brusco',
         titolo='Guccini', sottotitolo='Frammenti di un discorso musicale',
         editore='Mimesis', it='Milano-Udine 2020', en='Milan-Udine 2020'),
    dict(isbn13='9788862317078', isbn='9788862317078', slug='faber-nella-bottega-di-de-ebook-francesco-brusco',
         titolo='Faber nella bottega di De André',
         sottotitolo='Musica, musicisti e produzione collettiva nell’opera del più grande cantautore italiano',
         editore='Arcana', it='Roma 2019', en='Rome 2019'),
    dict(isbn13='9788862315395', isbn='9788862315395', slug='revolution-68-dei-beatles-libro-francesco-brusco',
         titolo='Revolution', sottotitolo='Il ’68 dei Beatles', editore='Arcana', it='Roma 2018', en='Rome 2018'),
    dict(isbn13='9788862314961', isbn='9788862314961', slug='estetica-di-sgt-pepper-genesi-libro-francesco-brusco',
         titolo='Estetica di Sgt. Pepper', sottotitolo='Genesi, linguaggi e ricezione del capolavoro dei Beatles',
         editore='Arcana', it='Roma 2017', en='Rome 2017'),
]
def url(b): return f"https://www.lafeltrinelli.it/{b['slug']}/e/{b['isbn13']}"

# ---------- testi ----------
T = {
 'it': dict(
   lang='it', home='/', libri='/libri/', other_home='/en/', other_libri='/en/books/',
   switch=('<span aria-current="true" title="Italiano">ITA</span>', '<a href="{o}" hreflang="en" lang="en" title="English">ENG</a>'),
   desc='Francesco Brusco insegna Musiche Popolari Contemporanee e Sound Design all’Università di Salerno. Ricerca, libri, giornalismo musicale e musica.',
   nav=[('#ricerca', 'Ricerca'), ('{libri}', 'Libri'), ('#attivita', 'Attività'), (RICERCA, 'La produzione discografica in Italia')],
   cv=['Docente di Musiche Popolari Contemporanee e Sound Design',
       'Università di Salerno, Dipartimento di Scienze del Patrimonio Culturale (Dispac)',
       'PhD in Scienze del Testo Letterario e Musicale, Università di Pavia',
       'Visiting Postgraduate Researcher, Institute of Popular Music, University of Liverpool',
       'Giornalista musicale, <i>Il Manifesto</i> e <i>il Giornale della Musica</i>'],
   unisa='Università di Salerno', photo_alt='Francesco Brusco legge durante un incontro pubblico',
   h_ricerca='Ricerca', ricerca_url=RICERCA,
   ricerca_t='La produzione discografica in Italia come pratica sociale <span class="yr">(1965–1999)</span>',
   ricerca_p='La rete di studi di registrazione, musicisti, produttori, tecnici del suono ed etichette dietro i venti album più venduti di ogni anno. Grafi, una mappa animata degli studi, le interviste e il dataset completo della tesi di dottorato.',
   stats=[('700', 'album'), ('3410', 'nodi'), ('7926', 'collegamenti')], go='Esplora il progetto',
   topics_label='Temi di ricerca',
   topics=['Popular music italiana', 'Record production e studi di registrazione', 'Canzone d’autore', 'Beatles',
           'Social network analysis', 'Mappatura culturale e GIS', 'Digital humanities', 'Intelligenza artificiale e musica'],
   h_libri='Libri', ultimo='Ultimo libro', tutti='Tutti i libri ({n})', luogo='it',
   h_att='Attività',
   att=[('Didattica', '<p>Insegna Musiche Popolari Contemporanee e Sound Design all’Università di Salerno e tiene laboratori e workshop su digital humanities, network analysis e mappatura delle scene musicali.</p>'),
        ('Giornalismo', '<p>Scrive di musica per <i>Il Manifesto</i> e <i>il Giornale della Musica</i>.</p><ul><li><a href="https://ilmanifesto.it/autori/francesco-brusco" target="_blank" rel="noopener">Articoli su il manifesto</a></li></ul>'),
        ('Musica', '<p>Come musicista ha all’attivo due album con i Là Nua.</p>')],
   libri_title='Libri', libri_lede='Monografie dedicate principalmente ai Beatles, alla canzone d’autore italiana e agli studi di registrazione. Ogni titolo porta alla scheda su laFeltrinelli.',
   back='← Torna alla home', felt='Scheda su laFeltrinelli', alt_cover='Copertina di',
 ),
 'en': dict(
   lang='en', home='/en/', libri='/en/books/', other_home='/', other_libri='/libri/',
   switch=('<a href="{o}" hreflang="it" lang="it" title="Italiano">ITA</a>', '<span aria-current="true" title="English">ENG</span>'),
   desc='Francesco Brusco teaches Contemporary Popular Music and Sound Design at the University of Salerno. Research, books, music journalism and music.',
   nav=[('#ricerca', 'Research'), ('{libri}', 'Books'), ('#attivita', 'Activities'), (RICERCA + 'en/', 'Record production in Italy')],
   cv=['Lecturer in Contemporary Popular Music and Sound Design',
       'University of Salerno, Department of Cultural Heritage Sciences (Dispac)',
       'PhD in Literary and Musical Text Studies, University of Pavia',
       'Visiting Postgraduate Researcher, Institute of Popular Music, University of Liverpool',
       'Music journalist, <i>Il Manifesto</i> and <i>il Giornale della Musica</i>'],
   unisa='University of Salerno', photo_alt='Francesco Brusco reading at a public event',
   h_ricerca='Research', ricerca_url=RICERCA + 'en/',
   ricerca_t='Record production in Italy as social practice <span class="yr">(1965–1999)</span>',
   ricerca_p='The network of recording studios, musicians, producers, sound engineers and labels behind the twenty best-selling albums of each year. Graphs, an animated map of the studios, interviews and the full dataset of the PhD thesis.',
   stats=[('700', 'albums'), ('3410', 'nodes'), ('7926', 'edges')], go='Explore the project',
   topics_label='Research topics',
   topics=['Italian popular music', 'Record production and recording studios', 'Italian singer-songwriters', 'The Beatles',
           'Social network analysis', 'Cultural mapping and GIS', 'Digital humanities', 'Artificial intelligence and music'],
   h_libri='Books', ultimo='Latest book', tutti='All books ({n})', luogo='en',
   h_att='Activities',
   att=[('Teaching', '<p>He teaches Contemporary Popular Music and Sound Design at the University of Salerno and leads workshops on digital humanities, network analysis and the mapping of music scenes.</p>'),
        ('Journalism', '<p>He writes about music for <i>Il Manifesto</i> and <i>il Giornale della Musica</i>.</p><ul><li><a href="https://ilmanifesto.it/autori/francesco-brusco" target="_blank" rel="noopener">Articles in il manifesto</a></li></ul>'),
        ('Music', '<p>As a musician he has released two albums with Là Nua.</p>')],
   libri_title='Books', libri_lede='Monographs devoted mainly to the Beatles, Italian singer-songwriters and recording studios, all published in Italian. Each title links to its page on laFeltrinelli.',
   back='← Back to home', felt='laFeltrinelli page', alt_cover='Cover of',
 ),
}

PROFILI = [('https://docenti.unisa.it/023922/home', None), ('https://unisa.academia.edu/FrancescoBrusco', 'Academia'),
           ('https://www.researchgate.net/profile/Francesco-Brusco?ev=hdr_xprf', 'ResearchGate'),
           ('https://ilmanifesto.it/autori/francesco-brusco', 'il manifesto'), ('https://github.com/francescobrusco', 'GitHub')]

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,400..900,0..100,0..1;1,9..144,400..900,0..100,0..1&family=EB+Garamond:ital,wght@0,400..700;1,400..700&family=Instrument+Sans:ital,wdth,wght@0,75..100,400..700;1,75..100,400..700&display=swap" rel="stylesheet">'

def head(t, title, alt_it, alt_en):
    return f'''<!DOCTYPE html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{t['desc']}">
<meta property="og:title" content="{title}">
<meta property="og:image" content="https://francescobrusco.github.io/img/francesco-brusco.jpg">
<link rel="alternate" hreflang="it" href="https://francescobrusco.github.io{alt_it}">
<link rel="alternate" hreflang="en" href="https://francescobrusco.github.io{alt_en}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{FONTS}
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
'''

def nav(t, other, home_page):
    items = ''
    for href, label in t['nav']:
        href = href.replace('{libri}', t['libri'])
        if href.startswith('#') and not home_page:
            href = t['home'] + href
        items += f'    <li><a href="{href}">{label}</a></li>\n'
    a, b = t['switch']
    sw = (a + b).replace('{o}', other)
    return f'''<nav class="top"><div class="wrap">
  <a class="brand" href="{t['home']}">Francesco Brusco</a>
  <ul>
{items}  </ul>
  <div class="lang">{sw}</div>
</div></nav>
'''

FOOT = '''<footer><div class="wrap">
  <span>© 2026 Francesco Brusco</span>
  <span><a href="https://github.com/francescobrusco">GitHub</a></span>
</div></footer>
'''
GROOVES = '''<script>
(function(){var g=document.getElementById('grooves');if(!g)return;for(var r=92;r<196;r+=2.6){var c=document.createElementNS('http://www.w3.org/2000/svg','circle');c.setAttribute('cx',200);c.setAttribute('cy',200);c.setAttribute('r',r.toFixed(1));c.setAttribute('stroke-width',(Math.round(r)%7===0)?1.2:.45);g.appendChild(c)}})();
</script>
'''

def home(t):
    cv = '\n'.join(f'      <li>{x}</li>' for x in t['cv'])
    prof = '\n'.join(f'      <li><a href="{u}" target="_blank" rel="noopener">{l or t["unisa"]}</a></li>' for u, l in PROFILI)
    stats = ''.join(f'<span><b>{n}</b>{l}</span>' for n, l in t['stats'])
    topics = ''.join(f'<li>{x}</li>' for x in t['topics'])
    b = LIBRI[0]
    att = '\n'.join(f'    <div>\n      <h3>{h}</h3>\n      {c}\n    </div>' for h, c in t['att'])
    return head(t, 'Francesco Brusco', '/', '/en/') + nav(t, t['other_home'], True) + f'''
<header class="intro"><div class="wrap intro-grid">
  <div>
    <h1>Francesco Brusco</h1>
    <ul class="cv">
{cv}
    </ul>
    <ul class="profiles">
{prof}
    </ul>
  </div>
  <figure style="margin:0"><img src="/img/francesco-brusco.jpg" alt="{t['photo_alt']}" width="1000" height="877"></figure>
</div></header>

<section id="ricerca"><div class="wrap">
  <h2>{t['h_ricerca']}</h2>
  <a class="feature" href="{t['ricerca_url']}">
    <div class="feat-art" aria-hidden="true"><div class="sl"></div>
    {DISCO}
    </div>
    <div class="feat-body">
      <h3>{t['ricerca_t']}</h3>
      <p>{t['ricerca_p']}</p>
      <div class="feat-stats">{stats}</div>
      <span class="feat-go">{t['go']}</span>
    </div>
  </a>
  <ul class="topics" aria-label="{t['topics_label']}">
    {topics}
  </ul>
</div></section>

<section id="libri" class="alt"><div class="wrap">
  <h2>{t['h_libri']}</h2>
  <a class="book-teaser" href="{t['libri']}">
    <img src="/img/libri/{b['isbn13']}.jpg" alt="{t['alt_cover']} {b['titolo']}" width="383" height="536">
    <div>
      <span class="lbl">{t['ultimo']}</span>
      <cite>{b['titolo']}</cite><span class="subt">{b['sottotitolo']}</span>
      <small>{b['editore']}, {b[t['luogo']]}</small>
      <span class="go">{t['tutti'].format(n=len(LIBRI))}</span>
    </div>
  </a>
</div></section>

<section id="attivita"><div class="wrap">
  <h2>{t['h_att']}</h2>
  <div class="cols">
{att}
  </div>
</div></section>

''' + FOOT + GROOVES + '</body>\n</html>\n'

def libri(t):
    li = ''
    for b in LIBRI:
        u = url(b)
        li += f'''    <li><a class="cover" href="{u}" target="_blank" rel="noopener" tabindex="-1" aria-hidden="true"><img src="/img/libri/{b['isbn13']}.jpg" alt="" loading="lazy" width="383" height="536"></a>
      <div><cite><a title="{t['felt']}" href="{u}" target="_blank" rel="noopener">{b['titolo']}</a></cite><span class="subt">{b['sottotitolo']}</span><small>{b['editore']}, {b[t['luogo']]} · ISBN {b['isbn']}</small></div></li>
'''
    title = f"{t['libri_title']} · Francesco Brusco"
    return head(t, title, '/libri/', '/en/books/') + nav(t, t['other_libri'], False) + f'''
<header class="page"><div class="wrap">
  <a class="back" href="{t['home']}">{t['back']}</a>
  <h1 style="margin-top:20px">{t['libri_title']}</h1>
  <p>{t['libri_lede']}</p>
</div></header>

<section class="alt" style="padding-top:56px"><div class="wrap">
  <ul class="books">
{li}  </ul>
</div></section>

''' + FOOT + '</body>\n</html>\n'

out = {'index.html': home(T['it']), 'libri/index.html': libri(T['it']),
       'en/index.html': home(T['en']), 'en/books/index.html': libri(T['en'])}
for path, html in out.items():
    f = ROOT / path
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(html, encoding='utf-8')
    print('Scritto', path)
