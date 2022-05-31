from abc import ABC
class Freq(ABC):
    address = ""
    def __init__(self, file):
        address = file
    def calculateFreqs(self):
        pass


class ListCount(Freq):
    def calculateFreqs(address):
        with open("strange.txt", "r") as f:
            content = f.read()
            wordlist = []

            for word in content.split():
                if word not in wordlist:
                    wordlist.append(word)

            for word in wordlist:
                wordlist[wordlist.index(word)] = (word + "=" + str(content.count(word)))
            print(wordlist)


class DictCount(Freq):
    def calculateFreqs(address):
        with open("strange.txt", "r") as f:
            content = f.read()
            worddict = {}

            for word in content.split():
                if word not in worddict:
                    worddict.update({word: "0"})

            for word in worddict:
                worddict[word] = str(content.count(word))
            print(worddict)
