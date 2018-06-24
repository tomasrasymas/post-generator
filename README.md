# post-generation is tool, which automatically generates text based on scrapped text.

Software consists on two parts:
* Corpus gathering
* Post generation

Text gathering is performed using beautifulsoup4.
Post text generation is performed using Markov Chains (markovify).

### Corpus generation
```
usage: download_corpus.py [-h] [-u URL] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL of delfi.lt rss item index to generate text file
  -o OUTPUT, --output OUTPUT
                        Path of text file to output downloaded rss index text
```

Command example:
```
python rabbitmq_to_http_proxy.py -u 'amqp://john:john1234@rabbit.john.com:5672/johnvhost?heartbeat=10' -e clients -q prices -r '*.prices' -v -a http://127.0.0.1:5000/api/prices -p 100
```