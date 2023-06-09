# SEOMATOR - tool list

SEOMATOR is a website that provides some tools for SEO testing.
This is the list with all of them with some notes about their usability.

### SEARCH ENGINE
-   ~~Google SERP~~: → **richiede keyword, quindi non generico**
        Richiede come input aggiuntivi una keyword di ricerca e lo Stato di ricerca (?).
        Restituisce il rank dell’url nei risultati Google rispetto a questi input e il PA e DA dei vari siti nel risultato.  
-   ~~Bing SERP~~: → **come il precedente**
        uguale al tool precedente, ma ricerca su Bing
-   ~~Top Search Queries~~: → **per indicare migliori query (?) - non sembra affidabile**
        Richiede come input aggiuntivo lo Stato di ricerca.
        Restituisce le principali query di ricerca col quale il sito in questione esce nei primi 98 (?) risultati, con annesse rank, e altri dati.
-   ~~Indexed Pages~~: → **non so neanche cosa fa**
        non so…
-   Robots.txt: → **dipende se è utile se il file non c’è/non è corretto**
        Restituisce le regole per specifici crawlers date dal robots.txt file, le sitemaps indicate e il testo di robots.txt.
        Dal sito viene specificato: “Robots.txt Tester analyzes the syntax and content of the robots.txt file and checks for any errors or warnings 
        that could prevent search engines from accessing important pages or content. 
        The tool provides a detailed report of the file's structure, syntax, and directives, highlighting any issues that need to be addressed.”
        → servirebbe test con robots.txt sbagliati/mancanti
-   Sitemap: → **potrebbe essere utile per verificare esistenza file**
        Restituisce la posizione dei file xml relativi a sitemap, indicando anche la loro effettiva esistenza.
        Da sito:”...can quickly identify if a website has an XML sitemap, what type of information it contains, and where it is located.”
-   ~~Submit Sitemaps~~: → **non so cosa faccia ma sembra inutile**
        Indica un bottone “submit” per sitemap che non so minimamente cosa faccia…

### BACKLINKS
-   High Quality Backlinks: → **utile per statistiche backlinks**
        Indica il numero totale di backlinks, indicando quanti di questi sono unici, quali puntano solo alla homepage e quanti hanno il tag “nofollow”.
        Inoltre restituisce un listone dei “migliori” backlink, indicando la provenieza, PA, DA e data scoperta backlink.
-   ~~New Backlinks~~: → **informazione non utile**
        Restituisce una lista dei backlink scoperti più di recente (in ordine cronologico quindi)
-   Poor Backlinks: → **potrebbe essere utile averne il numero**
        Restituisce una lista dei backlink provenienti da siti “poco affidabili” che potrebbero peggiorare il SEO del sito.
-   ~~Top Referrers~~: → **informazione non utile**
        Restituisce una lista dei siti in ordine di chi ha maggior backlink verso il sito in questione, con annesso numero di “dofollow”, DA e data scoperta.
-   Check Domain Authority: → **punteggio utile come statistica**
        Restituisce la DA del sito (punteggio in scala da 1 a 100).
-   Check Page Authority: → **come il precedente ma per pagina singola**
        Restituisce la PA di una pagina del sito, “/” default, ma può essere indicata qualsiasi (punteggio in scala da 1 a 100).

### TEST
-   Crawlability Test: → **informazioni povere ma utili**
        Indica se una pagina del sito (che può essere specificata, “/” default) è crawlable o meno e indicizzabile o meno, 
        secondo le regole di robots.txt (di cui riporta nuovamente il raw text), per Google e Bing.
-   ~~Mobile Support Test~~: → **utile ma forse lo ha lighthouse**
        Valuta se il sito supporta i dispositivi mobile e ne indica gli elementi che lo fanno (meta tag, css, ecc…).
-   Headers: → **utile se è necessario controllare presenza specifici headers**
        Elenca (con anche il raw text) i dati presenti nell’header della richiesta HTTP. 
        (Indica anche se la pagina ridirige ?)
-   ~~Speed Test~~: → **genericamente utile, ma probabilmente info anche da lighthouse**
        Effettua un test di velocità di una richiesta (selezionando una Regione di partenza) e ne restituisce il risultato: 
        indica un punteggio, con annesso tempo di caricamento, peso pagina e numero richieste, inoltre indica numero di responsi (200, 404, ecc…), 
        da quali elementi è formata la pagina (scripts, doc, ecc…) e il loro peso e numero richieste.

### CONTENT
-   Link Analysis: → **utile se indica anche link rotti, altrimenti no**
        Il risultato può essere valutato per una qualsiasi pagina del sito (“/” default).
        Restituisce dati relativi ai link presenti nella pagina (numero totale, esterni, interni e nofollow) e li elenca in una tabella.
-   ~~Keyword Density~~: → **potrebbe essere utile, ma un po’ generico**
        Restuisce (per una pagina specifica, “/” default) titolo e descrizione meta tag con contenuto e un elenco delle keyword presenti nella pagina, 
        con numero utilizzi, se sono presenti nel titolo/descrizione e il loro peso per la ricerca.
-   Extract Meta Tags: → **utile se è necessario controllare presenza specifici meta tags**
        Elenca tutti i meta tags presenti nel’head HTML di una pagina del sito (“/” default), e se sono utilizzati da Google/Bing.

### RESEARCH
-   ~~Keyword Research~~: → **inutile ai fini di monitoraggio**
        Necessita di input aggiuntivi quali keyword/frase e regione di ricerca.
        Restituisce una lista contenente keyword/frasi affini con il loro peso e volume di ricerca.
-   ~~Competition~~: → **specifico per query con keyword/frasi**
        Richiede come input aggiuntivi keyword/frase e regione di ricerca.
        Restituisce i risultati di una ricerca con quegli input (con dati quali DA, PA, backlinks e i loro dofollow, e domains, relativi ai vari siti trovati) 
        e indica la posizione del sito in questo rank. 
        Valuta la competitività del sito rispetto a determinate queries.
