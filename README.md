# Zeit Online Webscrapper

## Details

Get Articles and comments from zeitonline. API and Parser in a Docker container.

## How to use
**Use local**
```javascript
// setup python virtual enviorment
python3 -m venv /path/to/new/virtual/environment
// activate venv
source venv/bin/activate
// install packages
pip install -r requirements.txt

// start localhost with uvicorn
uvicorn api:app --port 8080 --reload
// open browser -> http://127.0.0.1:8080/docs
```

**Start Docker**
```javascript
// build container
docker build -t news-scraper .  
// start container
docker run -it --rm -p 8080:8080 news-scraper
// open browser -> http://0.0.0.0:8080/docs   
```

**FastAPI Info**
information can be found on the [fastapi website](https://fastapi.tiangolo.com/) as well as the [github project](https://github.com/tiangolo/fastapi)
```javascript
--reload // updates server resources when code changes are made

// you can specify also a host with --host 0.0.0.0
uvicorn api:app --host 0.0.0.0 --port 8080
```

## Request API
There are multiple ways to send requests to the api

**Articles**
zeit-online url example: https://www.zeit.de/politik/ausland/2020-03/donald-trump-coronavirus-wirtschaft-usa-ostern

1. '/article/{category}/{sub_category}/{title}/{date}'
    - category = politik
    - sub_category = ausland
    - title = donald-trump-coronavirus-wirtschaft-usa-ostern
    - date = 2020-03
2. '/article/{url}'
    - url = "politik\ausland\2020-03\donald-trump-coronavirus-wirtschaft-usa-ostern"
3. '/test'

**Comments**
1. '/comments/{category}/{sub_category}/{title}/{date}'
    - category = politik
    - sub_category = ausland
    - title = donald-trump-coronavirus-wirtschaft-usa-ostern
    - date = 2020-03
2. '/comments/{url}'
    - url = "politik\ausland\2020-03\donald-trump-coronavirus-wirtschaft-usa-ostern"
    
**News**
1. '/news'

## Article Response [Donald Trump Article](https://www.zeit.de/politik/ausland/2020-03/donald-trump-coronavirus-wirtschaft-usa-ostern)
```javascript
// article information
{
  "title": "Gefaehrlicher Eigensinn",
  "sub_title": "Donald Trump",
  "summary": "Schon in weniger als drei Wochen will Donald Trump die US-Wirtschaft wieder hochfahren. Der Praesident gefaehrdet Menschenleben, nur um seine Wiederwahl zu sichern.",
  "release": "24. Maerz 2020, 21:36 Uhr",
  "author": "Joerg Wimalasena",
  "comments_count": "779 Kommentare",
  "article_text": "Donald Trump glaubt an sein persoenliches Osterwunder. Wie einst Jesus Christus am dritten Tag nach seinem Tod auferstand, soll auch die US-amerikanische Wirtschaft trotz Corona-Pandemie schnell wieder zurueckkommen. \"Ich wuerde mich freuen, wenn das Land an Ostern wieder geoeffnet ist\", sagte der US-Praesident in einem TV-Interview seines Haussenders Fox News, bei dem auch Zuschauende Fragen stellen konnten. Wobei geoeffnet offenbar heisst, dass Unternehmen wieder den Betrieb aufnehmen und die Menschen ihren Jobs nachgehen sollen. \"Wir koennen uns fuenfmal am Tag die Haende waschen und aufs Haendeschuetteln verzichten, aber wir muessen wieder zurueck an die Arbeit\", sagte Trump im Rosengarten des Weissen Hauses.Der 73-Jaehrige hat waehrend seiner Amtszeit nicht zum ersten Mal Weitsicht und Gemeinsinn vermissen lassen, doch diese Entscheidung – sofern er sie tatsaechlich durchzusetzen vermag – waere verheerend. Sollte die Wirtschaft schon in etwas mehr als zwei Wochen wieder hochfahren, ergaeben sich daraus erhebliche Gefahren. Menschen gingen wieder zur Arbeit und wuerden sich in grosser Zahl gegenseitig mit dem Coronavirus anstecken.Die USA haben allerdings schon jetzt die drittmeisten Infektionsfaelle weltweit. Vor allem in New York explodieren die Zahlen geradezu und auch im Rest des Landes werden laut Berechnungen der Columbia University die Corona-Faelle auf bis zu 500.000 im Mai in die Hoehe schnellen. In vielen Bundesstaaten koennte die Wachstumskurve erst im Juni ihren Scheitelpunkt erreichen – Ostersonntag ist aber schon am 12. April.Der derzeitige Stillstand des oeffentlichen Lebens in vielen Teilen des Landes muesste also noch wochenlang aufrechterhalten werden, um den Verlauf der Pandemie ueber einen moeglichst langen Zeitraum zu strecken, damit die Krankenhaeuser des Landes alle Patientinnen und Patienten auch tatsaechlich versorgen und behandeln koennen. Das ohnehin dysfunktionale US-Gesundheitssystem droht unter den Fallzahlen zusammenzubrechen, wenn die Massnahmen zum Abstandhalten und die Schliessung der Betriebe in vielen Staaten nicht durchgehalten werden. Mit hoher Wahrscheinlichkeit werden mehr Menschen sterben, wenn Donald Trump mit seinem Vorhaben ernst macht.Doch dem Praesidenten und seinen Verbuendeten in der republikanischen Partei ist das offenbar egal. Schon seit Montag testen sie die Reaktionen der Öffentlichkeit auf einen derart weitreichenden Schritt. Dan Patrick, stellvertretender Gouverneur von Texas, sagte – natuerlich bei Fox News –, dass er seinen eigenen Tod durch Corona in Kauf nehmen wuerde, um \"das Amerika, das ganz Amerika liebt\" zu erhalten. Trump selbst twitterte: \"Wir koennen nicht zulassen, dass das Heilmittel schaedlicher ist als das Problem selbst.\"Am Dienstag fuehlte der US-Praesident sich offenkundig sicher genug, um den Vorstoss offiziell zu verkuenden. Sein Motiv ist simpel. Trump will eine zweite Amtszeit und sieht in einer florierenden Wirtschaft sein bestes Argument fuer die Wiederwahl. Die Opfer dieses Eigensinns sind ihm offenbar egal. Bei seinem TV-Auftritt versuchte er vor einem Millionenpublikum sogar, die Todesrate der Corona-Pandemie kleinzureden. Er rechne mit weniger als einem Prozent, \"substanziell weniger\", als man ihm zuvor mitgeteilt haette. Und wegen Verkehrs- und normalen Grippetoten fahre man ja auch nicht die Wirtschaft herunter.Das Signal dieser Worte ist fatal. Überall im Land kaempfen Behoerden und Landesregierungen um Akzeptanz fuer die Einschraenkungen des oeffentlichen Lebens. Wenn der US-Praesident nun billigt, Betriebe wieder zu oeffnen, und die Todesgefahr herunterspielt, koennte das die lokal muehsam erarbeitete Sensibilitaet der Bevoelkerung fuer die Bedrohung der Pandemie wieder untergraben. Unnoetige Infektionen waeren die Folge.Traurigerweise koennte Trump mit seiner Corona-Verharmlosung den Nerv einiger Waehlerinnen treffen. Die Federal Reserve in St. Louis rechnet wegen des aktuellen Wirtschaftsstillstands mit einer Arbeitslosenquote von bis zu 30 Prozent. In den USA gibt es auf Bundesebene keine langfristige Absicherung fuer Erwerbslose. Das vom Kongress verabschiedete Corona-Hilfspaket fuer Arbeitnehmer und Selbststaendige ist lueckenhaft, ein weiteres Billionenpaket haengt im Senat fest. Wer seine Arbeit verliert, dessen Existenz ist moeglicherweise mehr vom Stillstand des oeffentlichen Lebens bedroht als von Corona. Trump nutzt diese Ängste zynisch aus.Doch auch ausserhalb der USA duerfte Trumps Vorstoss schwerwiegende Folgen haben. Corona-Skeptiker in anderen Laendern – wie der brasilianische Praesident Jair Bolsonaro – duerften sich durch das Vorgehen des Praesidenten bestaetigt fuehlen. Die Regierungen koennten sich dazu gezwungen sehen, ebenfalls verfrueht die eigene Wirtschaft wieder hochzufahren. Nun bleibt nur noch die Hoffnung, dass Trump seine Entscheidung noch einmal ueberdenkt. Es waere nicht das erste Mal, dass er eine Ankuendigung nach politischem Widerstand revidiert. Dem Land, seinen Buergern und vielleicht der ganzen Welt taete er damit einen grossen Gefallen."
}
```
Article response positions: 
- title: str
- sub_title: str
- summary: str
- release: str
- source: str
- author: str
- comments_count: str
- article_text: str

Article vary from one and another. Empty positions will be ignored and will not be listed in the response (like source: "" in the example above)

## Comments Response
```javascript
// work in progress
```
Comments response positions: 
- todo: str

## News Response
```javascript
{
  "news_count": "51",
  "news_references": [
   {
      "link": "https://www.zeit.de/politik/ausland/2020-03/praesidentschaftswahl-polen-pis-coronavirus-pandemie",
      "link_contents": "politik\\ausland\\2020-03\\praesidentschaftswahl-polen-pis-coronavirus-pandemie",
      "news_title": "Präsidentschaftswahl in Polen - Der Wahl-Kampf"
   },
   {
      "link": "https://www.zeit.de/politik/ausland/2020-03/viktor-orban-ungarn-notstand-coronavirus-eu",
      "link_contents": "politik\\ausland\\2020-03\\viktor-orban-ungarn-notstand-coronavirus-eu",
      "news_title": "Viktor Orbán - Grüne und SPD fordern zum Eingreifen in Ungarn auf"
   },
   {...}
   ]
}
```
News response positions: 
- news_count: str
- news_references: [
    - link: str
    - link_contents: str
    - news_title: str
]

Test for yourself by following the steps under **How to use -> Use local**
## Future plans
- other websites (spiegel-online, faz)
- get article comments as well
- fetch articles from main page 