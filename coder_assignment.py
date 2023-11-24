import random

"""Accepts the length of a list of articles (which must be at least 200 articles long)

Returns list of dictionaries of equal length to total number of articles, each with a
'to_code' value of either True or False and a 'coders' value of a list of names (empty if False).
It should assign 2 coders to each article being coded & 100 articles to each of us"""


def assign_coders(length):
    names = ['Anna', 'MJ', 'Surya', 'Tessa']

    coding_data = [{'to_code': False, 'coders': []} for _ in range(length)]
    s = random.sample(range(0, length), 200)
    for val in s:
        coding_data[val]['to_code'] = True

    name_0 = random.sample(s, 100)
    name_1 = random.sample(s, 100)
    for val in name_0:
        coding_data[val]['coders'].append(names[0])
    for val in name_1:
        coding_data[val]['coders'].append(names[1])

    for i in range(len(coding_data)):
        if len(coding_data[i]['coders']) == 2:
            s.remove(i)

    count = 0
    s_temp = s.copy()
    for i in range(len(coding_data)):
        if coding_data[i]['to_code'] is True and len(coding_data[i]['coders']) == 0:
            coding_data[i]['coders'].append(names[2])
            count = count + 1
            if i in s_temp: s_temp.remove(i)

    print(count)
    if 100 - count > 0:
        name_2 = random.sample(s_temp, 100-count)
        for val in name_2:
            coding_data[val]['coders'].append(names[2])

        for i in range(len(coding_data)):
            if len(coding_data[i]['coders']) == 2:
                if i in s: s.remove(i)

    name_3 = random.sample(s, 100)
    for val in name_3:
        coding_data[val]['coders'].append(names[3])

    return coding_data
