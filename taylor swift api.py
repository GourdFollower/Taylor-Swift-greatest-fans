import requests
import json
import csv

params = {
    'q': 'Taylor Swift OR Eras Tour OR swifties',
    'searchIn' : 'title',
    'apiKey': '7298fe90084642578b34773b0ed70e88',
    'from': '2023-11-17',
    'to': '2023-11-22',
    'language': 'en',
}

response = requests.get('https://newsapi.org/v2/everything', params=params)

if response.status_code == 200:
    data = response.json()

    articles = data['articles']

    csv_file = 'taylor_swift_articles_6.csv'

    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Title', 'Description', 'Date', 'Source'])

        for article in articles:
            source_name = article['source']['name'] if article['source'] and 'name' in article['source'] else ''
            csv_writer.writerow([article['title'], article['description'], article['publishedAt'], source_name])

else:
    print(f"Error: {response.status_code} - {response.text}")
