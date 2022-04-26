import stanza
from collections import Counter, OrderedDict
from Model.Document import Document
from Model.Summ import SummModel
import networkx as nx
class ExtendedSummModel(SummModel):
    def __init__(self, document:Document, corpusWeight = 1.2) -> None:
        super().__init__(document)
        self.corpusWeight = corpusWeight
        
    def get_noun_words(self, sentence:str):
        return super().get_noun_words(sentence)

    def create_bigrams(self, sentence:str):
        return super().create_bigrams(sentence)
    
    def calculate_word_frequency(self, noun_words):
        return super().calculate_word_frequency(noun_words)
    
    def calculate_word_weights(self):
        word_weights = super().calculate_word_weights()
        print("inside")
        if self.document.corpus_text:
            #print(word_weights)
            for word in list(set(self.all_nouns)):
                if self.document.isWordInCorpus(word):
                    word_weights[word] *= self.corpusWeight
            #print(word_weights)
        return word_weights

    def create_text_graph(self):
        return super().create_text_graph()

    def show_text_graph(self, G):
        return super().show_text_graph(G)
    
    def get_candidate_edges(self, G, criteria="avg"):
        return super().get_candidate_edges(G)
    
    def get_candidate_summary(self, C):
        return super().get_candidate_summary(C, edges_count_threshold=1)

    def sentence_ranking(self, G:nx.Graph, S:list, n=None):
        return super().sentence_ranking(G, S, n)

    def sentence_selection(self, G, S, D:Document, n=None):
        # D document
        sentence_weights_dict = D.sentenceWeights
        sentence_rank_dict = self.sentence_ranking(G, S, n)
        
        for key in sentence_rank_dict.keys():
            sentence_rank_dict[key] *= sentence_weights_dict[key]
        orderedSentenceRankDict = OrderedDict(sorted(sentence_rank_dict.items(), key=lambda kv: kv[1], reverse=True))
        #print(orderedSentenceRankDict)
        orderedSentences = list(orderedSentenceRankDict.keys())
        if n >= len(orderedSentences):
            return S
        else:
            selectedSentences = list()
            for sentence in S:
                if sentence in orderedSentences[:n]:
                    selectedSentences.append(sentence)
            return selectedSentences