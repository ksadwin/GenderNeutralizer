import pickle
import os

def addToDict(picdic):
    if os.path.exists(picdic):
        dic = pickle.load(open(picdic, "rb"))
        print("Dictionary loaded.")
    else:
        dic = {}
        print("New dictionary created.")
    adding = "n"
    while adding == "n":
        key = input("Enter new key: ")
        if key in dic.keys():
            print("Key already exists.")
        else:
            value = input("Enter new value: ")
            dic[key] = value
        adding = input("Done? (y/n)")
    pickle.dump(dic, open(picdic, "wb"))
        
    
    

def main():
    print("Male to Female dictionary: mtf.p")
    print("Female to Male dictionary: ftm.p")
    print("Gender Neutral dictionary: gn.p")
    picdic = input("Enter desired dictionary to edit: ")
    addToDict(picdic)
    
main()
        
