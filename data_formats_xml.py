import xml.etree.ElementTree as ET

tree = ET.parse('files/newsafr.xml')
root = tree.getroot()

words_list = list()
words_dict = dict()

items = root.findall('channel/item')
for xmlitem in items:
    description_list = xmlitem.find('description').text.split()
    for item in description_list:
        if len(item) >= 6:
            if item.lower() not in words_dict.keys():
                words_dict[item.lower()] = 0
            words_dict[item.lower()] += 1
    title_list = xmlitem.find('title').text.split()
    for item in title_list:
        if len(item) >= 6:
            if item.lower() not in words_dict.keys():
                words_dict[item.lower()] = 0
            words_dict[item.lower()] += 1

for item in words_dict:
    words_list.append((words_dict[item], item))
words_list.sort(reverse=True)

print('10 наиболее часто встречающихся слов:')
for item in words_list[:10]:
    print(item[1])
