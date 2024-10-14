import csv


with open('books.csv', newline='', encoding='UTF 8') as fh: # или ISO-8859-1
    reader = csv.reader(fh, delimiter=';', quotechar='"')
    
    all_books = []
    all_tags = ''
    for row in reader:
        all_books.append(row)
        all_tags+=str(row[12])  #придумать как убрать жанр отсюда, может перекинуть считывание в функцию



all_books = all_books[1:]    #убрала первую строку с названиями столбцов


count_of_long_names = 0

for book in all_books:
    if len(book[1]) > 30:
        count_of_long_names += 1
       

print (f'Количество записей, в которых название длиннее 30 символов:{count_of_long_names}')  #2933, посчитали количество книг с названием > 30 символов

years = ['2014', '2016', '2017']
search_author = input ('Введите имя автора:')    #ищем книгу по автору и условию только 14,16,17 годов
for book in all_books:
    if (search_author == book[3]) or (search_author == book [4]):
        if any(year in book[6] for year in years):
            print (book[1], book[4], book[6])



sorted_books = sorted(all_books, key=lambda x: int(x[8]), reverse=True)
print ("\n20 CАМЫX ПОПУЛЯРНЫX КНИГ:")
for i in range (20):
    print ()
    print (f'{i+1}){sorted_books[i][1]}, {sorted_books[i][2]}, Кол-во выдач: {sorted_books[i][8]}\n')
#     return 0

# print_twnt_of_most_pop()


def set_of_tags():
    a = all_tags.split("#")
    print (len(a))
    print (len(set(a)))
    s = sorted(set(a))
    print (s)



set_of_tags()


#Отредактировать и подчистить код выше, добавить цвет


# Реализовать генератор библиографических ссылок вида <автор>. <название> - <год> для 20 записей. Записи выбрать произвольно. Список сохраняется как отдельный файл текстового формата с нумерацией строк.


# Используя приложенный файл currency.xml, выполнить следующее:
# Распарсить файл и извлечь  данные, согласно варианту(Список Name, но только для валют с Nominal=1). Выполнить приведения типов по необходимости.
