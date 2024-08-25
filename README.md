# Dependencency Parser
## **Introduction**
This repository contains the implementation of dependency parser for Turkish language in NLP.

## **Installation**
* Make sure you have installed spacy in your local machine
 ````text
pip install -U pip setuptools wheel
pip install -U spacy
````

* Clone repository to your local machine.
 ````text
git clone https://github.com/mbkorkusuz/dependencyParsing.git
````
* Navigate to the project directory in the terminal.

Initialize the spacy module with the given base configuration.
 ````text
python3 -m spacy init fill-config base_config.cfg config.cfg
````

Convert `conllu` data type to spacy data type.
 ````text
python3 -m spacy data/convert tr_imst-ud-train.conllu . --converter conllu --file-type spacy -m --lang tr
python3 -m spacy data/convert tr_imst-ud-dev.conllu . --converter conllu --file-type spacy -m --lang tr
python3 -m spacy data/convert tr_imst-ud-test.conllu . --converter conllu --file-type spacy -m --lang tr
````

Train the model with the converted data.
````text
python3 -m spacy train config.cfg --output . --paths.train ./tr_imst-ud-train.spacy --paths.dev ./tr_imst-ud-dev.spacy
````

For benchmark results, run:
````text
python3 -m spacy benchmark accuracy ./model-last tr_imst-ud-test.spacy -G -dp .
````

For testing the trained model with specific sentences, configure the sentences in displacy.py file and run it to see the output of the trained model.
````text
python3 displacy.py
````

## **Example Output**
Here are two examples of dependence detection of the trained model.
<div class="header">
  <h1>
    Correctly Detected (Easy example)
  </h1>
</div>
<img src="/output_sample/first-correct.svg" alt="Easy" title="Easy" width=50% height=50%>
<div class="header">
  <h1>
    Poorly Detected (Hard example)
  </h1>
</div>
<img src="/output_sample/first-poor.svg" alt = "Hard" title="Hard" width=50% height=50%>


## **Benchmark Results**


| Attribute  | Score |
| ------------- | ------------- |
| TOK  | 100.00  |
| UAS  | 60.16  |
| LAS  | 46.79  |
| SENT P  | 98.78  |
| SENT R  | 99.39  |
| SENT F  | 99.08  |
| SPEED  | 11150  |


Here is the labeled attachment score per type:


| POS | Precision | Recall | F-Score |
| -------------  | ------------- | ------------- | ------------- |
| obl | 40.41  | 41.70 | 41.05 |
| root | 68.16 | 68.58 | 68.37 |
| nsubj | 35.47 | 37.27 | 36.35 |
| det | 72.03 | 79.82 | 75.73 |
| obj | 50.00 | 45.87 | 47.85 |
| nummod | 40.21 | 36.79 | 38.42 |
| flat | 53.66 | 52.69 | 53.17 |
| amod | 47.23 | 52.82 | 49.87 |
| compound | 37.82 | 33.75 | 35.67 |
| cc | 42.75 | 38.56 | 40.55 |
| conj | 30.15 | 34.71 | 32.27 |
| nmod:poss | 46.33 | 54.49 | 50.08 |
| nmod | 26.87 | 22.55 | 24.52 |
| acl | 46.15 | 48.00 | 47.06 |
| dep | 0.00 | 0.00 | 0.00 |
| cop | 58.33 | 5.26 | 9.66 |
| case | 72.51 | 47.96 | 57.74 |
| compound:lvc | 61.84 | 56.63 | 59.12 |
| advmod | 48.08 | 48.70 | 48.39 |
| csubj | 0.00 | 0.00 | 0.00 |
| compound:redup | 30.77 | 22.22 | 25.81 |
| advmod:emph | 64.82 | 76.79 |70.30 |
| fixed | 0.00 | 0.00 | 0.00 |
| discourse | 53.85 | 28.00 | 36.84 |
| aux:q | 73.91 | 69.39 | 71.58 |
| mark | 26.67 | 23.53 | 25.00 |
| advcl | 0.00 | 0.00 | 0.00 |
| ccomp | 0.00 | 0.00 | 0.00 |
| parataxis | 0.00 | 0.00 | 0.00 |
| appos | 0.00 | 0.00 | 0.00 |
