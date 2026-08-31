# -*- coding: utf-8 -*-
"""Generatore del sito statico di Kinesiologia Studio.
Uso: python3 build.py  -> scrive i file HTML nella cartella ../sito-kinesiologia-studio (output).
I contenuti stanno in content.py e negli articoli (articoli/*.json).
"""
import json, os, re, html, shutil, datetime
from content import SITE, PAGES, PROBLEMI, RECENSIONI, TRATTAMENTI, REGALI

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'out')

def slugify(s):
    s = s.lower()
    s = re.sub(r"[àá]", "a", s); s = re.sub(r"[èé]", "e", s); s = re.sub(r"[ìí]", "i", s)
    s = re.sub(r"[òó]", "o", s); s = re.sub(r"[ùú]", "u", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip('-')
    return s[:70]

def esc(s): return html.escape(s, quote=True)

def paras(text):
    """Testo con doppie righe vuote -> paragrafi. Supporta **grassetto** e liste con '- '."""
    out = []
    for block in text.strip().split('\n\n'):
        block = block.strip()
        if not block: continue
        if block.startswith('## '):
            out.append('<h2>%s</h2>' % inline(block[3:])); continue
        if block.startswith('### '):
            out.append('<h3>%s</h3>' % inline(block[4:])); continue
        if all(l.startswith('- ') for l in block.split('\n')):
            out.append('<ul>' + ''.join('<li>%s</li>' % inline(l[2:]) for l in block.split('\n')) + '</ul>'); continue
        if block.startswith('> '):
            out.append('<blockquote>%s</blockquote>' % inline(block[2:])); continue
        out.append('<p>%s</p>' % inline(block))
    return '\n'.join(out)

def inline(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', s)
    return s.replace('\n', '<br>')

# ---------- articoli ----------
def load_articles():
    arts = []
    for fn in sorted(os.listdir(os.path.join(ROOT, 'articoli'))):
        if fn.endswith('.json'):
            arts += json.load(open(os.path.join(ROOT, 'articoli', fn), encoding='utf-8'))
    today = datetime.date.today().isoformat()
    for a in arts:
        a['slug'] = a.get('slug') or slugify(a['title'])
        a['url'] = 'blog/%s.html' % a['slug']
        a['published'] = a.get('date', '2026-01-01') <= today
        a['excerpt'] = a.get('preview') or a['text'].split('\n\n')[0][:220].rsplit(' ', 1)[0] + '…'
    arts = [a for a in arts if a['published']]
    arts.sort(key=lambda a: a['date'], reverse=True)
    return arts

TOPIC_LABEL = {'schiena': 'Schiena', 'cervicale': 'Cervicale e testa', 'spalla': 'Spalla', 'postura': 'Postura',
               'piede': 'Piede e gamba', 'stress': 'Respiro e stress', 'mandibola': 'Mandibola', 'sport': 'Sport e allenamento',
               'metodo': 'Come lavoro'}

def fmt_date(iso):
    d = datetime.date.fromisoformat(iso)
    mesi = ['gennaio','febbraio','marzo','aprile','maggio','giugno','luglio','agosto','settembre','ottobre','novembre','dicembre']
    return '%d %s %d' % (d.day, mesi[d.month-1], d.year)

# ---------- layout ----------
def layout(title, desc, body, depth=0, canonical='', og_type='website', extra_head=''):
    p = '../' * depth
    nav = ''.join('<li><a href="%s%s"%s>%s</a></li>' % (p, h, ' class="cta"' if h == 'contatti.html' else '', t)
                  for t, h in SITE['nav'])
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE['url']}/{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{SITE['url']}/{canonical}">
<meta property="og:image" content="{SITE['url']}/assets/og.png">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:locale" content="it_IT">
<link rel="icon" href="{p}assets/icon-192.png">
<link rel="apple-touch-icon" href="{p}assets/icon-192.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Instrument+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css">
{extra_head}
</head>
<body>
<a class="skip" href="#main">Vai al contenuto</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{p}index.html">
      <img src="{p}assets/icon-192.png" alt="" width="36" height="36">
      <span><strong>Kinesiologia Studio</strong><small>Dott. Davide Scuderi · Modena</small></span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
    <nav id="nav" class="nav"><ul>{nav}</ul></nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap grid-3">
    <div>
      <p class="f-brand"><strong>Kinesiologia Studio</strong><br>Dott. Davide Scuderi<br>Massoterapista · Chinesiologo</p>
      <p>Via Capilupi 21, Modena<br><small>(suonare a "Studio Olistico")</small></p>
      <p><a href="tel:+393481514382">348 151 4382</a><br><a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
    </div>
    <div>
      <p><strong>Orari</strong><br>Lunedì–Venerdì 9:00–20:00<br>Sabato 9:00–15:00</p>
      <p><a class="btn btn-sm" href="{SITE['calendly']}" target="_blank" rel="noopener">Prenota online</a>
      <a class="btn btn-sm btn-ghost" href="{SITE['whatsapp']}" target="_blank" rel="noopener">WhatsApp</a></p>
    </div>
    <div>
      <p><strong>Esplora</strong></p>
      <ul class="f-links">
        <li><a href="{p}prima-valutazione.html">La prima valutazione</a></li>
        <li><a href="{p}trattamenti.html">Trattamenti e prezzi</a></li>
        <li><a href="{p}blog/index.html">Blog</a></li>
        <li><a href="{p}regala.html">Regala un trattamento</a></li>
        <li><a href="{p}app.html">L'app dello Studio</a></li>
        <li><a href="{p}privacy.html">Privacy e cookie</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap f-legal">
    <p>© {datetime.date.today().year} Kinesiologia Studio · Davide Scuderi · {SITE['piva']}</p>
    <p class="f-disclaimer">I contenuti di questo sito hanno scopo informativo e non sostituiscono una visita medica. Il massoterapista non formula diagnosi: in presenza di sintomi importanti o improvvisi rivolgiti al tuo medico.</p>
  </div>
</footer>
<script src="{p}assets/site.js"></script>
</body>
</html>"""

def newsletter_block(depth=0):
    return f"""
<section class="newsletter" id="newsletter">
  <div class="wrap nl-inner">
    <div>
      <p class="eyebrow">Ogni due settimane, via email</p>
      <h2>Capire il proprio corpo, un articolo alla volta</h2>
      <p>Gli stessi articoli che leggi qui e nell'app, con un criterio pratico in ogni puntata: cosa osservare, cosa provare a casa, quando è il momento di farsi vedere. Niente promozioni a raffica: puoi cancellarti con un clic.</p>
    </div>
    <form class="nl-form" action="{SITE['brevo_action']}" method="POST" target="_blank" data-nl>
      <label>Nome <input type="text" name="FIRSTNAME" autocomplete="given-name" required></label>
      <label>Email <input type="email" name="EMAIL" autocomplete="email" required></label>
      <label class="check"><input type="checkbox" name="OPT_IN" value="1" required> <span>Acconsento a ricevere via email contenuti informativi e comunicazioni dello Studio. Ho letto l'<a href="{'../'*depth}privacy.html">informativa privacy</a>. Posso revocare il consenso in ogni momento.</span></label>
      <input type="hidden" name="email_address_check" value="" class="hp">
      <input type="hidden" name="locale" value="it">
      <button class="btn" type="submit">Iscrivimi</button>
      <p class="nl-note" data-nl-note hidden>Grazie! Controlla la posta: ti abbiamo mandato un'email per confermare l'iscrizione.</p>
    </form>
  </div>
</section>"""

def cta_block(depth=0, title="Hai un fastidio che torna sempre?", text="La prima valutazione serve esattamente a questo: capire da dove parte, prima di decidere cosa fare."):
    p = '../' * depth
    return f"""
<section class="cta-band">
  <div class="wrap">
    <h2>{esc(title)}</h2>
    <p>{esc(text)}</p>
    <p class="btn-row">
      <a class="btn btn-light" href="{SITE['calendly']}" target="_blank" rel="noopener">Prenota la prima valutazione</a>
      <a class="btn btn-outline-light" href="{SITE['whatsapp']}" target="_blank" rel="noopener">Scrivimi su WhatsApp</a>
    </p>
    <p class="small">60 minuti · Via Capilupi 21, Modena · <a href="{p}prima-valutazione.html">Cosa succede alla prima valutazione</a></p>
  </div>
</section>"""

def review_cards(items):
    return '<div class="reviews">' + ''.join(
        f'<figure class="review"><blockquote>«{esc(r["text"])}»</blockquote><figcaption>{esc(r["name"])}</figcaption></figure>' for r in items) + '</div>'

def article_card(a, depth=0):
    p = '../' * depth
    return f"""<article class="card post-card">
  <p class="eyebrow">{esc(TOPIC_LABEL.get(a.get('topic',''), a.get('cat','')))} · {fmt_date(a['date'])}</p>
  <h3><a href="{p}{a['url']}">{esc(a['title'])}</a></h3>
  <p>{esc(a['excerpt'])}</p>
  <a class="more" href="{p}{a['url']}">Leggi l'articolo →</a>
</article>"""

# ---------- pagine ----------
def build():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, 'blog')); os.makedirs(os.path.join(OUT, 'problemi')); os.makedirs(os.path.join(OUT, 'assets'))
    for f in os.listdir(os.path.join(ROOT, 'assets')):
        shutil.copy(os.path.join(ROOT, 'assets', f), os.path.join(OUT, 'assets', f))
    open(os.path.join(OUT, 'CNAME'), 'w').write('kinesiologiastudio.it\n')
    open(os.path.join(OUT, '.nojekyll'), 'w').write('')

    arts = load_articles()

    # HOME
    prob_cards = ''.join(f"""<a class="card prob-card" href="problemi/{pr['slug']}.html">
      <span class="prob-icon">{pr['icon']}</span><h3>{esc(pr['title'])}</h3><p>{esc(pr['teaser'])}</p><span class="more">Capire il perché →</span></a>""" for pr in PROBLEMI)
    home = f"""
<section class="hero">
  <div class="wrap hero-inner">
    <div>
      <p class="eyebrow">Massoterapia e chinesiologia · Modena</p>
      <h1>Prima di trattare, <em>bisogna capire.</em></h1>
      <p class="lead">Schiena, cervicale, spalla, postura: il dolore ti dice dove fa male, non perché. Alla prima valutazione cerchiamo il perché — e solo dopo decidiamo se, come e dove intervenire.</p>
      <p class="btn-row">
        <a class="btn" href="{SITE['calendly']}" target="_blank" rel="noopener">Prenota la prima valutazione</a>
        <a class="btn btn-ghost" href="prima-valutazione.html">Come funziona</a>
      </p>
      <p class="proof">★★★★★ <strong>5,0 su Google</strong> · 128 recensioni · <a href="{SITE['google_reviews']}" target="_blank" rel="noopener">leggile tutte</a></p>
    </div>
    <div class="hero-card">
      <p class="eyebrow">Il metodo, in una riga</p>
      <ol class="steps">
        <li><strong>Ascolto</strong> la tua storia, non solo i sintomi</li>
        <li><strong>Osservo</strong> come ti muovi, globalmente</li>
        <li><strong>Valuto</strong> con test la tua condizione</li>
        <li><strong>Ragiono</strong> sulla causa dei tuoi problemi</li>
        <li><strong>Intervengo</strong> sulla causa in modo efficace</li>
        <li><strong>Rivaluto</strong> per misurare cosa è cambiato</li>
      </ol>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">Si arriva per il problema, si sceglie per il metodo.</p>
    <h2>Per cosa le persone vengono in studio</h2>
    <p class="intro">Ogni pagina spiega come ragiono su quel problema: cosa guardo, cosa escludo, perché la stessa parola — "cervicale", "mal di schiena" — può portare a interventi diversi.</p>
    <div class="grid-4">{prob_cards}</div>
  </div>
</section>

<section class="section alt">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Perché non parto dal massaggio</p>
      <h2>Lo stesso sintomo, scelte diverse</h2>
      <p>Due persone arrivano con lo stesso dolore al collo. Una ha un dorso rigido che scarica tutto sul collo: lì il massaggio da solo dura un giorno, serve restituire movimento alla base. L'altra ha una mandibola che stringe di notte: il collo è solo il posto dove il conto arriva. Stesso sintomo, due strade.</p>
      <p>Per questo non ho un listino di tecniche da cui scegliere in base al sintomo. Ho una valutazione, e da quella deriva l'intervento: manuale, di movimento, un esercizio da portare a casa, oppure — a volte — il consiglio di sentire prima il medico.</p>
      <p><a class="more" href="prima-valutazione.html">Cosa succede alla prima valutazione →</a></p>
    </div>
    <div>
      <figure class="photo"><img src="assets/squat.jpg" alt="Davide Scuderi osserva il movimento di un paziente durante la valutazione" loading="lazy"></figure>
      <div class="card quote-card"><p class="big-quote">"Un esercizio aiuta, ma non dice il <em>perché</em>. In studio lo cerchiamo insieme, con calma."</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">Le parole di chi è passato di qui</p>
    <h2>Esperienze individuali, non promesse</h2>
    <p class="intro">Ogni caso è diverso e nessuna recensione garantisce lo stesso risultato a un'altra persona. Le riporto perché raccontano, meglio di me, cosa cambia quando prima si capisce e poi si interviene.</p>
    {review_cards(RECENSIONI[:3])}
    <p class="center"><a class="btn btn-ghost" href="{SITE['google_reviews']}" target="_blank" rel="noopener">Tutte le 128 recensioni su Google</a></p>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <p class="eyebrow">Dal blog</p>
    <h2>Capire il proprio corpo</h2>
    <div class="grid-3">{''.join(article_card(a) for a in arts[:3])}</div>
    <p class="center"><a class="more" href="blog/index.html">Tutti gli articoli →</a></p>
  </div>
</section>

<section class="section" id="app">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Gratis, per chi viene in studio</p>
      <h2>L'app dello Studio, tra un trattamento e l'altro</h2>
      <p>Il trattamento dura un'ora: il resto del mese lo passi tu con il tuo corpo. L'app ti ricorda quando è il momento del controllo, ti dà gli esercizi di prevenzione per la zona che senti e ti fa segnare come stai, giorno per giorno.</p>
      <ul class="ticks">
        <li><strong>Promemoria del check-up</strong>, con il conto dei giorni</li>
        <li><strong>Esercizi per zona</strong>: schiena, cervicale, spalla, anca, gambe, mandibola</li>
        <li><strong>Diario del corpo</strong>: un voto al giorno, il grafico lo guardiamo insieme</li>
      </ul>
      <p class="btn-row">
        <a class="btn" href="{SITE['app']}" target="_blank" rel="noopener">Apri l'app</a>
        <a class="btn btn-ghost" href="app.html">Cosa c'è dentro</a>
      </p>
    </div>
    <div class="card quote-card">
      <p class="eyebrow">Niente store, niente registrazione</p>
      <p class="big-quote">Si apre da un link e la aggiungi alla schermata <em>Home</em>: da lì funziona come un'app, anche offline.</p>
      <p class="small" style="color:#B9C4BD">Quello che segni resta sul tuo telefono.</p>
    </div>
  </div>
</section>
{newsletter_block()}
{cta_block()}
"""
    write('index.html', layout(SITE['name'] + ' — Massoterapista e chinesiologo a Modena', 'Schiena, cervicale, spalla, postura: prima di trattare, bisogna capire. Valutazione, ragionamento e intervento scelto sul tuo caso. Dott. Davide Scuderi, Modena.', home, canonical=''))

    # PRIMA VALUTAZIONE
    pv = PAGES['valutazione']
    body = f"""
<section class="page-head"><div class="wrap">
  <p class="eyebrow">{esc(pv['eyebrow'])}</p><h1>{esc(pv['title'])}</h1><p class="lead">{esc(pv['lead'])}</p>
  <p class="btn-row"><a class="btn" href="{SITE['calendly']}" target="_blank" rel="noopener">Prenota la prima valutazione</a> <a class="btn btn-ghost" href="{SITE['whatsapp']}" target="_blank" rel="noopener">Prima una domanda su WhatsApp</a></p>
</div></section>
<section class="section media-band"><div class="wrap photo-row">
  <figure class="photo"><img src="assets/colloquio.jpg" alt="Davide Scuderi ascolta un paziente alla scrivania dello studio" loading="lazy"><figcaption>Prima si ascolta</figcaption></figure>
  <figure class="photo"><img src="assets/test-spalla.jpg" alt="Test di mobilità della spalla durante la valutazione" loading="lazy"><figcaption>Poi si misura</figcaption></figure>
  <figure class="photo"><img src="assets/squat.jpg" alt="Osservazione del movimento: valutazione di uno squat" loading="lazy"><figcaption>E si osserva il movimento</figcaption></figure>
</div></section>
<section class="section"><div class="wrap prose">{paras(pv['body'])}</div></section>
<section class="section alt"><div class="wrap">
  <h2>In pratica</h2>
  <div class="grid-3 facts">
    <div class="card"><p class="eyebrow">Durata</p><p class="big">60 minuti</p><p>Circa metà per capire, metà per intervenire su quello che troviamo.</p></div>
    <div class="card"><p class="eyebrow">Costo</p><p class="big">{esc(TRATTAMENTI['valutazione_prezzo'])}</p><p>Comprende valutazione, test, primo intervento ed esercizi da portare a casa. <a href="trattamenti.html">Tutti i prezzi</a>.</p></div>
    <div class="card"><p class="eyebrow">Dove</p><p class="big">Via Capilupi 21</p><p>Modena, zona direzionale Toscanini. Suonare a "Studio Olistico".</p></div>
  </div>
</div></section>
{cta_block(title="Prenota la prima valutazione", text="Scegli giorno e ora online: ricevi subito la conferma via email con un promemoria prima dell'appuntamento.")}
"""
    write('prima-valutazione.html', layout(pv['title'] + ' — Kinesiologia Studio Modena', pv['lead'], body, canonical='prima-valutazione.html'))

    # PROBLEMI
    for pr in PROBLEMI:
        related = [a for a in arts if a.get('topic') in pr['topics']][:3]
        rel_html = ('<section class="section alt"><div class="wrap"><h2>Per approfondire</h2><div class="grid-3">' + ''.join(article_card(a, 1) for a in related) + '</div></div></section>') if related else ''
        body = f"""
<section class="page-head"><div class="wrap">
  <p class="eyebrow">{esc(pr['eyebrow'])}</p><h1>{esc(pr['h1'])}</h1><p class="lead">{esc(pr['lead'])}</p>
  <p class="btn-row"><a class="btn" href="{SITE['calendly']}" target="_blank" rel="noopener">Prenota la prima valutazione</a> <a class="btn btn-ghost" href="tel:+393481514382">Chiama 348 151 4382</a></p>
</div></section>
<section class="section media-band"><div class="wrap"><figure class="photo"><img src="../assets/{pr['img']}" alt="{esc(pr['alt'])}" loading="lazy"></figure></div></section>
<section class="section"><div class="wrap prose">{paras(pr['body'])}</div></section>
<section class="section"><div class="wrap">
  <div class="card warn"><p class="eyebrow">Quando non sono io la persona giusta</p>{paras(pr['red_flags'])}</div>
</div></section>
{rel_html}
{cta_block(1)}
"""
        write('problemi/%s.html' % pr['slug'], layout(pr['title'] + ' a Modena — Kinesiologia Studio', pr['lead'], body, depth=1, canonical='problemi/%s.html' % pr['slug']))

    # TRATTAMENTI E PREZZI
    tr = ''.join(f"""<div class="card"><h3>{esc(t['n'])}</h3><p class="price">{esc(t['p'])}</p><p>{esc(t['d'])}</p></div>""" for t in TRATTAMENTI['lista'])
    body = f"""
<section class="page-head"><div class="wrap">
  <p class="eyebrow">Trattamenti e prezzi</p><h1>Un'ora che serve a capire, non solo a trattare</h1>
  <p class="lead">Ogni seduta comprende valutazione, test muscolari, intervento manuale o di movimento ed esercizi da portare a casa. L'intervento cambia in base a cosa emerge dalla valutazione: il tempo e il prezzo no.</p>
</div></section>
<section class="section media-band"><div class="wrap photo-row two">
  <figure class="photo"><img src="assets/trattamento.jpg" alt="Trattamento della schiena in studio" loading="lazy"></figure>
  <figure class="photo"><img src="assets/trattamento2.jpg" alt="Trattamento del collo in studio" loading="lazy"></figure>
</div></section>
<section class="section"><div class="wrap">
  <div class="grid-3">{tr}</div>
  <p class="note">{esc(TRATTAMENTI['nota'])}</p>
</div></section>
<section class="section alt"><div class="wrap prose">{paras(TRATTAMENTI['testo'])}</div></section>
{cta_block()}
"""
    write('trattamenti.html', layout('Trattamenti e prezzi — Kinesiologia Studio Modena', 'Prezzi trasparenti: prima valutazione, trattamento da 60 e 30 minuti, percorsi. Ogni seduta comprende valutazione, test, intervento ed esercizi.', body, canonical='trattamenti.html'))

    # CHI SONO
    cs = PAGES['chi_sono']
    body = f"""
<section class="page-head"><div class="wrap split">
  <div><p class="eyebrow">{esc(cs['eyebrow'])}</p><h1>{esc(cs['title'])}</h1><p class="lead">{esc(cs['lead'])}</p></div>
  <div class="portrait"><img src="assets/davide.jpg" alt="Davide Scuderi nello studio di Modena" loading="lazy"></div>
</div></section>
<section class="section"><div class="wrap prose">{paras(cs['body'])}</div></section>
{cta_block()}
"""
    write('chi-sono.html', layout('Chi sono — Davide Scuderi, massoterapista e chinesiologo a Modena', cs['lead'], body, canonical='chi-sono.html'))

    # BLOG index
    cards = ''.join(article_card(a, 1) for a in arts)
    topics = sorted({a.get('topic','') for a in arts if a.get('topic')})
    body = f"""
<section class="page-head"><div class="wrap">
  <p class="eyebrow">Blog</p><h1>Capire il proprio corpo</h1>
  <p class="lead">Articoli brevi, scritti per chi ha un fastidio e vuole capirlo prima di curarlo. Gli stessi che trovi nell'app dello Studio e nella newsletter.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="grid-3">{cards}</div>
</div></section>
<section class="section alt"><div class="wrap split">
  <div>
    <p class="eyebrow">Gli stessi articoli, in tasca</p>
    <h2>Nell'app c'è anche l'archivio</h2>
    <p>L'app dello Studio raccoglie questi articoli insieme al falso mito della settimana, agli esercizi di prevenzione per la tua zona e al promemoria del prossimo controllo. Puoi anche proporre l'argomento di cui parlare la volta dopo.</p>
    <p class="btn-row">
      <a class="btn" href="{SITE['app']}" target="_blank" rel="noopener">Apri l'app</a>
      <a class="btn btn-ghost" href="../app.html">Cosa c'è dentro</a>
    </p>
  </div>
  <div class="card">
    <p class="eyebrow">In due tocchi</p>
    <ol class="steps">
      <li>Apri l'app dal link: è una pagina, non un download</li>
      <li>Aggiungila alla schermata Home</li>
      <li>Funziona anche senza connessione</li>
    </ol>
  </div>
</div></section>
{newsletter_block(1)}
"""
    write('blog/index.html', layout('Blog — Kinesiologia Studio', 'Articoli per capire schiena, cervicale, spalla, postura e dolore: cosa osservare, cosa provare, quando farsi vedere.', body, depth=1, canonical='blog/index.html'))

    # BLOG articles
    for i, a in enumerate(arts):
        prev_a = arts[i+1] if i+1 < len(arts) else None
        next_a = arts[i-1] if i > 0 else None
        pn = '<nav class="post-nav">'
        if prev_a: pn += f'<a href="{prev_a["slug"]}.html">← {esc(prev_a["title"])}</a>'
        if next_a: pn += f'<a href="{next_a["slug"]}.html" class="right">{esc(next_a["title"])} →</a>'
        pn += '</nav>'
        share = f"""<div class="share"><span>Condividi:</span>
  <a href="https://wa.me/?text={esc(a['title'])}%20{SITE['url']}/{a['url']}" target="_blank" rel="noopener">WhatsApp</a>
  <a href="https://www.facebook.com/sharer/sharer.php?u={SITE['url']}/{a['url']}" target="_blank" rel="noopener">Facebook</a>
  <button type="button" data-copy="{SITE['url']}/{a['url']}">Copia link</button></div>"""
        body = f"""
<article class="post">
  <header class="page-head"><div class="wrap narrow">
    <p class="eyebrow">{esc(TOPIC_LABEL.get(a.get('topic',''), a.get('cat','')))} · {fmt_date(a['date'])} · Davide Scuderi</p>
    <h1>{esc(a['title'])}</h1>
  </div></header>
  <div class="wrap narrow prose">{paras(a['text'])}
    <div class="card warn small"><p>Questo articolo è informativo e non sostituisce una valutazione. Se il fastidio è comparso di colpo, peggiora o si accompagna ad altri sintomi, parlane prima con il tuo medico.</p></div>
    {share}
    {pn}
  </div>
</article>
{cta_block(1, title="Ti riconosci in questa descrizione?", text="Alla prima valutazione guardiamo insieme da dove arriva, prima di decidere cosa fare.")}
{newsletter_block(1)}
"""
        write(a['url'], layout(a['title'] + ' — Kinesiologia Studio', a['excerpt'], body, depth=1, canonical=a['url'], og_type='article'))

    # REGALA
    gifts = ''.join(f"""<div class="card"><h3>{esc(g['n'])}</h3><p class="price">{esc(g['p'])}</p><p>{esc(g['d'])}</p><a class="btn btn-sm" href="{g['sumup']}" target="_blank" rel="noopener">Regala {esc(g['n'])}</a></div>""" for g in REGALI)
    body = f"""
<section class="page-head"><div class="wrap">
  <p class="eyebrow">Idee regalo</p><h1>Il regalo che si sente addosso</h1>
  <p class="lead">Paghi online con carta e ricevi subito il voucher da stampare o inviare su WhatsApp. Chi lo riceve prenota quando vuole, e la prima cosa che facciamo insieme è capire di cosa ha bisogno.</p>
</div></section>
<section class="section"><div class="wrap"><div class="grid-3">{gifts}</div>
<p class="note">Il pagamento avviene su SumUp, in modo sicuro. Dopo il pagamento riceverai il voucher via email; se hai dubbi scrivimi su <a href="{SITE['whatsapp']}" target="_blank" rel="noopener">WhatsApp</a>.</p></div></section>
"""
    write('regala.html', layout('Regala un trattamento — Kinesiologia Studio Modena', 'Voucher regalo: trattamento da 30 o 60 minuti, percorsi e un anno di prevenzione. Pagamento online, voucher subito.', body, canonical='regala.html'))

    # CONTATTI
    body = f"""
<section class="page-head"><div class="wrap">
  <p class="eyebrow">Contatti e prenotazione</p><h1>Prenota, scrivi o chiama</h1>
  <p class="lead">Scegli il modo che preferisci. Se non sai se il tuo caso fa per me, scrivimi due righe: ti rispondo io.</p>
</div></section>
<section class="section"><div class="wrap grid-4 contact-grid">
  <div class="card"><p class="eyebrow">Prenota online</p><h3>Calendario</h3><p>Scegli giorno e ora, ricevi conferma via email e un promemoria prima dell'appuntamento.</p><a class="btn" href="{SITE['calendly']}" target="_blank" rel="noopener">Apri il calendario</a></div>
  <div class="card"><p class="eyebrow">Scrivimi</p><h3>WhatsApp</h3><p>Per una domanda prima di prenotare, o per un orario che non trovi nel calendario.</p><a class="btn btn-ghost" href="{SITE['whatsapp']}" target="_blank" rel="noopener">Apri WhatsApp</a></div>
  <div class="card"><p class="eyebrow">Chiama</p><h3>348 151 4382</h3><p>Se sono in seduta non rispondo: lascia un messaggio, ti richiamo appena posso.</p><a class="btn btn-ghost" href="tel:+393481514382">Chiama ora</a></div>
  <div class="card"><p class="eyebrow">Prevenzione</p><h3>L'app dello Studio</h3><p>Promemoria del check-up, esercizi per la tua zona e diario del corpo. Gratis, si aggiunge alla schermata Home.</p><a class="btn btn-ghost" href="app.html">Scopri l'app</a></div>
</div></section>
<section class="section media-band"><div class="wrap"><figure class="photo"><img src="assets/contatti.jpg" alt="Colloquio iniziale nello studio di Via Capilupi 21 a Modena" loading="lazy"></figure></div></section>
<section class="section alt"><div class="wrap split">
  <div>
    <h2>Lo studio</h2>
    <p><strong>Via Capilupi 21, Modena</strong> — zona direzionale Toscanini. Al citofono suonare a "Studio Olistico".</p>
    <p><strong>Orari:</strong> lunedì–venerdì 9:00–20:00, sabato 9:00–15:00.</p>
    <p><strong>Email:</strong> <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
    <p><a class="btn btn-sm btn-ghost" href="https://www.google.com/maps/search/?api=1&query=Kinesiologia+Studio+Via+Capilupi+21+Modena" target="_blank" rel="noopener">Indicazioni su Google Maps</a></p>
  </div>
  <div class="card">
    <p class="eyebrow">Come funziona la prenotazione</p>
    <ol class="steps">
      <li>Scegli data e ora dal calendario</li>
      <li>Inserisci nome, email e telefono</li>
      <li>Ricevi la conferma via email</li>
      <li>Vieni in studio: al resto pensiamo insieme</li>
    </ol>
    <p><a class="more" href="prima-valutazione.html">Cosa succede alla prima valutazione →</a></p>
  </div>
</div></section>
"""
    write('contatti.html', layout('Contatti e prenotazione — Kinesiologia Studio Modena', 'Prenota online, scrivi su WhatsApp o chiama. Via Capilupi 21, Modena. Lun–Ven 9–20, Sab 9–15.', body, canonical='contatti.html'))

    # APP
    body = f"""
<section class="page-head"><div class="wrap">
  <p class="eyebrow">Gratis · niente da scaricare dagli store</p><h1>L'app dello Studio</h1>
  <p class="lead">Il trattamento dura un'ora, il resto del mese lo passi tu con il tuo corpo. L'app serve a quello: ricordarti il controllo, darti gli esercizi giusti per la tua zona e tenere traccia di come stai, così quando torni in studio partiamo da dati, non da ricordi.</p>
  <p class="btn-row">
    <a class="btn" href="{SITE['app']}" target="_blank" rel="noopener">Apri l'app</a>
    <a class="btn btn-ghost" href="#dentro">Cosa c'è dentro</a>
  </p>
  <p class="small">Si apre nel browser, come un sito. Se vuoi, la aggiungi alla schermata Home e da lì funziona come un'app, anche offline.</p>
</div></section>

<section class="section" id="dentro"><div class="wrap">
  <p class="eyebrow">Cosa trovi dentro</p>
  <h2>Sei cose che continuano a lavorare tra un trattamento e l'altro</h2>
  <div class="grid-3">
    <div class="card">
      <p class="eyebrow">Promemoria</p><h3>Il prossimo controllo</h3>
      <p>Scegli ogni quanto vuoi essere richiamato e l'app conta i giorni. Quando è il momento te lo dice, senza che tu debba ricordartelo a fine giornata.</p>
    </div>
    <div class="card">
      <p class="eyebrow">Esercizi</p><h3>Per la zona che senti</h3>
      <p>Schiena, cervicale, spalla, anca, gambe, mandibola: tocchi la zona e trovi esercizi di prevenzione da fare a casa, spiegati passo per passo.</p>
    </div>
    <div class="card">
      <p class="eyebrow">Ogni giorno</p><h3>Consiglio e micro-abitudine</h3>
      <p>Una cosa sola al giorno, piccola abbastanza da farla davvero. Chi tiene la serie per sette giorni sblocca le routine complete.</p>
    </div>
    <div class="card">
      <p class="eyebrow">Diario</p><h3>Come sta il tuo corpo</h3>
      <p>Un tocco al giorno da 0 a 10. Ne esce un grafico che mi mostri in studio: è il modo più onesto di capire se stiamo andando nella direzione giusta.</p>
    </div>
    <div class="card">
      <p class="eyebrow">Test</p><h3>Quanto è pronto il tuo corpo</h3>
      <p>Cinque mini-prove da fare in casa in due minuti, un punteggio e un piano della settimana che si aggiorna quando rifai il test.</p>
    </div>
    <div class="card">
      <p class="eyebrow">Studio</p><h3>Prenotazione e buoni</h3>
      <p>Il calendario, i trattamenti con i prezzi, le idee regalo e i buoni che si sbloccano usando l'app. Da mostrare direttamente in studio.</p>
    </div>
  </div>
  <p class="note">Gli esercizi dell'app sono di prevenzione generale e non sostituiscono una valutazione. In caso di dolore acuto o persistente sospendi e <a href="contatti.html">scrivimi</a>.</p>
</div></section>

<section class="section alt"><div class="wrap split">
  <div>
    <h2>Non si scarica: si aggiunge</h2>
    <p>Non la trovi su App Store o Play Store, e non serve. È una web app: si apre da un link, e se vuoi la metti sulla schermata Home con l'icona dello studio. Da lì si comporta come qualsiasi altra app — si apre a schermo intero e continua a funzionare anche senza connessione.</p>
    <p>Non chiede registrazione e non raccoglie i tuoi dati: quello che segni — il diario, le abitudini, il promemoria — resta sul tuo telefono.</p>
    <p class="btn-row"><a class="btn" href="{SITE['app']}" target="_blank" rel="noopener">Apri l'app</a></p>
  </div>
  <div class="card">
    <p class="eyebrow">Come metterla sulla Home</p>
    <ol class="steps">
      <li><strong>Apri l'app</strong> dal pulsante qui accanto</li>
      <li><strong>iPhone:</strong> tocca Condividi, poi "Aggiungi a Home"</li>
      <li><strong>Android:</strong> menu ⋮, poi "Installa app"</li>
      <li><strong>Attiva le notifiche</strong> se vuoi il promemoria del check-up</li>
    </ol>
    <p class="small">Dentro l'app trovi anche un pulsante "Installa" che fa la stessa cosa in un tocco.</p>
  </div>
</div></section>
{cta_block(title="L'app accompagna, la valutazione capisce", text="Un esercizio aiuta, ma non dice il perché. Se un fastidio torna sempre, il posto giusto per cercarlo è lo studio.")}
"""
    write('app.html', layout("L'app dello Studio — Kinesiologia Studio Modena", "L'app gratuita dello Studio: promemoria del check-up, esercizi di prevenzione per zona, consiglio del giorno e diario del corpo. Si aggiunge alla schermata Home e funziona offline.", body, canonical='app.html'))

    # PRIVACY
    body = f"""<section class="page-head"><div class="wrap narrow"><p class="eyebrow">Informativa</p><h1>Privacy e cookie</h1></div></section>
<section class="section"><div class="wrap narrow prose">{paras(PAGES['privacy'])}</div></section>"""
    write('privacy.html', layout('Privacy e cookie — Kinesiologia Studio', 'Informativa sul trattamento dei dati personali e sui cookie del sito kinesiologiastudio.it.', body, canonical='privacy.html'))

    # 404 + sitemap + robots
    body = """<section class="page-head"><div class="wrap narrow"><h1>Pagina non trovata</h1><p class="lead">Il sito è stato rinnovato e alcuni vecchi indirizzi non esistono più. Prova dalla <a href="/index.html">home</a> o dal <a href="/blog/index.html">blog</a>.</p></div></section>"""
    write('404.html', layout('Pagina non trovata — Kinesiologia Studio', 'Pagina non trovata', body, canonical='404.html'))
    urls = ['', 'prima-valutazione.html', 'trattamenti.html', 'chi-sono.html', 'contatti.html', 'regala.html', 'app.html', 'blog/index.html'] + \
           ['problemi/%s.html' % p['slug'] for p in PROBLEMI] + [a['url'] for a in arts]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
         ''.join('  <url><loc>%s/%s</loc></url>\n' % (SITE['url'], u) for u in urls) + '</urlset>\n'
    open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm)
    open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n' % SITE['url'])

    # newsletter export (per Brevo / app): JSON degli articoli
    json.dump([{k: a[k] for k in ('title', 'date', 'topic', 'text', 'url')} for a in arts],
              open(os.path.join(OUT, 'articoli.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('OK: %d pagine, %d articoli' % (len(urls), len(arts)))

def write(rel, content):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(content)

if __name__ == '__main__':
    build()
