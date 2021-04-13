# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

import sys

def designerPdfViewer(h, word):
    return len(word) * max(list(map(lambda x: h[ord(x) - ord('a')], word)))

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)import sys

########### 2ND WAY

def area_highlighted(h_words, word):
    letters = [ord(i.lower()) - ord('a') for i in word]
    area = max([h_words[i] for i in letters]) * len(letters)
    return area

h = list(map(int, input().strip().split(' ')))
word = input().strip()
print (area_highlighted(h, word))
