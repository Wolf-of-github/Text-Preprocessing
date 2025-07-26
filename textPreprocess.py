import re
import nltk
import contractions
import unidecode
from nltk.corpus import stopwords

nltk.download('stopwords')


class TextPreprocessing:
    def __init__(self):
        self.text = """<p>Social media% platforms0, 6789 they've@
        revolutionized the way people communicate and share information. Users are
        constantly generating vast amounts& of textual data through posts, commentsand messages. %It*'s$ data contains valuable insights into public opinions,
        trends, and$ user preferences. However, extracting meaningful information from
        this unstructured text can be challenging. Applying <strong>Natural0 Language
        Processing (NLP)</strong> techniques to social media data allows us to uncover
        patterns, sentiments, and topics of@ discussion. By analyzing user-generated
        content, we can gain a deeper understanding of customer sentiments, identify90
        émerging! we've trends, and develop targeted marketing strategies. NLP enables
        us to sift through the énormous volume of social media10 data, i'm
        transforming& it into valuable knowledge that can drive informed décision-
        making and *enhance ^ user () experiences..</p> 109"""
        self.tokens = []

    def processText(self):
        self.removeHTML()
        self.removeAccentedText()
        self.wordTokenization()
        self.rm_digit_spChr_punct()
        self.expandContractions()
        self.convertToLowerCase()
        self.removeStopWords()
        cleanText = self.removeWhiteSpaces()
        return cleanText

    def removeHTML(self):
        regex = re.compile(r'<[^>]+>')
        self.text = regex.sub('', self.text)

    def removeAccentedText(self):
        self.text = unidecode.unidecode(self.text)

    def wordTokenization(self):
        self.tokens = [word for word in self.text.split()]

    def rm_digit_spChr_punct(self):
        self.tokens = [re.sub(r"[^a-zA-Z']", '', word) for word in self.tokens]

    def expandContractions(self):
        self.tokens = [contractions.fix(word) for word in self.tokens]

    def convertToLowerCase(self):
        self.tokens = [word.lower() for word in self.tokens]

    def removeStopWords(self):
        text = ' '.join(self.tokens)
        words = text.split()
        stop_words = set(stopwords.words('english'))
        self.tokens = [word for word in words if word not in stop_words]

    def removeWhiteSpaces(self):
        return ''.join(self.tokens)


t = TextPreprocessing()
cleanText = t.processText()
print(cleanText)
