from collections import Counter, OrderedDict
from statistics import mean, median_high
from Model.Document import Document
from Model.Summ import SummModel
import networkx as nx
class ExtendedSummModel2(SummModel):
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
    
    def get_candidate_summary(self, G):
        node_weights = dict(G.nodes.data("weight"))
        bigrams_counter = Counter(self.all_bigrams)
        bigram_weights = dict()
        for bigram in list(set(self.all_bigrams)):
            bigram_weight = 0.0
            for word in bigram:
                bigram_weight += node_weights[word]
            bigram_weight *= bigrams_counter[bigram]
            bigram_weights.update({bigram:bigram_weight})
        bigram_sentences = dict()
        for sentence in self.document.paragraphs:
            sentence_bigrams = self.create_bigrams(sentence)
            for bigram in sentence_bigrams:
                if bigram not in bigram_sentences.keys():
                    bigram_sentences.update({bigram:list()})
                bigram_sentences[bigram].append(sentence)
        return self.document.paragraphs, bigram_weights, bigram_sentences

    def sentence_ranking(self, G:nx.Graph, S:list, n=None):
        return super().sentence_ranking(G, S, n)

    def sentence_selection(self, G, S, D:Document, BiW, BiS, n=None):
        # D document
        sentence_weights_dict = D.sentenceWeights
        sentence_rank_dict = self.sentence_ranking(G, S, n)
        
        for key in sentence_rank_dict.keys():
            sentence_rank_dict[key] *= sentence_weights_dict[key]
        orderedBigramWeightsDict = OrderedDict(sorted(BiW.items(), key=lambda kv: kv[1], reverse=True))  
        selectedSentences = list()   
        if n < len(orderedBigramWeightsDict):
            for bigram in list(BiW.keys())[:n]:
                prevValue = -100
                for sentence in BiS[bigram]:
                    if sentence_weights_dict[sentence] > prevValue:
                        prevValue = sentence_weights_dict[sentence]
                        dominantSentence = sentence
                selectedSentences.append(dominantSentence)
        return selectedSentences