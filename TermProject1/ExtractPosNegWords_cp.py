from Parser import Parser
import jieba.posseg as pseg
import jieba
import operator

parser = Parser()

neg_dict = {}
pos_dict = {}
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
                if word in pos_dict.keys():
                    pos_dict[word] += 1
                else:
                    pos_dict[word] = 0
            elif opinion == '-1':
                if word in neg_dict.keys():
                    neg_dict[word] += 1
                else:
                    neg_dict[word] = 0
sorted_pos = sorted(pos_dict.items(), key=operator.itemgetter(1))
sorted_neg = sorted(neg_dict.items(), key=operator.itemgetter(1))

print(sorted_pos)
print('=========')
print(sorted_neg)

target_candidate = 15
candidate_num = 0
for index in range(len(sorted_pos)-1, 0, -1):
    adj = sorted_pos[index][0]
    pos_num = sorted_pos[index][1]
    if adj in neg_dict.keys():
        neg_num = neg_dict[adj]
        if pos_num - neg_num > 1000:
            print ('(%s, %d)' %(adj, pos_num))
            candidate_num += 1
    else:
        print ('(%s, %d)' %(adj, pos_num))
        candidate_num += 1
    if candidate_num >= target_candidate:
        break
print('=========')

target_candidate = 15
candidate_num = 0
for index in range(len(sorted_neg)-1, 0, -1):
    adj = sorted_neg[index][0]
    neg_num = sorted_neg[index][1]
    if adj in pos_dict.keys():
        pos_num = pos_dict[adj]
        if neg_num - pos_num > 1000:
            print ('(%s, %d)' %(adj, neg_num))
            candidate_num += 1
    else:
        print ('(%s, %d)' %(adj, neg_num))
        candidate_num += 1
    if candidate_num >= target_candidate:
        break

# print (sorted_pos[-10:])
# print ('===============')
# print (sorted_neg[-10:])

# pos_file = open('pos_cp.txt', 'w')
# for word in pos_words:
#     pos_file.write('%s\n' %word)
# pos_file.close()


# neg_file = open('neg_cp.txt', 'w')
# for word in neg_words:
#     neg_file.write('%s\n' %word)
# neg_file.close()