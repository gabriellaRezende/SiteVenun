from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Product 
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitevenun.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco com o app
db.init_app(app) 

#Render Index
@app.route('/')
def index(): 
    return render_template('index.html')

#Render Login
@app.route('/login')
def login():
    return render_template('login.html')

#Render Profile
@app.route('/profile')
def profile():
    return render_template('profile.html')

#Render Cart
@app.route('/cart')
def cart():
    return render_template('cart.html')

#Render checkout 

#Render shop-single

#Render shop

#Login para fazer
@app.route('/login_handler', methods=['POST'])
def login_handler():
    username = request.form.get('login-form-username')
    password = request.form.get('login-form-password')

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.senha, password):
        return redirect(url_for('index'))  # Login bem-sucedido
    return redirect(url_for('login'))

#Render register 
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

#Render 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__=='__main__':
    with app.app_context():  # Cria o contexto antes de acessar o banco
        db.create_all()
        print("banco de dados criado com sucesso!")
    app.run(debug=True)