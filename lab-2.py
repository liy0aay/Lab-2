# import csv
# from random import randrange
RED = '\u001b[31;1m' 
END =  '\u001b[0m'
# with open('books.csv', newline='', encoding='UTF 8') as fh: # или ISO-8859-1
#     reader = csv.reader(fh, delimiter=';', quotechar='"')

    
#     all_books = []
#     all_ta = []
#     for row in reader:
#         all_books.append(row)
#         all_ta+=row[12]  




# all_books = all_books[1:]    #убрала первую строку с названиями столбцов
# all_tags = ''.join(all_ta[1:])

# count_of_long_names = 0

# for book in all_books:
#     if len(book[1]) > 30:
#         count_of_long_names += 1
       

# print (f'Количество записей, в которых название длиннее 30 символов:{count_of_long_names}')  #2933, посчитали количество книг с названием > 30 символов

# years = ['2014', '2016', '2017']
# search_author = input ('Введите имя автора:')    #ищем книгу по автору и условию только 14,16,17 годов
# for book in all_books:
#     if (search_author == book[3]) or (search_author == book [4]):
#         if any(year in book[6] for year in years):
#             print (book[1], book[4], book[6])



# sorted_books = sorted(all_books, key=lambda x: int(x[8]), reverse=True)
# print ("\n20 CАМЫX ПОПУЛЯРНЫX КНИГ:")
# for i in range (20):
#     print ()
#     print (f'{i+1}){sorted_books[i][1]}, {sorted_books[i][2]}, Кол-во выдач: {sorted_books[i][8]}\n')
# #     return 0

# # print_twnt_of_most_pop()


# def set_of_tags():
#     a = all_tags.split("#")
#     for tag in sorted(set(a)):
#         print (tag)
  



# set_of_tags()


# #Отредактировать и подчистить код выше, добавить цвет


# # Реализовать генератор библиографических ссылок вида <автор>. <название> - <год> для 20 записей.
# #  Записи выбрать произвольно. Список сохраняется как отдельный файл текстового формата с нумерацией строк.

# result = [randrange(0, 9400) for x in range (20)]

# with open ('result.txt', 'w') as fh:
#     for num, line in enumerate(result):
#         fh.write(f'{num + 1}.{line} {all_books[line][3]} {all_books[line][1]} {all_books[line][6][6:10]}\n')
        




import xml.dom.minidom as minidom
#Список Name, но только для валют с Nominal=1
#выполнить приведение типов
xml_file = open("currency.xml", "r", encoding = "Windows-1251")
xml_data = xml_file.read() #cчитываем весь контент XML-файла

dom = minidom.parseString(xml_data)  #разбираем содержимое строки xml_data
dom.normalize() #упрощаем структуру документа, объединяя смежные текстовые узлы 


elements = dom.getElementsByTagName ('Valute') # Возвращает список всех узлов с тегом "Valute"

names_list = [] #будем заполнять name и nominal

for node in elements: #узлы
    for child in node.childNodes: #дочерние узлы
        if child.nodeType == 1:   #проверка, что эл явл тегом <...>
            if child.tagName == 'Nominal':
                if child.firstChild.nodeType == 3: #проверяем, что это текстовые данные
                
                    nominal = int(child.firstChild.data)

            if child.tagName == 'Name':
                if child.firstChild.nodeType == 3: #проверяем, что это текстовые данные
                    name = (child.firstChild.data)
    if nominal == 1:   
        names_list += [name]
print (f'{RED}Список валют с номиналом 1{END}:')
for name in names_list:
    print (name)
