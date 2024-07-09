import spacy
from spacy import displacy

nlp = spacy.load("model-last")

file1 = open("first-correct.svg", "w")
file2 = open("first-poor.svg", "w")

doc = nlp("Baran yemek yedi")
first_correct = displacy.render(doc, style = 'dep')
file1.write(first_correct)
file1.close()

doc = nlp("Baran yemek yemek istedi ama yemedi")
first_poor = displacy.render(doc, style = 'dep')
file2.write(first_poor)
file2.close()