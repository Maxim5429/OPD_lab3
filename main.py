from flask import Flask, render_template, request

app = Flask(__name__) #создание объекта класса Flask

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        f=open('login.txt', 'r').readlines() # присвоили переменной date дату из talon.txt под указанным номером
        admin_login = f[0].strip()
        admin_password = f[1].strip()
        if (login==admin_login) and (password==admin_password):
            return("correct")
        else:
            return("incorrect")
    #return render_template('index.html', ans=num_1 + num_2)

if __name__ == '__main__': #запуск
    app.run(debug=True)