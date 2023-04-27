# OpenAPI fine-tuning example

Scrape some pages from the TechMiners homepage and fine-tune the OpenAPI index.

## Setup

Copy `.env.example` to `.env` and add your OPENAI_API_KEY.

## Running

``` bash
# install dependencies
pip install -r requirements.txt
# create index file
python finetune.py
# query the index
python query.py
```