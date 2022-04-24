from turtle import pos
import xml.etree.ElementTree as ET

class Document:
    def __init__(self, documentPath) -> None:
        self.all = list()
        self.titles = list()
        self.descriptions = list()
        self.keywords = ""
        self.paragraphs = list()
        
        tree = ET.parse(documentPath)
        root = tree.getroot()
        for child in root:
            for sentence in child:
                sentence_content = sentence.text.strip()
                if child.tag in ("title", "subtitle"):
                    self.titles.append(sentence_content)
                elif child.tag == "keyword":
                    self.keywords = sentence_content
                elif child.tag == "description":
                    self.descriptions.append(sentence_content)
                elif child.tag == "paragraph":
                    self.paragraphs.append(sentence_content)
                else:
                    raise Exception("Invalid Document Object {}".format(child.tag))
                self.all.append(sentence_content)
        

                