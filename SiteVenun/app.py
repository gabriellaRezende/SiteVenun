from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Product 
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitevenun.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instância do SQLAlchemy
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    with app.app_context():  # Cria o contexto antes de acessar o banco
        db.create_all()
    app.run(debug=True)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profiele')
def profile():
    return render_template('profile.html')


@app.route('/login_handler', methods=['POST'])
def login_handler():
    username = request.form.get('login-form-username')
    password = request.form.get('login-form-password')


    if username == 'admin' and password == 'admin':
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['register-form-name']
        email = request.form['register-form-email']
        username = request.form['register-form-username']
        phone = request.form['register-form-phone']
        senha = request.form['register-form-password']

        #gerador de hash para a senha 
        senha_hash = generate_password_hash(senha)

        # criar instancia do user
        user = User(nome=nome, email=email, username=username, phone=phone, senha=senha_hash)

        #adiciona um user no banco de dados 
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


if __name__=='__main__':
    app.run(debug=True)