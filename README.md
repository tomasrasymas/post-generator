# post-generation is tool, which automatically generates text based on scrapped text.

Software consists on two parts:
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

