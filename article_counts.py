import csv

tone = {'Positive': 0, 'Negative': 0, 'Neutral': 0}
categories = {'Performances': {'Positive': 0, 'Negative': 0, 'Neutral': 0},
              'Public Image & Media Perception': {'Positive': 0, 'Negative': 0, 'Neutral': 0},
              'Industry-specific Impact': {'Positive': 0, 'Negative': 0, 'Neutral': 0},
              'Musical Creation': {'Positive': 0, 'Negative': 0, 'Neutral': 0},
              'Romance': {'Positive': 0, 'Negative': 0, 'Neutral': 0},
              'Personal Life': {'Positive': 0, 'Negative': 0, 'Neutral': 0}}

with open('annotated_articles.csv', 'r') as fp:
    r = csv.DictReader(fp)
    for row in r:
        tone[row['Annotation tone']] += 1
        inner_dict = categories[row['Annotation category']]
        inner_dict[row['Annotation tone']] += 1

totals = {}
for key in categories:
    s = sum(categories[key].values())
    totals[key] = s

print(tone)
print(categories)
print(totals)
