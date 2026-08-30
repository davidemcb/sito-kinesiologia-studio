# -*- coding: utf-8 -*-
"""Contenuti del sito. Modifica qui i testi, poi esegui build.py."""

SITE = {
    'name': 'Kinesiologia Studio',
    'url': 'https://kinesiologiastudio.it',
    'email': 'infokinesiologia@gmail.com',
    'calendly': 'https://calendly.com/infokinesiologia/consulenza',
    'whatsapp': 'https://wa.me/393481514382?text=Ciao%20Davide%2C%20ti%20scrivo%20dal%20sito%3A%20',
    'google_reviews': 'https://www.google.com/maps/search/?api=1&query=Kinesiologia+Studio+Modena+Via+Capilupi',
    'app': 'https://davidemcb.github.io/kinesiologia-studio/',
    'brevo_action': '#',   # <- URL del form Brevo (da inserire quando l'account è pronto)
    'piva': 'P.IVA 02887890362 · C.F. SCDDVD81D23B819L',
    'nav': [('La prima valutazione', 'prima-valutazione.html'), ('Problemi', 'problemi/mal-di-schiena.html'),
            ('Trattamenti', 'trattamenti.html'), ('Blog', 'blog/index.html'), ('Chi sono', 'chi-sono.html'),
            ('Regala', 'regala.html'), ('Prenota', 'contatti.html')],
}

RECENSIONI = [
    {'text': "Schiena bloccata e dolorante da ieri sera, tanto da non riuscire a stare sdraiata o seduta. Davide mi ha trattata e ora riesco a fare tutti i movimenti e il dolore è quasi scomparso — e questo in una sola seduta.", 'name': 'Manuela P., naturopata'},
    {'text': "Ottimo professionista: dopo aver provato vari fisiatri e osteopati è stato l'unico con cui ho avuto dei grossi benefici.", 'name': 'Stefano S.'},
    {'text': "Ha intuito subito quale fosse il mio problema e il trattamento è stato risolutivo. Sono rimasta soddisfatta oltre le aspettative!", 'name': 'Virginia V.'},
    {'text': "Mi sono fatta una torsione alla caviglia il giorno prima di un torneo di padel. Sono andata da lui e il giorno dopo ho potuto giocare tutto il torneo. Non mi fa più male!", 'name': 'Alba N.'},
    {'text': "Sono uscita completamente libera e sbloccata da tutte le tensioni. Un senso di leggerezza unico. Stupefacente.", 'name': 'Nicoletta G.'},
    {'text': "Ho avuto problemi di contratture alla schiena, al collo e blocchi intestinali, tutti risolti nel giro di breve tempo. Se tu non ci fossi bisognerebbe inventarti.", 'name': 'Monica G.'},
]

TRATTAMENTI = {
    'valutazione_prezzo': '90 €',
    'lista': [
        {'n': 'Prima valutazione e trattamento', 'p': '90 € · 60 minuti', 'd': "Il primo incontro. Metà del tempo serve a capire: storia, osservazione, test muscolari e di movimento. L'altra metà a intervenire su quello che emerge. Esci con un'idea chiara del perché e con due o tre esercizi tuoi."},
        {'n': 'Seduta completa', 'p': '90 € · 60 minuti', 'd': "Per chi ha già fatto la valutazione o segue un percorso. Si parte sempre da una breve rivalutazione: cosa è cambiato dall'ultima volta decide cosa fare oggi."},
        {'n': 'Seduta breve', 'p': '47 € · 30 minuti', 'd': "Intervento mirato su una zona già valutata, o controllo di mantenimento per chi sta bene e vuole restarci. Non è la scelta giusta per un problema nuovo: lì serve l'ora intera."},
        {'n': 'Percorso Reset', 'p': '249 € · 3 sedute da 60 min', 'd': "Per chi si trascina un problema vero. Tre incontri sono il minimo per un cambiamento stabile, ed è onesto dirlo. Alla terza seduta rivalutiamo con gli stessi test della prima."},
        {'n': 'Percorso Trasformazione', 'p': '399 € · 5 sedute + ri-test', 'd': "Cinque sedute più una rivalutazione finale: il prima e il dopo, misurati con gli stessi test. Per chi vuole cambiare come si muove, non solo togliere un dolore."},
        {'n': 'Un anno di prevenzione', 'p': '297 € · 4 controlli', 'd': "Un controllo a stagione, per chi ha risolto e vuole accorgersi in tempo di quando qualcosa ricomincia a compensare. Il tagliando della schiena."},
    ],
    'nota': "I prezzi sono comprensivi di tutto: non ci sono supplementi per test, esercizi o materiale. Si paga in studio (contanti, carta) oppure online con voucher. Se non sei sicuro di quale scegliere, parti dalla prima valutazione: è quella che serve per decidere il resto.",
    'testo': """## Perché non c'è un listino di tecniche

Sui siti di molti studi trovi un elenco: decontratturante, linfodrenaggio, tecar, taping, trigger point. Scegli la tecnica, prenoti la tecnica. Qui non funziona così, e il motivo è semplice: la tecnica giusta la si conosce **dopo** aver capito il problema, non prima.

Nella stessa ora posso usare lavoro manuale sui tessuti, mobilizzazioni articolari, esercizi di controllo del movimento, lavoro sul respiro. Quale, e in che ordine, dipende da quello che emerge dai test. Due persone con lo stesso sintomo escono spesso con interventi diversi. È normale: è il segno che qualcuno ha guardato.

## Quando non tratto

A volte la cosa più utile che posso fare in un'ora è non fare il trattamento. Succede quando i test indicano qualcosa che va visto prima da un medico, quando il dolore è appena comparso e ha bisogno di calma più che di mani, o quando la persona ha bisogno di un esercizio e non di una seduta. In quei casi lo dico. Un massoterapista che a volte non massaggia non è un paradosso: è uno che ha guardato prima di decidere.

## Cosa comprende ogni seduta

Ascolto e storia del problema; osservazione di come ti muovi; test muscolari e articolari; intervento scelto in base ai test; esercizi da portare a casa, pochi e spiegati; rivalutazione a fine seduta e all'incontro successivo, per misurare cosa è cambiato davvero e non solo come ti senti.""",
}

REGALI = [
    {'n': "Mezz'ora per te", 'p': '47 €', 'd': "Il regalo sicuro: 30 minuti di trattamento mirato. Costa come un mazzo di fiori, se lo ricordano per mesi.", 'sumup': 'https://pay.sumup.com/b2c/Q84C0NZ5'},
    {'n': "Un'ora tutta sua", 'p': '90 €', 'd': "Il trattamento completo: valutazione, test muscolari, trattamento ed esercizi personali. Il regalo di compleanno che nessun altro fa.", 'sumup': 'https://pay.sumup.com/b2c/QQCVILTM'},
    {'n': 'Kit Rinascita', 'p': '97 €', 'd': 'Trattamento completo da 60 minuti + il libro "Vestirsi di Sé" di Davide Scuderi: l\'esperienza in studio e qualcosa da scartare subito.', 'sumup': 'https://pay.sumup.com/b2c/Q5E5UIKK'},
    {'n': 'Benessere in Due', 'p': '87 €', 'd': "Due trattamenti da 30 minuti per due persone: un'esperienza da condividere con chi vuoi bene.", 'sumup': 'https://pay.sumup.com/b2c/Q235U8U0'},
    {'n': 'Percorso Reset', 'p': '249 €', 'd': "Tre trattamenti da 60 minuti per chi si trascina un problema vero. Tre incontri sono il minimo per un cambiamento stabile — ed è onesto dirlo.", 'sumup': 'https://pay.sumup.com/b2c/QKAIRU5H'},
    {'n': 'Un Anno di Prevenzione', 'p': '297 €', 'd': "Quattro check-up, uno a stagione. Per chi ami e vuoi vedere in piedi a lungo: la sua schiena ha un tagliando per tutto l'anno.", 'sumup': 'https://pay.sumup.com/b2c/Q2N2HO1G'},
    {'n': 'Percorso Trasformazione', 'p': '399 €', 'd': "Cinque trattamenti più ri-test finale: il prima e il dopo, misurati. Un trattamento è praticamente in omaggio.", 'sumup': 'https://pay.sumup.com/b2c/QBXFL47P'},
]

PAGES = {
 'valutazione': {
    'eyebrow': 'La prima valutazione',
    'title': 'Cosa succede alla prima valutazione',
    'lead': "Sessanta minuti in cui la domanda non è «dove fa male?» ma «perché fa male proprio lì, proprio a te?». Ecco cosa faccio, in ordine, e cosa porti a casa.",
    'body': """## 1. Ascolto — la storia, non solo il sintomo

I primi minuti sono tuoi. Da quanto tempo, com'è cominciato, cosa lo peggiora e cosa lo calma, cosa hai già provato, cosa non riesci più a fare. Ti chiedo anche cose che sembrano lontane: un intervento di dieci anni fa, una caviglia che «ormai non fa più male», come dormi, quante ore stai seduto. Non fa male non vuol dire che lavora bene.

## 2. Osservo — come ti muovi, tutto intero

Ti guardo in piedi, mentre cammini, mentre ti pieghi, mentre ruoti. Non guardo solo la zona che indichi con il dito: guardo come il resto del corpo la sta aiutando o la sta caricando. Un collo che si irrigidisce sempre allo stesso modo spesso ha sotto un dorso che non collabora; un tallone che duole al mattino a volte dipende da un'anca che ha perso rotazione. Non sono regole fisse, sono ipotesi: e le ipotesi si verificano.

## 3. Valuto — test precisi, ripetibili

Test muscolari, di mobilità articolare, di controllo del movimento. Servono a due cose: capire cosa regge e cosa no, e avere un punto di partenza misurabile. Gli stessi test li rifaremo alla fine della seduta e agli incontri successivi: così sappiamo cosa è cambiato davvero, non solo come ti senti quel giorno.

## 4. Ragiono — e te lo spiego

Qui metto insieme i pezzi e ti dico cosa penso: da dove sembra arrivare il problema, cosa lo tiene in piedi, cosa possiamo aspettarci. In parole semplici, senza sigle. Quando capisci cosa sta succedendo nel tuo corpo, il sistema nervoso percepisce meno minaccia, e la minaccia percepita è uno degli ingredienti del dolore. Spiegare fa parte del trattamento.

## 5. Intervengo — solo dove ha senso

Nella seconda metà dell'ora lavoro su quello che abbiamo trovato: manualmente sui tessuti, con mobilizzazioni, con esercizi di controllo, con il respiro. La scelta dipende dai test, non dal sintomo. E se i test indicano qualcosa che va visto prima da un medico, te lo dico, e ti indirizzo. A volte la cosa più utile che posso fare è non trattare.

## 6. Rivaluto — e ti do i compiti

Rifacciamo i test. Poi ti lascio due o tre esercizi, non venti, spiegati e provati insieme, con un criterio chiaro per capire se stai esagerando. Se serve un secondo incontro te lo dico con un perché; se non serve, te lo dico lo stesso.

## Cosa portare

Abbigliamento comodo, che permetta di vedere come ti muovi. Se hai esami recenti (radiografie, risonanze, referti), portali: non li interpreto al posto del medico, ma mi aiutano a capire cosa è già stato escluso.""",
 },
 'chi_sono': {
    'eyebrow': 'Chi sono',
    'title': 'Davide Scuderi',
    'lead': "Massoterapista e chinesiologo a Modena. Il mio lavoro non è fare più trattamenti: è rendere comprensibile perché un certo intervento abbia senso per te e per la tua situazione.",
    'body': """Ho aperto Kinesiologia Studio con un'idea semplice che nel tempo è diventata un metodo: prima di trattare, bisogna capire. Non è uno slogan. È il motivo per cui la prima ora la divido a metà, e la prima metà non prevede nessun trattamento.

Nella pratica di tutti i giorni vedo soprattutto schiene, cervicali, spalle e posture che si sono adattate male a giornate lunghe e sedute. Ma la lista dei problemi conta meno del modo di guardarli: non un elenco di tecniche da applicare al sintomo, ma una valutazione da cui deriva l'intervento. Due persone con lo stesso dolore escono spesso con interventi diversi.

Tre cose in cui credo, e che ritrovi in ogni seduta. Che nessun terapista ripara un tessuto: lo ripara il corpo, e il mio lavoro è togliere i freni e dare lo stimolo giusto. Che il dolore non misura il danno, e spiegarlo è già parte del trattamento. Che a volte la risposta giusta è un esercizio, un consiglio, o «prima passa dal medico», e non una seduta in più.

## La formazione

Il mio percorso parte da lontano e tiene insieme corpo e persona. Sono naturopata dal 2003, diplomato presso l'Istituto di Medicina Psicosomatica Riza, con due master: uno in lettura del corpo in bioenergetica e uno in kinesiologia applicata. Mi sono poi laureato in Scienze Motorie e ho conseguito un master universitario di primo livello in psicologia delle organizzazioni. Sono massoterapista M.C.B. (massaggiatore e capo bagnino degli stabilimenti idroterapici), il titolo che in Italia abilita alla massoterapia.

Sono autore di «Vestirsi di Sé — manuale di automassaggio consapevole», e scrivo regolarmente articoli per i miei pazienti, che trovi nel blog e nell'app dello Studio. Preferisco un paziente che ha capito a un paziente che dipende da me.

Lo studio è in Via Capilupi 21 a Modena, zona direzionale Toscanini. Se vuoi capire se il tuo caso fa per me, scrivimi: ti rispondo io.""",
 },
 'privacy': """## Informativa privacy

In questa informativa si descrivono le modalità di gestione del sito in riferimento al trattamento dei dati personali degli utenti che lo consultano, nonché le pratiche di trattamento dei dati trasmessi dall'interessato al Titolare tramite questo sito.

In adempimento agli artt. 13 (per i dati raccolti presso l'interessato) e 14 (per i dati non raccolti presso l'interessato) del Regolamento (UE) 2016/679 (GDPR) si rendono agli Utenti di questo Sito Web le seguenti informazioni, che si riferiscono esclusivamente al trattamento eseguito attraverso detto Sito Web e non tramite altri siti web eventualmente visitati tramite link dal presente, per i quali si suggerisce di prendere visione delle relative informative rese dai rispettivi Titolari.

Questo Sito Web e i servizi eventualmente offerti tramite il Sito Web sono riservati a soggetti che hanno compiuto il diciottesimo anno di età. Il Titolare non raccoglie quindi dati personali relativi ai soggetti minori di anni 18. Su richiesta di tali Utenti, il Titolare ne cancellerà tempestivamente tutti i dati personali involontariamente raccolti.

### Titolare del trattamento

Lo Studio Kinesiologia di Scuderi Davide, con sede legale in via Capilupi n. 21, 41122 Modena — P.IVA 02887890362, C.F. SCDDVD81D23B819L (di seguito anche "Titolare"), in qualità di titolare del trattamento dei dati personali degli utenti del sito kinesiologiastudio.it (di seguito, "Utenti") fornisce qui di seguito l'informativa privacy ai sensi dell'art. 13 del Regolamento UE 2016/679 del 27 aprile 2016 (di seguito "Regolamento").

Il Titolare si riserva di nominare quale Responsabile del trattamento dei dati personali gestiti per le finalità di assistenza tecnica, manutenzione, gestione tecnica e simili del presente Sito un'agenzia web o un consulente, i cui riferimenti potranno essere comunicati a seguito di richiesta agli indirizzi sopra indicati.

### Finalità del trattamento

I dati personali degli Utenti del Sito Web saranno oggetto di trattamento nei modi e nelle forme prescritti dal GDPR, per lo svolgimento delle funzionalità proprie del Sito Web, con particolare riferimento alle procedure di raccolta dati, contatto, prenotazione e iscrizione alla newsletter. In particolare, i dati personali forniti al Titolare verranno trattati per le seguenti finalità:

- per dar seguito alle specifiche richieste rivolte al Titolare dall'Utente per il tramite del Sito Web e dei suoi strumenti di comunicazione (email, WhatsApp, telefono e simili);
- per l'eventuale iscrizione alla newsletter e il conseguente invio di comunicazioni informative e commerciali concernenti il settore nel quale opera il Titolare, con apposito consenso prestato dall'Utente; il servizio di invio è gestito tramite la piattaforma Brevo (server nell'Unione Europea), che agisce come responsabile del trattamento;
- per la prenotazione online degli appuntamenti tramite Calendly, che riceve nome, email e telefono al solo fine di fissare l'appuntamento e inviare conferma e promemoria;
- per comunicazioni di natura informativa relative ai servizi dello stesso Titolare, a seguito della richiesta di informazioni;
- per altre finalità accessorie o collegate a quelle sopra indicate e comunque rientranti nell'ambito delle attività del Sito Web.

I dati sanitari eventualmente condivisi in studio non sono trattati tramite questo sito: sono oggetto di informativa e consenso specifici consegnati di persona.

### Base giuridica del trattamento

Il trattamento dei dati personali si fonda sul diritto di informazione, sull'adempimento degli obblighi contrattuali o precontrattuali, ovvero — laddove necessario — sul consenso, prestato mediante la libera e consapevole compilazione degli appositi campi informativi (caselle non preselezionate). Il trattamento si fonda inoltre sul legittimo interesse del Titolare, quale l'esercizio dei propri diritti nel contesto della società dell'informazione e la risposta alle richieste degli Utenti.

### Obbligatorietà del conferimento

Il conferimento dei dati richiesti nei moduli (nome, email) è necessario per erogare il servizio richiesto (iscrizione alla newsletter, prenotazione, risposta a una richiesta). Il conferimento di tutti gli altri dati è facoltativo.

### Eventuali destinatari dei dati personali

I dati potranno essere comunicati a consulenti o a soggetti terzi che operano, anche in nome e per conto del Titolare, per l'evasione delle prestazioni connesse alle finalità indicate nella presente informativa (in particolare Brevo per la newsletter e Calendly per le prenotazioni, quest'ultima con garanzie di trasferimento ai sensi del GDPR). Il sito è ospitato su GitHub Pages (GitHub, Inc.), che può registrare l'indirizzo IP del visitatore nei log del server per motivi di sicurezza.

### Periodo di conservazione

I dati conferiti dall'Interessato saranno conservati fino alla revoca espressa da parte dell'Interessato, mediante richiesta espressa o disiscrizione. I dati di navigazione saranno conservati per il tempo tecnico necessario all'evasione delle funzioni per cui sono stati raccolti.

### Diritti dell'interessato

Ciascun Interessato ha diritto di accesso, di rettifica, di cancellazione (oblio), di limitazione, di ricezione della notifica in caso di rettifica, cancellazione o limitazione, di portabilità, di opposizione e di non essere oggetto di una decisione individuale automatizzata, ai sensi degli artt. da 15 a 22 del GDPR. Tali diritti possono essere esercitati nelle forme e nei termini di cui all'art. 12 GDPR, mediante comunicazione scritta inviata al Titolare via email. Il Titolare renderà risposta adeguata al più presto e comunque entro il termine di 1 mese dalla ricezione della richiesta.

### Diritto di revoca del consenso

È possibile revocare il consenso in qualsiasi momento tramite: invio di una email all'indirizzo del Titolare, infokinesiologia@gmail.com; il link di disiscrizione presente in ogni newsletter; comunicazione espressa presso la sede del Titolare.

### Reclami

Ciascun Interessato ha diritto di proporre reclamo ai sensi degli artt. 77 e seguenti del GDPR a un'autorità di controllo, che per lo Stato italiano è individuata nel Garante per la protezione dei dati personali (www.garanteprivacy.it). Il reclamo fa salve le azioni amministrative e giurisdizionali, che per lo Stato italiano possono proporsi alternativamente al medesimo Garante o al Tribunale competente.

## Informativa cookie

Il presente sito Web, di proprietà di Scuderi Davide, titolare del trattamento, ai sensi e per gli effetti del Regolamento (UE) 2016/679, utilizza cookies e tecnologie analoghe solo nella misura descritta di seguito. La presente informativa fornisce indicazioni su come sono utilizzati i cookies e su come possono essere controllati dall'utente.

### Cosa sono i cookies

I cookies sono piccoli file, contenenti lettere e numeri, che vengono scaricati sul computer o dispositivo mobile dell'utente quando si visita un sito Web, e che vengono re-inviati al sito originario a ogni visita successiva. Consentono a un sito Web di riconoscere il dispositivo dell'utente, ricordare le preferenze e, più in generale, migliorare l'esperienza di navigazione.

In funzione della finalità, si distinguono: **cookies tecnici** (di navigazione o sessione, di funzionalità), utilizzati per permettere la trasmissione di una comunicazione o per erogare un servizio espressamente richiesto dall'utente, il cui utilizzo non richiede il consenso; **cookies analytics**, utilizzati per raccogliere informazioni in forma aggregata sul numero di utenti e su come visitano il sito; **cookies di profilazione**, volti a creare profili relativi all'utente e utilizzabili soltanto con il suo consenso.

### I cookies di questo sito

Questo sito non usa cookies diretti di profilazione né cookies analitici: le sue pagine sono statiche e non installano cookies propri. I caratteri tipografici sono caricati da Google Fonts. I servizi esterni raggiungibili tramite link o pulsanti — Calendly per la prenotazione, WhatsApp, SumUp per i pagamenti dei voucher, Google Maps, Brevo per la newsletter — possono installare propri cookies sulle rispettive pagine, in qualità di autonomi titolari: si rinvia alle loro informative.

### Come controllare o eliminare i cookies

È possibile bloccare o eliminare i cookies seguendo le istruzioni fornite dal browser. Scegliendo di rifiutare i cookies, l'utente potrebbe non essere in grado di utilizzare tutte le funzionalità dei servizi esterni collegati. Istruzioni per i browser più diffusi:

- Chrome — support.google.com/chrome/answer/95647
- Firefox — support.mozilla.org/it/kb/protezione-antitracciamento-avanzata-firefox-desktop
- Edge — support.microsoft.com/it-it/microsoft-edge
- Safari — support.apple.com/it-it/guide/safari/sfri11471/mac

Ultimo aggiornamento: settembre 2026.""",
}

PROBLEMI = [
 {
  'slug': 'mal-di-schiena', 'img': 'schiena.jpg', 'alt': 'Trattamento manuale della schiena nello studio di Modena', 'icon': '🧍', 'title': 'Mal di schiena e lombalgia',
  'teaser': "Blocchi, colpo della strega, una schiena che «si fa sentire» da mesi. Perché il punto che fa male raramente è il colpevole.",
  'eyebrow': 'Schiena e zona lombare',
  'h1': 'Mal di schiena: prima di trattarlo, capiamo da dove arriva',
  'lead': "Una schiena che si blocca, che si irrigidisce al mattino, che non regge più una giornata in piedi o seduta. Il dolore ti dice dove; la valutazione serve a capire perché — e a scegliere l'intervento giusto per te, non per il sintomo.",
  'topics': ['schiena'],
  'body': """## Come si presenta

Le storie sono diverse ma si somigliano: un blocco improvviso chinandosi (il classico «colpo della strega»); una rigidità che al mattino ci mette mezz'ora a sciogliersi; un dolore sordo che compare dopo un'ora seduti o in piedi; una schiena che «si fa sentire» da mesi e che hai imparato a proteggere, evitando di sollevare, di piegarti, di fare sport.

## Perché lo stesso sintomo può avere origini diverse

La colonna non lavora da sola: sta in mezzo a un bacino, due anche, un diaframma che respira e un dorso che ruota. Quando uno di questi anelli fa meno del dovuto — un'anca che ha perso rotazione, un diaframma che non scende, un dorso irrigidito dalla scrivania — il carico non sparisce: se lo prende la zona lombare, che regge finché può. Poi fa male. Ma non è lei il colpevole: è quella che ha retto più a lungo.

Ci sono anche schiene che fanno male perché sono state messe in pensione: dopo un episodio si smette di caricarle, i tessuti si indeboliscono, la soglia dell'allarme si abbassa, e sollevare la cassa dell'acqua diventa un problema. Stessa parola, «mal di schiena», ma qui l'intervento è quasi l'opposto: non calmare, ma ricostruire tolleranza un po' alla volta.

## Cosa guardo alla prima valutazione

Come ti pieghi e come ti rialzi, quanto ruotano le anche, quanto collabora il dorso, come respiri sotto sforzo, se un lato lavora come l'altro. Test muscolari e di movimento che ripeteremo a fine seduta. Ti chiedo di vecchi traumi, interventi, cicatrici: una cicatrice sull'addome può c'entrare con una schiena che si blocca sempre dallo stesso lato.

## Come scelgo l'intervento

Se prevale uno spasmo di difesa, la prima cosa è calmare: lavoro manuale, respiro, movimento piccolo e frequente. Se prevale una zona vicina che non collabora, lavoro lì, e la schiena spesso si scarica da sola. Se prevale la paura di muoversi e la perdita di tolleranza, l'intervento è un piano di carico progressivo con un criterio semplice: fastidio fino a 3 su 10 va bene, e la mattina dopo non devi stare peggio.

## Cosa cambia, e come lo misuriamo

Rifacciamo gli stessi test della prima ora. Il criterio non è solo «come ti senti», ma cosa riesci a fare: piegarti, sollevare, stare seduto più a lungo. Nella maggior parte degli episodi acuti il miglioramento arriva in pochi giorni; nei problemi che durano da mesi servono di norma alcuni incontri, e te lo dico dall'inizio.""",
  'red_flags': """Vai prima dal medico, non da me, se insieme al mal di schiena compaiono debolezza alle gambe che peggiora, formicolio in entrambe le gambe, difficoltà a controllare intestino o vescica, febbre, un dolore che non cambia con la posizione o che ti sveglia di notte, oppure se il dolore è comparso dopo un trauma importante. Sono situazioni rare, ma non si aspetta.""",
 },
 {
  'slug': 'cervicale', 'img': 'cervicale.jpg', 'alt': 'Valutazione e trattamento del collo in studio', 'icon': '💆', 'title': 'Cervicale, collo e mal di testa',
  'teaser': "Quei due cordoni duri sopra le spalle, il mal di testa a fine giornata. Perché il massaggio dà sollievo ma non dura.",
  'eyebrow': 'Collo, spalle alte e testa',
  'h1': 'Cervicale: il collo è dove si sente, non sempre da dove arriva',
  'lead': "Collo rigido, spalle che tirano, mal di testa che comincia nel pomeriggio, mani che si addormentano di notte. Prima di trattare il collo, capiamo cosa lo sta facendo lavorare per due.",
  'topics': ['cervicale', 'mandibola'],
  'body': """## Come si presenta

«Ho la cervicale» è la frase con cui arrivano in tanti. Dietro ci sono cose diverse: due cordoni duri sopra le spalle che nessun massaggio scioglie per più di un giorno; una rigidità che limita la rotazione quando guidi; un mal di testa a cerchio che comincia verso le quattro del pomeriggio; formicolii alla mano che compaiono di notte; una mascella che al risveglio è stanca come dopo aver masticato per ore.

## Perché il collo lavora per due

La testa pesa quattro o cinque chili. A reggerla non c'è solo il collo: sotto ci sono le scapole e la parte alta della schiena, che fanno da base. Se quella base si irrigidisce — dopo anni di scrivania capita spesso — il collo si ritrova a fare due mestieri: reggere la testa e compensare quello che il dorso non fa più. I muscoli sopra le spalle diventano duri perché stanno lavorando, non per capriccio. Ecco perché il massaggio dà sollievo ma non dura: togli la tensione al muscolo che fa gli straordinari, ma il lavoro da fare resta lo stesso.

C'è poi la mandibola, che stringi senza accorgertene quando sei concentrato o mentre dormi. Il muscolo che la chiude è tra i più potenti del corpo per la sua dimensione, e quando lavora tutta la notte la tensione sale alle tempie e scende ai muscoli sotto la nuca. Certi fastidi al collo del risveglio hanno origine trenta centimetri più avanti.

## Cosa guardo alla prima valutazione

Quanto ruota il dorso con le braccia incrociate, quanto si apre la parte alta della schiena, come stanno le scapole, come respiri (un respiro alto e corto tiene collo e spalle in tensione), la posizione di riposo della mandibola, e se i formicolii cambiano muovendo la testa, il braccio o il polso. Non tutti i colli hanno sotto un dorso rigido: a volte il problema è davvero locale. La valutazione serve a distinguerlo, non a confermare una teoria.

## Come scelgo l'intervento

Se la base non collabora, lavoro lì: mobilità del dorso, scapole, respiro, e il collo si alleggerisce di conseguenza. Se la mandibola stringe, la tratto e ti insegno la posizione di riposo: labbra chiuse, denti staccati, lingua al palato. Se è locale, intervengo sul collo, con manualità e movimento. In tutti i casi la cosa che aiuta di più fuori dallo studio non è un esercizio: è alzarsi trenta secondi ogni quarantacinque minuti. Il collo non si stanca delle posizioni, si stanca dell'immobilità.

## Cosa cambia, e come lo misuriamo

Rotazione, apertura del dorso, quante ore alla scrivania prima che il collo si faccia sentire, quanti giorni dura il sollievo. Se dopo il primo intervento il beneficio tiene più a lungo di prima, siamo sulla strada giusta; se non tiene, cambiamo ipotesi, non aumentiamo la dose.""",
  'red_flags': """Fatti vedere da un medico, non da me, se il mal di testa è comparso all'improvviso ed è il più forte della tua vita, se peggiora di giorno in giorno, se arriva con febbre alta e collo rigido, se dà disturbi alla vista o alla parola; oppure se il formicolio alla mano non passa più nemmeno di giorno, se compare una debolezza vera nella presa, o se un dolore al collo segue un trauma o un incidente.""",
 },
 {
  'slug': 'spalla', 'img': 'spalla.jpg', 'alt': 'Test di elevazione del braccio durante la valutazione della spalla', 'icon': '🏋️', 'title': 'Dolore alla spalla',
  'teaser': "Non riesci ad allacciare il reggiseno, a dormire su quel lato, a sollevare il braccio. La spalla è mobile: per questo paga per gli altri.",
  'eyebrow': 'Spalla e braccio',
  'h1': 'Dolore alla spalla: l\'articolazione più mobile del corpo, e la più facile da caricare male',
  'lead': "Un braccio che non sale, una fitta quando allacci qualcosa dietro la schiena, una notte su quel lato che non riesci a fare. Prima di trattare la spalla, capiamo cosa le chiede di lavorare più del dovuto.",
  'topics': ['spalla', 'cervicale'],
  'body': """## Come si presenta

Una fitta quando sollevi il braccio oltre una certa altezza o quando lo porti dietro la schiena. Un dolore che compare di notte, dormendo su quel lato. Una spalla che «scricchiola» o che sembra più debole dell'altra. Una rigidità che è arrivata piano, in mesi, dopo un periodo di sforzi ripetuti, di lavoro al computer o dopo un trauma banale che sembrava passato.

## Perché la spalla paga per gli altri

La spalla è l'articolazione più mobile del corpo, e la mobilità ha un prezzo: non ha una struttura ossea che la tenga, si regge sui muscoli e sul modo in cui la scapola scivola sulla gabbia toracica. Se la scapola non si muove bene — perché il dorso è rigido, perché le spalle sono chiuse in avanti, perché il respiro resta alto nel petto — il braccio sale «tirando» sull'articolazione invece di accompagnarla. Ripetuto migliaia di volte, quel modo di salire irrita i tendini. Trattare solo il punto che fa male dà sollievo, ma il gesto che lo irrita resta lo stesso.

Lo stesso vale per il collo: spalla e cervicale si influenzano, e un dolore che scende lungo il braccio può partire da entrambi. Distinguere le due cose è una parte importante della valutazione.

## Cosa guardo alla prima valutazione

Come sale il braccio e cosa fa la scapola mentre sale; la mobilità del dorso in rotazione ed estensione; la forza dei muscoli che stabilizzano la spalla, confrontata con l'altro lato; se il dolore cambia muovendo il collo; come respiri. Ti chiedo com'è cominciato, cosa hai già fatto, e se hai esami recenti li guardo insieme a te per capire cosa è già stato escluso.

## Come scelgo l'intervento

Se la scapola non collabora, lavoro sul dorso, sui muscoli che la muovono e sul respiro, e la spalla spesso ritrova spazio da sola. Se i tendini sono irritati da un gesto ripetuto, l'intervento è un lavoro manuale per calmare e un piano di carico progressivo per renderli di nuovo tolleranti: fermarsi del tutto non li fa guarire, li indebolisce. Se il dolore viene dal collo, lavoro lì. In tutti i casi porti a casa pochi esercizi, con un criterio chiaro: un fastidio fino a 3 su 10 durante l'esercizio va bene, la mattina dopo non devi stare peggio.

## Cosa cambia, e come lo misuriamo

Quanto sale il braccio senza dolore, se riesci a dormire su quel lato, quanto peso regge quel gesto. Sono misure che rifacciamo ogni volta: la spalla è un'articolazione che migliora per gradi, e vale la pena vederli.""",
  'red_flags': """Vai prima dal medico se il dolore è comparso dopo una caduta o un trauma e non riesci a muovere il braccio, se la spalla è gonfia, calda o deformata, se la debolezza è improvvisa e marcata, se hai febbre, o se il dolore alla spalla sinistra si accompagna a oppressione al petto, affanno o sudorazione: in quel caso chiama subito il 118.""",
 },
 {
  'slug': 'postura', 'img': 'postura.jpg', 'alt': 'Osservazione della postura in piedi durante la valutazione', 'icon': '🚶', 'title': 'Postura e tensioni da scrivania',
  'teaser': "Non esiste la postura perfetta: esiste un corpo che regge bene le tue giornate. Valutazione dalla testa ai piedi.",
  'eyebrow': 'Postura, sedentarietà e stress',
  'h1': 'Postura: non cerco quella perfetta, cerco un corpo che regge le tue giornate',
  'lead': "Spalle chiuse, testa in avanti, tensioni che si accumulano ora dopo ora davanti a uno schermo, respiro corto quando sei sotto pressione. Prima di «correggere» la postura, capiamo cosa il tuo corpo sta compensando.",
  'topics': ['postura', 'stress', 'piede'],
  'body': """## Come si presenta

Arrivi a sera con le spalle all'altezza delle orecchie. Ti dicono che stai «storto», o te ne accorgi in una foto. Hai tensioni diffuse che si spostano: oggi il collo, domani la zona lombare, dopodomani il mal di testa. Il respiro resta alto e corto, soprattutto nei periodi di stress. Le gambe a fine giornata sono pesanti. Nessun dolore forte, ma un corpo che non si sente mai davvero a posto.

## Perché non esiste la postura perfetta

La postura non è una posizione da tenere: è il modo in cui il corpo si organizza per fare quello che gli chiedi. Un corpo che sta otto ore seduto si adatta a stare seduto: il dorso si arrotonda, le anche si accorciano, il diaframma perde escursione, il collo si porta in avanti. Non è un difetto da raddrizzare con la forza di volontà (nessuno riesce a «stare dritto» per più di dieci minuti): è un adattamento, e si cambia dando al corpo stimoli diversi.

C'è poi un legame che spesso sorprende: quando sei sotto pressione il diaframma si irrigidisce, il respiro si accorcia, resta nel petto. Un respiro corto dice al cervello che c'è pericolo anche quando non c'è, e un corpo in allerta tiene tutto in tensione: collo, spalle, mandibola, schiena. Il diaframma è un muscolo: si può trattare e si può allenare.

## Cosa guardo alla prima valutazione

Ti guardo dalla testa ai piedi, in piedi e in movimento: come appoggi, come ruotano le anche, quanto si apre il dorso, dove sta la testa rispetto alle spalle, come respiri a riposo e sotto sforzo. Test di mobilità e di forza, confrontando i due lati. Non cerco lo «storto»: cerco gli anelli della catena che fanno meno del dovuto e quelli che stanno lavorando al posto loro.

## Come scelgo l'intervento

Se il dorso e il diaframma sono il collo di bottiglia, lavoro lì, manualmente e con il respiro, e le tensioni a distanza spesso calano da sole. Se prevale la perdita di forza e di tolleranza, l'intervento è un piano di pochi esercizi, progressivi, da fare a casa. Se prevale l'immobilità, la cosa più utile non è un esercizio: è alzarsi trenta secondi ogni quarantacinque minuti. In tutti i casi non ti do una lista di venti esercizi: ne scegliamo due o tre, e li verifichiamo.

## Cosa cambia, e come lo misuriamo

Apertura del dorso, escursione del respiro, quante ore di scrivania prima che qualcosa si faccia sentire, quanto tempo dura il beneficio. Rifacciamo il test tra due e quattro settimane: il piano si aggiorna con i progressi, non resta uguale per mesi.""",
  'red_flags': """Se le tensioni si accompagnano a dolore toracico, affanno a riposo, vertigini, perdita di peso senza motivo o disturbi che peggiorano rapidamente, parlane prima con il tuo medico. Se il respiro corto è presente anche a riposo da molto tempo, un controllo medico viene prima di qualsiasi lavoro sul diaframma.""",
 },
]
