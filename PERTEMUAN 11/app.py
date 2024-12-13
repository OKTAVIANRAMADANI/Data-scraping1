from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/liputan6-popular")
def Liputan6Popular():
    htmlDoc = requests.get("https://www.liputan6.com/tekno/internet")
    soup = BeautifulSoup(htmlDoc.text, "html.parser")
    popularArea = soup.find(attrs={'class': 'hentry main'})

    images = []
    if popularArea:
        articles = popularArea.find_all('hentry main')
        for article in articles:
            img_tag = article.find('read-page--top-media')
            if img_tag and 'src' in img_tag.attrs:
                images.append(img_tag['read-page--tod-media'])

    return render_template("populer.html", gambar=images)

if __name__ == "__main__":
    app.run(debug=True)
