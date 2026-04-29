import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

def get_news_titles(url, num_titles=20):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.select('h3 a')
    return [title.get_text().strip() for title in titles[:num_titles]]

@app.route('/')
def home():
    url = "https://www.chinatimes.com/realtimenews/?chdtv"
    titles = get_news_titles(url)
    html = "<h1>前十則新聞標題</h1><ol>"
    for title in titles:
        html += f"<li>{title}</li>"
    html += "</ol>"
    return html

if __name__ == '__main__':
    app.run(debug=True)