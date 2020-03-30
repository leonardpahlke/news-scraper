# Zeit Online Webscrapper

## Details

Docker Container Webscrapper for Zeit Online. Get article and comments information.

## How to use

```
# build container
docker build -t news-scraper .  
# start container
docker run -it --rm -p 8080:8080 news-scraper  

# or execute ./zeitonline/main.py -> run/4 
```

**run(category, sub_category, title, date)**
(If date parameter is not given, ignore it)

ZeitOnline url example: https://www.zeit.de/politik/ausland/2020-03/donald-trump-coronavirus-wirtschaft-usa-ostern

1. category = politik
2. sub_category = ausland
3. title = donald-trump-coronavirus-wirtschaft-usa-ostern
4. date = 2020-03

## Response [Donald Trump Article](https://www.zeit.de/politik/ausland/2020-03/donald-trump-coronavirus-wirtschaft-usa-ostern)
empty positions will be ignored and are **missing** in the response (like source: "" in this example)
```
{
  title: "Gefährlicher Eigensinn",
  sub_title: "Donald Trump",
  summary: "Schon in weniger als drei Wochen will Donald Trump die US-Wirtschaft wieder hochfahren. Der Präsident gefährdet Menschenleben, nur um seine Wiederwahl zu sichern.",
  release: "24. März 2020, 21:36 Uhr",
  author:  "Jörg Wimalasena",
  comments_count: "44 Kommentare",
  article_text: "Donald Trump glaubt an sein persönliches Osterwunder. Wie einst Jesus Christus am dritten Tag nach seinem Tod auferstand, soll auch die US-amerikanische Wirtschaft   trotz Corona-Pandemie schnell wieder zurückkommen. "Ich würde mich freuen, wenn das Land an Ostern wieder geöffnet ist", sagte der US-Präsident in einem TV-Interview seines Haussenders Fox News, bei dem auch Zuschauer Fragen stellen konnten. ... Es wäre nicht das erste Mal, dass er eine Ankündigung nach politischem Widerstand revidiert. Dem Land, seinen Bürgern und vielleicht der ganzen Welt täte er damit einen großen Gefallen."
}
```

## Future plans
other websites

get article comments as well
