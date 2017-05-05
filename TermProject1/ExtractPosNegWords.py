from Parser import Parser
import nltk
from nltk.collocations import *
import jieba.posseg as pseg
import jieba
import operator

parser = Parser()
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
filter_list = '~!@#$%^&*()_+`-=\\{\\}[]\|;:\'\"><:;,.?/'

neg_words = []
pos_words = []
# print (pos_words)

aspect_term = {}
aspect = "交通"
for index, line in enumerate(parser.polarity_seg()):
    print (index)
    opinion = line[0]
    content = line[1]
    # print (content)

    finder = TrigramCollocationFinder.from_words(content)
    finder.apply_word_filter(lambda w: w.lower() in filter_list)

    for a, b, c in finder.nbest(trigram_measures.pmi, 10):
        if a == aspect:
            if b in aspect_term.keys():
                aspect_term[b] += 1
            else:
                aspect_term[b] = 0
            if c in aspect_term.keys():
                aspect_term[c] += 1
            else:
                aspect_term[c] = 0
            # print ("%s, %s, %s" %(a, b, c))
        elif b == aspect:
            if a in aspect_term.keys():
                aspect_term[a] += 1
            else:
                aspect_term[a] = 0
            if c in aspect_term.keys():
                aspect_term[c] += 1
            else:
                aspect_term[c] = 0
            # print ("%s, %s, %s" %(a, b, c))
        elif c == aspect:
            if a in aspect_term.keys():
                aspect_term[a] += 1
            else:
                aspect_term[a] = 0
            if b in aspect_term.keys():
                aspect_term[b] += 1
            else:
                aspect_term[b] = 0
            # print ("%s, %s, %s" %(a, b, c))

sorted_x = sorted(aspect_term.items(), key=operator.itemgetter(1))
print (sorted_x)


# aspect_review_list = parser.aspect_review()
# for line in aspect_review_list:
#     print (line[0])
#     print (' '.join(jieba.cut(line[1])))
#     print (len(line[2]))
#     # finder = BigramCollocationFinder.from_words(jieba.cut(line[1]))
#     # finder.apply_word_filter(lambda w: w.lower() in filter_list)
#     # for a, b in finder.nbest(bigram_measures.pmi, 10):
#     #     print "%s, %s" %(a, b)

#     # print "======="

#     finder = TrigramCollocationFinder.from_words(jieba.cut(line[1]))
#     finder.apply_word_filter(lambda w: w.lower() in filter_list)
#     for a, b, c in finder.nbest(trigram_measures.pmi, 10):
#         print "%s, %s, %s" %(a, b, c)