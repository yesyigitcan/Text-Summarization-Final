import xml.etree.ElementTree as ET
import os

class Document:
    def __init__(self, documentPath, corpusPath=None, minimumSentenceWeight = 0.8) -> None:
        self.all = list()
        self.titles = list()
        self.descriptions = list()
        self.keywords = None
        self.paragraphs = list()
        self.sentenceWeights = dict()
        __tmpSentenceGroup = list()
        tree = ET.parse(documentPath)
        root = tree.getroot()
        if corpusPath:
            if "corpus" in root.attrib:
                corpusFileName = root.attrib["corpus"] + ".txt"
                corpusFilePath = os.path.join(corpusPath, corpusFileName)
                if os.path.exists(corpusFilePath):
                    with open(corpusFilePath, encoding="utf-8") as corpusFile:
                        self.corpus_text = corpusFile.read()
                else:
                    self.corpus_text = None
                    print("WARNING: Corpus file {} does not exist in path {}".format(corpusFileName, corpusFilePath))
                    print("WARNING: Corpus effect is ignored")
            else:
                self.corpus_text = None
                print("WARNING: No corpus assigned for input document")
                print("WARNING: Corpus effect is ignored")
        for child in root:
            for sentence in child:
                sentence_content = sentence.text.strip()
                if child.tag == "paragraph":
                    self.paragraphs.append(sentence_content)
                    __tmpSentenceGroup.append(sentence_content)
                else:
                    if __tmpSentenceGroup:
                        __tmpSentenceWeights = self.__sentencePositionWeight(__tmpSentenceGroup, minimumSentenceWeight)
                        self.sentenceWeights.update(__tmpSentenceWeights)
                        __tmpSentenceGroup = list()
                    if child.tag in ("title", "subtitle"):
                        self.titles.append(sentence_content)
                    elif child.tag == "keyword":
                        self.keywords = sentence_content
                    elif child.tag == "description":
                        self.descriptions.append(sentence_content)
                    else:
                        raise Exception("Invalid Document Object {}".format(child.tag))
                self.all.append(sentence_content)
        if __tmpSentenceGroup:
            __tmpSentenceWeights = self.__sentencePositionWeight(__tmpSentenceGroup, minimumSentenceWeight)
            self.sentenceWeights.update(__tmpSentenceWeights)
    
    def __sentencePositionWeight(self, __tmpSentenceGroup, minimumSentenceWeight):
        sentenceWeights = list()
        groupSize = len(__tmpSentenceGroup)
        if groupSize == 1:
            sentenceWeights.append(1)
        elif groupSize == 2:
            sentenceWeights.append(1)
            sentenceWeights.append(1)
        else:
            isEven = groupSize%2==0.0
            if isEven:
                second_mid_point = int(groupSize / 2.0)
                first_mid_point = second_mid_point - 1
            else:
                first_mid_point = int(groupSize / 2.0)
                second_mid_point = first_mid_point
            stepSize = (1 - minimumSentenceWeight)/first_mid_point
            prevValue = 1
            sentenceWeights.append(1)
            for i in range(1, first_mid_point):
                newValue = prevValue - stepSize
                sentenceWeights.append(newValue)
                prevValue = newValue
            sentenceWeights.append(minimumSentenceWeight)
            if isEven:
                sentenceWeights.append(minimumSentenceWeight)
            prevValue = minimumSentenceWeight
            for i in range(second_mid_point, groupSize-1):
                newValue = prevValue + stepSize
                sentenceWeights.append(newValue)
                prevValue = newValue
            sentenceWeights.append(1)
        return dict(zip(__tmpSentenceGroup, sentenceWeights))

    def isWordInCorpus(self,word):
        if word in self.corpus_text:
            return True
        return False





        

                