# ex.8.1
# reading text files


def get_points(filepath):
    f = open(filepath, 'r')
    new_points = []
    for line in f:
        new_points.append(line.split())
    return new_points


b = get_points('points.txt')
print(b)

# ex.8.2
# reading GPS files
import csv


def read_csv_file_old(filename):
    f = open(filename)
    reader = []
    for line in f:
        reader.append(line.split(','))
    return reader
    f.close()

def read_csv_file(filename):
    f = open(filename)
    data = []
    reader = csv.reader(f)
    for line in reader:
        data.append(line)
    return data
    f.close()

gps_list = read_csv_file('GPS.csv')
print(gps_list)


def list_gps_commands(filename):
    char = {}
    for c in gps_list:
        if c[0] in char:
            char[c[0]] = char[c[0]] + 1
            # char[c[0]]+=1
        else:
            char[c[0]] = 1
    return char


gps_dict = list_gps_commands(gps_list)
print(gps_dict)


# ex8.3
# counting words
import string


def word_count(filePath):
    f = open(filePath)
    word_dict = {}  # dictionary in which (key:value) will be (word:count)

    for line in f:
        new_line = line.strip(string.whitespace + string.punctuation).lower().split()
        print(new_line)

        for word in new_line:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

    f.close()
    return word_dict


word_table = word_count('snark.txt')
print(word_table['and'])


# ex.8.4
def store_dict(dictionary, file_path):
    f = open(file_path, "w")
    for key in dictionary:
        f.write("%s: %i\n" % (key, dictionary[key]))

    f.close()

store_dict(word_table, "result32.txt")


# ex.8.5
word_table = word_count ('snark.txt')
def most_often (dictionary):
    count = 0
    word = ''
    for key in dictionary:
        if dictionary [key ] > count:
            count = dictionary [key]
            word = key
    return word , count
print(most_often(word_table))



# def most_often_5_chars (dictionary):
#     count = 0
#     word = ''
#     for key in dictionary :
#      if len(key) == 5:
#         if dictionary [key ] > count :
#             count = dictionary [key]
#             word = key
#     return word , count
# print(most_often_5_chars(word_table))


def most_often_n_chars(dictionary, length):
    count = 0
    word = ''
    for key in dictionary :
        if len(key) == length :
            if dictionary [key ] > count :
                count = dictionary [key]
                word = key
        return word , count
print(most_often_n_chars(word_table, 5))


# ex.8.6
def begin_with_b(file_path):
    word_table = word_count(file_path)
    count = 0
    for key in word_table:
        if key [0] == 'b':
            count += 1
    return count
print ( begin_with_b ('snark.txt'))


def begin_with_char(file_path , char):
    word_table = word_count(file_path)
    count = 0
    for key in word_table:
        if key [0] == char:
            count += 1
    return count
print(begin_with_char('snark.txt', 'b'))