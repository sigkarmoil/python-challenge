import re
import statistics

#using paragraph 2 in resources
txtpath= (r'C:\Users\haeze\OneDrive\Documents\GitHub\python-challenge\PyParagraph\raw_data\paragraph_2.txt')
paragraph=open(txtpath,"r")

read_paragraph=paragraph.read()

#character count, take out special characters (.,?!) in the string
def replaceMult(mainString, toBeReplaced, newString):
    for elem in toBeReplaced:
        if elem in mainString:
            mainString=mainString.replace(elem, newString)
    return mainString
read_word_count=replaceMult(read_paragraph, ['.',',','"'] , "" )
print(f"Approximate Word Count: {len(read_word_count)}"   )

#count sentences - resulting in list containing sentences
paragraph_sentence=read_paragraph.split(".")
print(f"Approximate sentence count  {len(paragraph_sentence)-1}" )

#count average letter length in a word - resulting in list containing words
paragraph_letter=read_paragraph.split(" ")
word_length=[]
for words in paragraph_letter:
    word_length.append( len(words) )
print(f"Approximate letter count (per word): {statistics.mean(word_length) }" )

#count average words in a sentence
words_in_sentence=[]
for words in paragraph_sentence:
    words_in_sentence.append( words.split(" ") )
word_count_per_sentence=[]
for j in words_in_sentence:
    word_count_per_sentence.append(len(j) )
print(f"Average sentence length (in words): {statistics.mean(word_count_per_sentence)}"  )


    