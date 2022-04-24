import stanza
from collections import Counter
from Model.Document import Document
from Model.Summ import SummModel
class ExtendedSummModel(SummModel):
    def __init__(self, document:Document) -> None:
        super().__init__(document)
        
    def get_noun_words(self, sentence:str):
        return super().get_noun_words(sentence)

    def create_bigrams(self, sentence:str):
        return super().create_bigrams(sentence)
    
    def calculate_word_frequency(self, noun_words):
        return super().calculate_word_frequency(noun_words)
    
    def calculate_word_weights(self):
        return super().calculate_word_weights()

    def create_text_graph(self):
        return super().create_text_graph()

    def show_text_graph(self, G):
        return super().show_text_graph(G)
    
    def get_candidate_edges(self, G, criteria="avg"):
        return super().get_candidate_edges(G)
    
    def get_candidate_summary(self, C):
        return super().get_candidate_summary(C, edges_count_threshold=1)

    def sentence_selection(self, G, S, n=None):
        return super().sentence_selection(G, S, n)