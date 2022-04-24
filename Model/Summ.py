from abc import abstractmethod
from matplotlib.pyplot import text
import stanza
from abc import ABC, abstractmethod
from collections import Counter, OrderedDict
from Model.Document import Document
from statistics import mode, mean, median
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class SummModel(ABC):
    def __init__(self, document:Document) -> None:
        self.nlp = stanza.Pipeline(processors='tokenize,mwt,lemma,pos', models_dir='.', lang="tr", treebank="UD_Turkish-Tourism", use_gpu=True, pos_batch_size=3000) # Build the pipeline, specify part-of-speech processor's batch size
        self.document= document

        self.sentence_bigram_dict = dict()

        self.title_nouns = list()
        self.title_nprops = list()
        for title in document.titles:
            tmp_nouns, tmp_nprops = self.get_noun_words(title)
            self.title_nouns += tmp_nouns
            self.title_nprops += tmp_nprops

        if document.keywords:
            self.keywords_nouns, self.keywords_nprops = self.get_noun_words(document.keywords)
        else:
            self.keywords_nouns, self.keywords_nprops = list(), list()

        self.sentence_nouns = list()
        self.sentence_nprops = list()
        for sentence in document.paragraphs:
            tmp_nouns, tmp_nprops = self.get_noun_words(sentence)
            self.sentence_nouns += tmp_nouns
            self.sentence_nprops += tmp_nprops
        
        self.all_nouns = self.title_nouns + self.keywords_nouns + self.sentence_nouns
        self.all_nprops = self.title_nprops + self.keywords_nprops + self.sentence_nprops

    @abstractmethod
    def get_noun_words(self, sentence:str):
        sentence = sentence.replace('.', ' ').replace('\n', ' ')
        
        doc = self.nlp(sentence)

        noun_words = list()
        prop_words = list()
        for token in doc.sentences[0].tokens:
            if token.words[0].xpos in ("Noun", "Prop"):
                root_word = token.words[0].lemma.lower()
                noun_words.append(root_word)
                if token.words[0].xpos == "Prop":
                    prop_words.append(root_word)
        return noun_words, prop_words


    @abstractmethod
    def create_bigrams(self, sentence:str):
        noun_words, prop_words = self.get_noun_words(sentence)
        bigrams = list(zip(noun_words[0::2], noun_words[1::2])) + list(zip(noun_words[1::2], noun_words[2::2]))
        
        return bigrams

    @abstractmethod
    def calculate_word_frequency(self, noun_words):
        return Counter(noun_words)

    @abstractmethod
    def calculate_word_weights(self):
        word_frequency = self.calculate_word_frequency(self.all_nouns)
        title_frequency = self.calculate_word_frequency(self.title_nouns)
        keyword_frequency = self.calculate_word_frequency(self.keywords_nouns)
        bigram_frequency = self.calculate_word_frequency(self.sentence_nouns)
        proper_frequency = self.calculate_word_frequency(self.all_nprops)

        w_f = abs(mean(word_frequency.values()) - median(word_frequency.values()))
        w_t = abs(mean(title_frequency.values()) - median(title_frequency.values())) if title_frequency else 0.0
        w_k = abs(mean(keyword_frequency.values()) - median(keyword_frequency.values())) if keyword_frequency else 0.0
        w_bi = abs(mean(bigram_frequency.values()) - median(bigram_frequency.values())) if bigram_frequency else 0.0
        w_p = abs(mean(proper_frequency.values()) - median(proper_frequency.values())) if proper_frequency else 0.0

        word_weights = dict()
        for word_key in word_frequency.keys():
            if word_key in title_frequency:
                f_t = title_frequency[word_key]
            else:
                f_t = 0.0
            if word_key in keyword_frequency:
                f_k = keyword_frequency[word_key]
            else:
                f_k = 0.0
            if word_key in bigram_frequency:
                f_bi = bigram_frequency[word_key]
            else:
                f_bi = 0.0
            if word_key in proper_frequency:
                f_p = 1.0
            else:
                f_p = 0.0
            weight = w_f + w_t * f_t + w_k * f_k + w_bi * f_bi + w_p * f_p
            word_weights.update({word_key:weight})
        return word_weights

    @abstractmethod
    def create_text_graph(self):
        G = nx.DiGraph()

        word_weights = self.calculate_word_weights()
        for word in word_weights.keys():
            G.add_node(word, weight=word_weights[word])
        
        all_bigrams = list()
        for sentence in self.document.paragraphs:
            sentence_bigrams = self.create_bigrams(sentence)
            self.sentence_bigram_dict.update({sentence:sentence_bigrams})
            all_bigrams += sentence_bigrams

        G.add_edges_from(all_bigrams)
        return G
    
    @abstractmethod
    def show_text_graph(self, G):
        fig = plt.figure(figsize=(1000,1000))
        pos = nx.spectral_layout(G)
        nx.draw(G, with_labels = True)
        plt.show()
        
    @abstractmethod
    def get_candidate_edges(self, G:nx.Graph, criteria="avg"):
        '''Method = avg Average, node_avg Median'''
        # candidate edges
        C = list()
        #nodes, weights = zip(*G.nodes.data("weight"))
        nodes = dict(G.nodes.data("weight"))
        for node in nodes.keys():
            out_nodes = list(G.neighbors(node))
            out_nodes_weights = [nodes[out_node] for out_node in out_nodes]
            if not out_nodes_weights:
                continue
            if criteria == "avg":
                average_weight = mean(out_nodes_weights)
                destination_node_weight = average_weight
            elif criteria == "node_avg":
                weights = nodes.values()
                average_weight = mean(weights)
                median_weight = median(weights)
                if median_weight > average_weight:
                    source_node_weight = median_weight
                else:
                    source_node_weight = average_weight
                destination_node_weight = source_node_weight
            elif criteria == "max":
                maximum_weight = max(out_nodes_weights)
                destination_node_weight = maximum_weight
            else:
                raise Exception("Invalid Criteria '{}'".format(criteria))
            
            for out_node in out_nodes:
                pass_flag = 0
                if nodes[out_node] >= destination_node_weight:
                    pass_flag = 1
                    C.append((node, out_node))
                #print("Base node: {} | Out node: {} | Out node weight {} | Destination node weight {} | Pass flag {}".format(node, out_node, nodes[out_node], destination_node_weight, pass_flag))
        return C

    @abstractmethod
    def get_candidate_summary(self, C, edges_count_threshold=1):
        candidate_summary = list()
        for sentence in self.document.paragraphs:
            candidate_count = 0
            for bigram in self.sentence_bigram_dict[sentence]:
                if bigram in C:
                    candidate_count += 1
            if candidate_count >= edges_count_threshold:
                candidate_summary.append(sentence)
        return candidate_summary

    @abstractmethod
    def sentence_selection(self, G:nx.Graph, S:list, n=None):
        # Sentece bigram ranking used
        if not n:
            return S
        noun_weight = dict(G.nodes.data("weight"))
        sentence_rank_dict = dict()
        for sentence in S:
            # Bigram weight
            sentence_nodes = list(set(np.ravel(self.sentence_bigram_dict[sentence])))
            sentence_nodes_weight = [noun_weight[node] for node in sentence_nodes]
            bigram_weight = sum(sentence_nodes_weight) / max(sentence_nodes_weight)
            sentence_rank_dict.update({sentence:bigram_weight})
        orderedSentenceRankDict = OrderedDict(sorted(sentence_rank_dict.items(), key=lambda kv: kv[1], reverse=True))
        orderedSentences = list(orderedSentenceRankDict.keys())
        if n >= len(orderedSentences):
            return S
        else:
            selectedSentences = list()
            for sentence in S:
                if sentence in orderedSentences[:n]:
                    selectedSentences.append(sentence)
            return selectedSentences


                
            


        
