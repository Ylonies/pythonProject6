from flask import Flask, url_for

app = Flask(__name__)

prom = ['Человечество вырастает из детства.',
            'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.',
            'И начнем с Марса!',
            'Присоединяйся!']

@app.route('/')
def mission_name():
     return "Миссия Колонизация Марса"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def promotion():
    return '</br>'.join(prom)

@app.route("/image_mars")
def image_mars():

    return f"""<!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Привет, Марс!</title>
    </head>
    <body>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/mars.png')}">
    <p>Вот она какая, красная планета</p>
    </body>
    </html>"""

@app.route("/promotion_image")
def promotion_image():
    alert = ["primary", "secondary", "success", "danger", "warning", "info"]
    text = []
    for i in range(len(prom)):
        text.append(f"""
        <div class="alert alert-{alert[i]}" role="alert">
          {prom[i]}
        </div>
""")
    return f"""<!doctype html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
        <title>Привет, Марс!</title>
        </head>
        <body>
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='img/mars.png')}">
        {"".join(text)}
        </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
