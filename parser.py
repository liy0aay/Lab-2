import xml.dom.minidom as minidom
#Список Name, но только для валют с Nominal=1
#выполнить приведение типов
xml_file = open("currency.xml", "r", encoding = "Windows-1251")
xml_data = xml_file.read() #cчитываем весь контент XML-файла

dom = minidom.parseString(xml_data)  #разбираем содержимое строки xml_data
dom.normalize() #упрощаем структуру документа, объединяя смежные текстовые узлы 


elements = dom.getElementsByTagName ('Valute') # Возвращает список всех узлов с тегом "Valute"

names_dict = {} #будем заполнять name и nominal

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

print (names_dict)