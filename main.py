from csv import reader
from random import randint
import xml.etree.ElementTree as ET

count = 0
blist = []
flag = 0
output = open('result.txt', 'w')
author = input('Введите автора произведения: ').lower()
with open('books.csv', 'r') as csvfile:
    books = reader(csvfile, delimiter=';')
    for row in books:
        lowercase = row[4].lower()
        if not lowercase.find(author) == -1:
            print(row[1])
            flag = 1
            blist.append(f'{row[1]}. {row[4]}')
        if len(row[1]) > 30:
            count += 1
output.write(str(count) + '\n')
for i in range(len(blist)):
    output.write(f'{blist[i]} \n')

    if flag == 0:
        print('Ничего не найдено.')

output.close()



line = 1
bglist = []
output = open('gener.txt', 'w')
rng = []
for i in range(20):
    rng.append(randint(0, 9409))
with open('books.csv', 'r') as csvfile:
    books = reader(csvfile, delimiter=';')
    for line_num, number in enumerate(books):
        if rng.count(line_num) == 1:
            bglist.append(f'{line}.{number[4]}. {number[1]}')
            line+=1
for i in range(len(bglist)):
    output.write(f'{bglist[i]} \n')

output.close()



def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    char_code_list = []
    value_list = []

    for valute in root.findall('.//Valute'):
        char_code = valute.find('CharCode').text
        value = valute.find('Value').text

        value = float(value.replace(',', '.'))

        char_code_list.append(char_code)
        value_list.append(value)

    return char_code_list, value_list

xml_file_path = 'currency.xml'

char_code_values, value_values = parse_xml(xml_file_path)

print("CharCode:", char_code_values)
print("Value:", value_values)
