from platform import node
import sys
from Model.ExtendedSumm import ExtendedSummModel
from Model.ExtendedSumm2 import ExtendedSummModel2
from Model.EdgeSumm import EdgeSummModel
from Model.Document import Document
import numpy as np
import itertools
from statistics import mode, mean, median
import os
import matplotlib.pyplot as plt


model_type = "ExtendedSumm2"
n=5
corpusWeight = 1.2
corpusPath = "Corpus"
document_name = "Document_2"

document_path = os.path.join("Document", document_name + ".xml")

if model_type == "EdgeSumm":
    document = Document(document_path)
    model = EdgeSummModel(document)
elif model_type == "ExtendedSumm":
    document = Document(document_path, corpusPath=corpusPath)
    model = ExtendedSummModel(document, corpusWeight=corpusWeight)
elif model_type == "ExtendedSumm2":
    document = Document(document_path, corpusPath=corpusPath)
    model = ExtendedSummModel2(document, corpusWeight=corpusWeight)
else:
    raise Exception("Invalid Model Type '{}'".format(model_type))

G = model.create_text_graph()
#model.show_text_graph(G)
C = model.get_candidate_edges(G)
#print(C)
if model_type == "ExtendedSumm2":
    S, BiW, BiS = model.get_candidate_summary(G)
else:
    S = model.get_candidate_summary(C)

if model_type  == "ExtendedSumm":
    S_final = model.sentence_selection(G, S, D=document, n=n)
elif model_type == "ExtendedSumm2":
    S_final = model.sentence_selection(G, S, D=document, BiW=BiW, BiS=BiS, n=n)
else:
    S_final = model.sentence_selection(G, S, n=n)
summary = "\n".join(S_final)
with open(os.path.join("Summary", "Auto Generated", document_name + "_" + model_type + "_" + str(n) + ".txt"), "w", encoding="utf-8") as outputFile:
    outputFile.write(summary)

#bigrams = list(itertools.chain.from_iterable([model.create_bigrams(sentence) for sentence in sentences]))

    

'''
Ağırlıkları bir kere de aşağıdaki paragrafa göre tekrar ağırlıklandırıyoruz
Assuming that the occurrence of a word in the title is the most important

while the occurrence in the keywords, frequent bi-grams, and biased words lists is at the same level of importance and more im-
portant than the occurrence in the proper nouns list because the latter list could include very important words as well as less

important words. Therefore, the adjusted weight value used to compute WT, WK, WBI, WP, and WB values is multiplied by αT, αK, αBI,
αP, and αB respectively in Eq. (5). For simplicity, values of αT, αK, αBI, αP, and αB have been chosen to be 1 in the experiments but any
other values could be used too.
'''
