import pickle
import os

def addToDict(dic, filename):
    f = open(filename, "r")
    for line in f.readlines():
        line = line.split(":")
        if len(line) == 2:
            dic[line[0]] = line[1].replace("\n", "")
    f.close()
    
    

def main():
    #a dictionary for miscellaneous gendered terms (e.g. husband, fireman, etc.)
    miscTerms = {}
    addToDict(miscTerms, "MGender.txt")
    addToDict(miscTerms, "Fgender.txt")
    pickle.dump(miscTerms, open("misc.p", "wb"))
    
    #order: subjective, objective, possessive, possessive noun. PRP($) is for Stanford grammar
    she = ["she", "her", "her", "hers"]
    he = ["he", "him", "his", "his"]
    they = ["they", "them", "their", "their"]

    #change any pronoun to they
    toThey = {}
    #change she pronouns to he
    toHe = {}
    #change he pronouns to she
    toShe = {}
    for i in range(4):
        toThey[she[i]] = they[i]
        toThey[he[i]] = they[i]
        toShe[he[i]] = she[i]
        toHe[she[i]] = he[i]
    pickle.dump(toThey, open("toThey.p", "wb"))
    pickle.dump(toShe, open("toShe.p", "wb"))
    pickle.dump(toHe, open("toHe.p", "wb"))

    print(toThey)
    print(toHe)
    print(toShe)
    print(miscTerms)
    
    
    
main()
        
