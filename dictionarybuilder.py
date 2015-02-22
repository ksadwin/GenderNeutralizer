import pickle
import os

def addToDict(dic, filename):
    f = open(filename, "r")
    for line in f.readlines():
        line = line.split(":")
        if len(line) == 2:
            dic[line[0]] = line[1]
    f.close()
    
    

def main():
    #a dictionary for miscellaneous gendered terms (e.g. husband, fireman, etc.)
    miscTerms = {}
    addToDict(miscTerms, "MGender.txt")
    addToDict(miscTerms, "Fgender.txt")
    pickle.dump(miscTerms, open("misc.p", "wb"))
    
    #order: subjective, objective, possessive, possessive noun. PRP($) is for Stanford grammar
    she = [("PRP", "she"), ("PRP", "her"), ("PRP$", "her"), ("PRP", "hers")]
    he = [("PRP", "he"), ("PRP", "him"), ("PRP$", "his"), ("PRP", "his")]
    they = [("PRP", "they"), ("PRP", "them"), ("PRP$", "their"), ("PRP", "their")]

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
    
    
    
main()
        
