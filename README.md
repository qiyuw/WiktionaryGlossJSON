# WiktionaryGlossJSON
Extract glosses of words from [Wiktionary](https://en.wiktionary.org/wiki/Wiktionary:Main_Page) and dump them into a JSON file.

## Overview
Wiktionary dump file could be parsed by tools like [Wiktextract](https://github.com/tatuylonen/wiktextract). Processes above may take hours for a complete Wiktionary dump file, depending on your computing power, as the large size of raw data. Hence, here providing a trimmed JSON file which only preserves the glosses of words.

## Usage
The JSON could be loaded as a python dict like `{word: list of glosses}`. Each value is a list of glosses of the word.  

A complete pasrsed JSON for the latest version of Wiktionary at **March 23, 2020** is provided. **You can download it (`wikt.gloss.json`) at this repo.**

If you want to parse another version of Wiktionary, check [Wiktextract](https://github.com/tatuylonen/wiktextract) and `process.py`.

* Extract from Wiktionary dump file `enwiktionary-<date>-pages-articles.xml.bz2` ([download here](https://dumps.wikimedia.org/enwiktionary/)) by [Wiktextract](https://github.com/tatuylonen/wiktextract), you will get a JSON file like `wikt.words` here.
* Run the script `python process.py ./wikt.words` to get the glosses of words and dump them into a JSON. Other information of words rather than glosses can be easily obtained by modifying the method `get_gloss` in `process.py`.