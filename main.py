import os
from bs4 import BeautifulSoup
import urllib.request
import re
from nltk.tokenize import word_tokenize
from nltk.parse.stanford import StanfordParser
import nltk.tree
#configure these directories to your computer
"""
download stanford jars at:
 http://nlp.stanford.edu/software/stanford-parser-full-2015-01-29.zip
source code for nltk.parse.stanford at:
 http://www.nltk.org/_modules/nltk/parse/stanford.html
"""
os.environ['JAVAHOME'] = "c:/Program Files/Java/jdk1.8.0_05/bin/java.exe"
os.environ['STANFORD_PARSER'] = "stanford-parser-full-2015-01-30/stanford-parser.jar"
os.environ['STANFORD_MODELS'] = "stanford-parser-full-2015-01-30/stanford-parser-3.5.1-models.jar"
#from google import search


#fetch web page, return plain text
def fetch(url):
    try:
        #requests url using faked firefox header
        firefox = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        firefox = urllib.request.urlopen(firefox)
        #decodes the url into a string
        htmlstring = firefox.read().decode("utf-8", errors="ignore")
        #takes the messy string and sticks it in a Beautiful Soup object
        soupy = BeautifulSoup(htmlstring)
        #sticks the header of the url into a variable so we can smash it
        self.header = str(firefox.info())

        #remove excess tags
        [x.extract() for x in soup.findAll('script', 'iframe', 'style', 'link')]

        return htmlstring
    
    except Exception:
        return None

#thank you stackoverflow user James Brady
def flatten(nestedList):
    result = []
    for l in nestedList:
        if isinstance(l, nltk.tree.Tree):
            result.append(l.label())
        if hasattr(l, "__iter__") and not isinstance(l, str):
            result.extend(flatten(l))
        else:
            result.append(l)
    return result

# parses and replaces terms according to !dictionary chosen
def stanfordParse(text):
    #StanfordParser takes params: path to main jar, path to models jar
    sp=StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
    #build terrible tree list
    t = sp.raw_parse(text)    
    l = flatten(t)
    print(l)

#tokenize
def tokenize(text):
    tokens = word_tokenize(text)
    return tokens

#parse and replace with dictionary of choice, return as string edited
#currently basic, only identifies whole words
def parse(tokens, dic):
    edited = ""
    for token in tokens:
        if token in dic.keys():
            token = dic[token]
        edited += token
    return edited

def getSearchResults(query):
    search(query)

#CHOOSE ARTICLES AND DICTIONARIES????

stanfordParse("what am I doing? what is this place?")
