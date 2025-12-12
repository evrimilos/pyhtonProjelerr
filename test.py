textFile = open(r"wordList.txt",'r').readline()
w = [len(word) for word in textFile.split(",")]
print(w)