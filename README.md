# ampelmann
Corpus search engine, out of necessity

ampelmann is a corpus search engine tailor-made for the case studies in my PhD research. The long-term goal of this program is to create specialised datasets from scratch (i.e. from corpus source files).

ampelmann does *not* aim to be able to create datasets for every single research use case. However, the interface it provides can be useful for other researchers to extend the current functionality for their own case studies.

## Installing ampelmann

### Preparation

These instructions only have to be run once.

1. Download and install [Python](https://www.python.org/).
2. `git clone https://github.com/AntheSevenants/ampelmann.git`,   
    or download and unzip [this archive](https://github.com/AntheSevenants/ampelmann/archive/refs/heads/main.zip).
3. Open a terminal window. Navigate to the `ampelmann` directory:  
    `cd ampelmann`
4. Create a new virtual environment:  
    `python -m venv venv` or `python3 -m venv venv`
5. Activate the virtual environment:  
    `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (unix)
6. Install all dependencies:  
    `pip install -r requirements.txt`

### Running

These instructions need to be followed every time you want to use the ampelmann program.

1. Open a terminal window. Navigate to the `ampelmann` directory:  
    `cd ampelmann`
2. Activate the virtual environment:  
    `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (unix)
3. You can now run any of the case study scripts detailed below.

## Red and green word order in Dutch

ampelmann has built-in functionality which can filter red and green word order in Dutch subordinate sentences. Currently, you need three files for its functionality. Your sentences should already be sorted into potential "red" sentences and potential "green" sentences. For example:

**red-sentences.txt**
```
Ik weet dat hij een groene kikker heeft gezien.
Weet jij waar chocomelk is ontstaan?
```

**green-sentences.txt**
```
Ik weet dat hij een groene kikker gezien heeft.
Weet jij waar chocomelk ontstaan is?
```

You also need a "closed set" of items which will definitely appear in all your desired examples. The [flashtext](https://arxiv.org/abs/1711.00046) algorithm (thanks, [@lemontheme](https://github.com/lemontheme)) is used to quickly filter all sentences which are *definitely* not part of that set. In the case of the red and the green order, this file should include all possible auxiliaries which allow for a red and green alternation. This file is already included in the repository under [data/RoodGroen/closed_items.json](https://github.com/AntheSevenants/ampelmann/blob/main/data/RoodGroen/closed_items.json).

To recreate my dataset, run the following command. Make sure your virtual environment is enabled!

```bash
python3 RoodGroen.py "data/RoodGroen/closed_items.json" "data/RoodGroen/WRPPB-rood.txt" "data/RoodGroen/WRPPB-groen.txt" --output_path "RoodGroen.csv"
```

* The argument `--output_path` is optional. If not supplied, the output file will be `RoodGroenAnthe.csv`.
* You can create your own dataset by specifying your own files with possible red and green sentences.

## Future work

* Incorporate [xml_query](https://github.com/BramVanroy/xml_query) by [@BramVanroy](https://github.com/BramVanroy). This will allow for building datasets completely from scratch from Alpino-parsed corpora
* Implement other case studies