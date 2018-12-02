import json

words_list = list()
words_dict = dict()

with open('files/newsafr.json', encoding='utf-8') as datafile:
    json_data = json.load(datafile)
    for data in json_data['rss']['channel']['items']:
        description_list = data['description'].split()
        for item in description_list:
            if len(item) >= 6:
                if item.lower() not in words_dict.keys():
                    words_dict[item.lower()] = 0
                words_dict[item.lower()] += 1
        title_list = data['title'].split()
        for item in title_list:
            if len(item) >= 6:
                if item.lower() not in words_dict.keys():
                    words_dict[item.lower()] = 0
                words_dict[item.lower()] += 1

for item in words_dict:
    words_list.append((words_dict[item], item))
words_list.sort(reverse=True)

print('10 наиболее часто встречающихся слов:')
for i, item in enumerate(words_list):
    if i < 6:
        print(item[1])


