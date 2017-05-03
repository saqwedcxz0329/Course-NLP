from Parser import Parser
import jieba.posseg as pseg
import jieba

parser = Parser()


neg_words = []
pos_words = []
# print (pos_words)
for index, line in enumerate(parser.polarity_pos()):
    print (index)
    opinion = line[0]
    content = line[1]
    content = content.split('\n')
    for seg in content:
        seg = seg.split(' ')
        word = seg[0]
        pos = seg[1]
        if pos == 'a':
            if opinion == '1':
                if word not in pos_words:
                    pos_words.append(word)
            elif opinion == '-1':
                if word not in neg_words:
                    neg_words.append(word)
    
                
pos_file = open('pos_cp.txt', 'w')
for word in pos_words:
    pos_file.write('%s\n' %word)
pos_file.close()


neg_file = open('neg_cp.txt', 'w')
for word in neg_words:
    neg_file.write('%s\n' %word)
neg_file.close()