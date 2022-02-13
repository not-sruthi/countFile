#function to take text file and count words

filename=input("Enter the filename: ")


def countText(filename):
    text = open(filename, 'r')
    wordCount= 0
    for i in text:
        word = i.split()
        wordCount = wordCount+len(word)
    print("There are",wordCount, "words in this text file.")

countText(filename)

def countLines(filename):
    text = open(filename, 'r')
    lineCount = 1
    for i in text:
        word = i.split('\n')
        lineCount = lineCount+len(word)
    print("There are",lineCount, "lines in this text file.")

countLines(filename)