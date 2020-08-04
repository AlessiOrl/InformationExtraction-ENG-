from . import Extraction
import stanza, spacy
from spacy_stanza import StanzaLanguage


class PatternExtraction(Extraction):
    """Angel X. Chang and Christopher D. Manning. 2014. TokensRegex: Defining cascaded regular expressions over
    tokens. Stanford University Technical Report, 2014. [bib] """

    def SpacyStanzaPatternMatching(self):
        path = "../data/originalTexts/" + self.filename

        snlp = stanza.Pipeline(lang="en")
        nlp = StanzaLanguage(snlp)
        text = open(path).read()
        doc = nlp(text)

        # SAVE SENTENCES IN FILE
        f = open("SpacyStanzaSegmentation.txt", "w+")
        for sentence in doc.sents:
            f.write("\n |--------------------------------------| \n" + sentence.text)
        f.close()

    def Stanzapatternmatching(self):
        path = "../data/originalTexts/" + self.filename
        text = open(path).read()
        stanza.download("en")
        nlp = stanza.Pipeline(lang='en', processors='tokenize')
        # Tokenization and sentence segmentation (every sentence is a group of tokens)
        doc = nlp(text)

        # SAVE SENTENCES IN FILE
        """f = open("StanzaSegmentation.txt", "w+")
        for sentence in doc.sentences:
            f.write("\n |--------------------------------------| \n" + sentence.text)
        #print(*[f'{sentence.text}' for sentence in doc.sentences], sep='\n |--------------------------------------| \n')
        f.close()"""

    def Spacypatternmatching(self):
        path = "../data/originalTexts/" + self.filename
        text = open(path).read()
        nlp = spacy.load('en_core_web_sm')
        # parsing full text and creating a doc object
        doc = nlp(text)
        # dividing doc in sentences
        sentences = list(doc.sents)

        # SAVE SENTENCES IN FILE
        """f = open("SpacySegmentation.txt", "w+")
        for sentence in sentences:
            f.write("\n |--------------------------------------| \n" + sentence.text)
        f.close()"""

        # creating a matcher that is gonna be used within the patterns
        """matcher = Matcher(nlp.vocab)
        matcher.add("parentChild", None, pattern)
        matches = matcher(doc)
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]
            span = doc[start:end]
            print(match_id, string_id, start, end, span.text)"""

    def extract(self):
        pass
