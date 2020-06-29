import nltk

file1 = open("doc1.txt", "r")
text1 = file1.readlines()

file2 = open("doc2.txt", "r")
text2 = file2.readlines()

str1 = ''.join(text1)
str2 = ''.join(text2)

"""
    Here by using '.' we can check the sentences between two documents.
    Here by using '\n' we can check two paras batween two documents for plagiarism.
    In the same if we use ' ' space then we can check words between two documents for plagiarism.

"""
senten_text1 = str1.split(".")
senten_text2 = str2.split(".")

final_list = []

for x in senten_text1:
    for y in senten_text2:
        if x == y:
            final_list.append(x)



