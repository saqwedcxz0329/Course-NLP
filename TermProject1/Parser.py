import csv


class Parser():
    """docstring for Parser"""
    def __init__(self):
        self.data_folder = "./data/"
        self.filter_punc = ",，.．。!！?？-()（）「」『 』:：、;～~ "

    
    def _trim_punc(self, line, replace_str = ','):
        for punc in self.filter_punc:
            line = line.replace(punc, replace_str)
        return line

    '''
    if parse aspect_review.txt the size = 4
    else parse test.review.txt the size = 2
    '''
    def parse_review(self, file_name, size):
        index = 0
        aspect_review_list = []
        with open(self.data_folder + file_name) as file:
            content = []
            for line in file:
                line = line.strip()
                line = self._trim_punc(line)
                if index > 1:
                    line = line.split('\t')
                content.append(line)
                index += 1
                if index == size:
                    index = 0
                    aspect_review_list.append(content)
                    content = []
        return aspect_review_list

    def test_review(self, file_name):
        index = 0
        review_id = 0
        aspect_review_list = {}
        # with open(self.data_folder + 'test_review.txt') as file:
        with open(self.data_folder + file_name) as file:
            for line in file:
                line = line.strip()
                if index == 0:
                    review_id = line
                    index +=1
                elif index == 1:
                    line = self._trim_punc(line)
                    aspect_review_list[review_id] = line
                    index = 0
        return aspect_review_list

    def polarity_seg(self):
        polarity_seg = []
        with open(self.data_folder + 'polarity_review_seg.csv') as file:
            for index, row  in enumerate(csv.reader(file)):
                if index == 0:
                    continue
                row[1] = row[1].split(' ')
                tmp = []
                for word in row[1]:
                    if word not in self.filter_punc:
                        tmp.append(word)
                row[1] = tmp
                polarity_seg.append(row)
        return polarity_seg

    def polarity_pos(self):
        polarity_pos = []
        with open(self.data_folder + 'polarity_review_posseg.csv') as file:
            for index, row in enumerate(csv.reader(file)):
                if index == 0:
                    continue
                polarity_pos.append(row)
        return polarity_pos

    def polarity_review(self):
        polarity_review = []
        with open(self.data_folder + 'polarity_review.txt') as file:
            for line in file:
                line = line.strip()
                line = line.split('\t')
                # line[1] = self._trim_punc(line[1], '')
                polarity_review.append(line)
        return polarity_review

    def read_test(self, file_name):
        # csv_reader = list(csv.reader(open(self.data_folder + 'test.csv')))
        csv_reader = list(csv.reader(open(self.data_folder + file_name)))
        return csv_reader[1:]

    def read_aspect_term(self):
        with open(self.data_folder + 'aspect_term.txt') as file:
            aspect_term = {}
            for line in file:
                line = line.strip('\n').split('\t')
                aspect = line[0]
                terms = line[1].split(' ')
                terms.append(aspect)
                aspect_term[aspect] = terms
        return aspect_term

    def negative(self, file_name):
        with open(self.data_folder + file_name) as file:
            negative_word = []
            for line in file:
                line = line.strip('\n')
                negative_word.append(line)
        return negative_word

    def positive(self, file_name):
        with open(self.data_folder + file_name) as file:
            negative_word = []
            for line in file:
                line = line.strip('\n')
                negative_word.append(line)
        return negative_word


if __name__ == '__main__':
    parser = Parser()
    print (parser.polarity_seg())
