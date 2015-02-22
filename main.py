import os
from bs4 import BeautifulSoup
import urllib.request
import re
from nltk.tokenize import word_tokenize
from nltk.parse.stanford import StanfordParser
import nltk.tree
import pickle
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


#fetch web page, return tuple of title, plain text
def fetch(url):
    try:
        #requests url using faked firefox header
        firefox = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        firefox = urllib.request.urlopen(firefox)
        #decodes the url into a string
        htmlstring = firefox.read().decode("utf-8", errors="ignore")
        #takes the messy string and sticks it in a Beautiful Soup object
        soupy = BeautifulSoup(htmlstring)
        

        #remove excess tags
        [x.extract() for x in soupy.findAll('script', 'iframe', 'style', 'link')]
        if (soupy.title != None):
            title = soupy.title.string.strip()
        text = soupy.get_text().strip()

        return [title, text]
    
    except Exception:
        return None
"""
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
"""
# parses and replaces terms according to !dictionary chosen
def parse(text, dic, gendic):
    #tokenize page (list of individual words)
    tokens = nltk.word_tokenize(text)
    #add tags (list of tuple (tag, word) pair)
    body = nltk.pos_tag(tokens)
    #accumulate edited text
    edited = ""
    for word in body:
        if word[1] == "PRP" or word[1] == "PRP$":
            if word in dic.keys():
                edited += dic[word[0]]
        elif word[0] in gendic.keys():
            edited += gendic[word[0]]
        else:
            edited += word[0]
    return edited
                
"""
def getSearchResults(query):
    search(query)
"""


def main():
    gendic = pickle.load(open("misc.p", "rb"))
    url = input("URL: ")
    print("1. They\n2. She\n3. He")
    r = input("Which?: ")
    if r == "3":
        dic = pickle.load(open("toHe.p", "rb"))
    elif r == "2":
        dic = pickle.load(open("toShe.p", "rb"))
    else:
        dic = pickle.load(open("toThey.p", "rb"))
    print(gendic)
    print(dic)

main()
