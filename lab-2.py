import csv
import xml.dom.minidom as minidom
from random import randrange

RED = '\u001b[31;1m' 
GREEN = '\u001b[32;1m'
YELLOW = '\u001b[33;1m'
END =  '\u001b[0m'


def open_books():
    with open('books.csv', newline='', encoding='UTF 8') as fh: 
        reader = csv.reader(fh, delimiter=';', quotechar='"')
        books = [row for row in reader]
    return books[1:]


def count_long_names():
    summa = 0
    for  book in books:
        if len(book[1]) > 30:
            summa += 1
    print (f'{YELLOW}Количество книг, c названием длиннее 30 символов:{END}{summa}')
    return 0
    


def search_author():
    years = ['2014', '2016', '2017']
    name_author = input (f'\n{RED}Введите имя автора:{END}')  
    for book in books:
        if (name_author == book[3]) or (name_author == book [4]):
            if any(year in book[6] for year in years):
                print(book[1], book[4], book[6])
    return 0



def search_popular_books():
    sorted_books = sorted(books, key=lambda x: int(x[8]), reverse=True)
    print (f"\n{GREEN}20 CАМЫX ПОПУЛЯРНЫX КНИГ:{END}")
    for i in range(20):
        print (f'{i+1}){sorted_books[i][1]}, {sorted_books[i][3]}, Кол-во выдач: {sorted_books[i][8]}\n')
    return 0


def set_of_tags():
    all_tags = ''.join(((raw[12])) for raw in books)
    list_of_tags = [tag for tag in ((all_tags.split("#")))]
    set_of = set(tag.strip() for tag in list_of_tags)
    print(f'{GREEN}#ЖАНРЫ КНИГ:{END}\n')
    for tag in sorted(set_of):
        print (tag)
    return 0

def generate_books():
    print (f'{RED}Генерирую список случайных книг... ... ...{END}')
    result = [randrange(0, len(books)) for x in range (20)]
    with open ('result.txt', 'w') as fh:
        for num, line in enumerate(result):
            fh.write(f'{num + 1}.{line} {books[line][3]} {books[line][1]} {books[line][6][6:10]}\n')
    return (print(f'{YELLOW}Результат записан в файл result.txt{END}'))




#Список Name, но только для валют с Nominal=1

def read_xml():
    xml_file = open("currency.xml", "r", encoding = "Windows-1251")
    xml_data = xml_file.read() #cчитываем весь контент XML-файла
    dom = minidom.parseString(xml_data)  #разбираем содержимое строки xml_data
    dom.normalize() #упрощаем структуру документа, объединяя смежные текстовые узлы 
    return dom


def search_xml():
    elements = dom.getElementsByTagName ('Valute') # Возвращает список всех узлов с тегом "Valute"
    names_list = []
    for node in elements: #узлы
        for child in node.childNodes: #дочерние узлы
            if child.nodeType == 1:   #проверка, что эл явл тегом <...>
                if child.tagName == 'Nominal':
                    if child.firstChild.nodeType == 3: #проверяем, что это текстовые данные
                    
                        nominal = int(child.firstChild.data)

                if child.tagName == 'Name':
                    if child.firstChild.nodeType == 3:
                        name = (child.firstChild.data)
        if nominal == 1:   
            names_list += [name]
    print (f'\n{GREEN}Список валют с номиналом 1{END}:')
    for name in names_list:
        print (name)
    return 0


if __name__ == "__main__":
    books = open_books()
    count_long_names()
    search_author()
    search_popular_books()
    set_of_tags()
    generate_books()
    dom = read_xml()
    search_xml()


