import sys
import string
               
inFileName = sys.argv[1]
outFileName = sys.argv[2]
wordCount = dict()

inFile = open(inFileName)
inText = inFile.read()
outFile = open(outFileName,'w')

#Remove punctuations from input text
for punc in string.punctuation:
    inText = inText.replace(punc,'')

inText = inText.lower()

for word in inText.split():
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

for word in sorted(wordCount):
    outFile.write(word + ' ' + str(wordCount.get(word)) + '\n')
