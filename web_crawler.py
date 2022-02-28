from bs4 import BeautifulSoup
import requests

# webcrawler for stackoverflow questions
response = requests.get("https://stackoverflow.com/questions")

# response.text is an attribute
soup = BeautifulSoup(response.text, "html.parser")
questions = soup.select(".question-summary")
for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())
