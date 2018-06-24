# post-generation is tool, which automatically generates text based on scrapped text.

Software consists of two parts:
* Corpus gathering
  * URL - https://www.delfi.lt/rss/
  * output file - corpus.txt
* Post generation

Text gathering is performed using beautifulsoup4.  
Post text generation is performed using Markov Chains (markovify).

### Corpus generation
```
usage: download_corpus.py [-h] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Path of text file to output downloaded rss index text

```

Command example:
```
python download_corpus.py
```

### Post generation
```
python generate_text.py
```

## Generated post examples
* Apie patį incidentą nieko nežino ir užsienio šalių ambasadoms išplatintas elektroninis laiškas su melaginga naujiena platintas adresatams valstybiniame sektoriuje.
* Jis patikino, kad informacija apie „Avia Solutions Group“ veikla, nei su jos advokatu agentūrai „Reuters“ susisiekti nepavyko.
* Ne paslaptis, kad būsimojo Rusijos prezidento rinkimų ir paties V. Putino rinkimų štabo ausis Maskvoje.
* Galiausiai neslepiama, kad pagal suplanuotas operacijas ir jų dinamiką, pratybos „Kardo kirtis“ ir iš anksto sunkiau prognozuojamų dislokavimo terminų.
* Daugiausiai kliuvo būtent lyderės vaidmenį Baltijos šalių vadovų tuo metu iš viso buvo galima surinkti 60 taškų, tai yra niekšybė.