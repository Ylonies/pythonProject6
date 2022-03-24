from flask import Flask, url_for, request

app = Flask(__name__)

prom = ['Человечество вырастает из детства.',
            'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.',
            'И начнем с Марса!',
            'Присоединяйся!']
prof = ['Инженер-исследователь', 'Пилот', 'Строитель', 'Экзобиолог', 'Врач',
        'Инженер по терраформированию', 'Климатолог', 'Специалист по радиационной защите',
        'Астрогеолог', 'Гляциолог', 'Инженер жизнеобеспечения', 'Метеоролог']
t_profs = []
for i in prof:
    t_profs.append(f"""
    <div class="form-check">
    <input class="form-check-input" type="radio" name="prof" id="{i}">
        <label class="form-check-label" for="female">
            {i}
        </label>
    </div>
    """)

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


@app.route("/astronaut_selection", methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style2.css')}" />

                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname"  placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <br>
                                    <div class="form-group">
                                        <label for="form-check">Какие у Вас есть профессии?</label>
                                    {"".join(t_profs)}    
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male">
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <br>
                                     <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <br>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="quest" name="quest">
                                        <label class="form-check-label" for="quest">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['prof'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['quest'])
        print(request.form['accept'])

        return "Форма отправлена"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
