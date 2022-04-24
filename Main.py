from platform import node
from Model.ExtendedSumm import ExtendedSummModel
from Model.EdgeSumm import EdgeSummModel
from Model.Document import Document
import numpy as np
import itertools
from statistics import mode, mean, median
import os
import matplotlib.pyplot as plt



document_name = "Document_1"
document_path = os.path.join("Document", document_name + ".xml")
document = Document(document_path)
model = EdgeSummModel(document)

G = model.create_text_graph()
#model.show_text_graph(G)
C = model.get_candidate_edges(G)
print(C)
S = model.get_candidate_summary(C)
S_final = model.sentence_selection(G, S, n=5)
print(" ".join(S_final))

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
