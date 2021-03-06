'''
Не все элементы входных данных XML будут в конечном итоге являться элементами анализируемого дерева. В настоящий момент
этот модуль пропускает все комментарии XML, инструкции по обработке и объявления типа документа во входных данных. Тем
не менее, деревья, построенные с использованием API этого модуля, а не синтаксического анализа из XML-текста, могут
иметь комментарии и инструкции по обработке в них.

Создание и сборка XML-документов
Импорт модуля Элемента Дерева
'''

import xml.etree.ElementTree as ET
# Функция Element () используется для создания элементов XML
p = ET.Element('parent')
# Функция SubElement(), используемая для создания вложенных элементов в элементе give
c = ET.SubElement(p, 'child1')
# Функция dump() используется для вывода элементов xml.
ET.dump(p)
# Для сохранения в файл, нужно создать дерево XML с функцией ElementTree() и сохранить в файл, используя метод write()
tree = ET.ElementTree(p)
tree.write("data/example.xml")
# Функция Comment() используется для вставки комментариев в XML-файл.
comment = ET.Comment('user comment for xml-file')
# Данный комментарий будет добавлен к родительскому элементу
p.append(comment)
ET.dump(p)