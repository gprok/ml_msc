import requests
from bs4 import BeautifulSoup 
import csv 
import time

file = open('freviews.csv', 'w')
out_csv = csv.writer(file)

out_csv.writerow(['title','rating','review'])

for i in range(1, 4):
    response = requests.get(f'https://www.trustpilot.com/review/easyautoonline.com?page={i}')

    page_text = response.text

    soup = BeautifulSoup(page_text, "html.parser")

    reviews_list = soup.select("div[data-reviews-list-start='true']")
    # print(reviews_list)
    reviews = reviews_list[0].find_all("article")

    for review in reviews:
        # print(review.text)
        title = review.select("h2[data-service-review-title-typography='true']")
        # print(title[0].text)
        rating = review.select("div[data-service-review-rating]")
        # print(rating[0]['data-service-review-rating'])
        content = review.select("p[data-service-review-text-typography='true']")
        # print(content[0].text)
        if len(title) > 0 and len(rating) > 0 and len(content) > 0:
            out_csv.writerow([title[0].text, rating[0]['data-service-review-rating'], content[0].text])

    time.sleep(6)
    
file.close()
