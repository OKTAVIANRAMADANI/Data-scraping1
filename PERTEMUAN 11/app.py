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
    popularArea = soup.find(attrs={'class': 'container-article'})

    images = []
    if popularArea:
        figures = popularArea.find_all('figure')
        for figure in figures:
            img_tag = figure.find('img')
            if img_tag and 'src' in img_tag.attrs:
                images.append(img_tag['src'])

    return render_template("populer.html", gambar=images)

if __name__ == "__main__":
    app.run(debug=True)
