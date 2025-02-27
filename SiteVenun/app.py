from flask import Flask, render_template, redirect, url_for, request, session, flash 
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Product 
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session
from flask import flash  # 👈 Adicione esta linha

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # 👈 Chave definida
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitevenun.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco com o app
db.init_app(app) 

# Render Index
@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/logout')
def logout():
    # Remove a informação do usuário armazenada na sessão
    session.pop('user_id', None)
    # Redireciona para a página de login (ou outra de sua escolha)
    return redirect(url_for('login'))

# Render Login (exibe a página de login)
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_handler', methods=['POST'])
def login_handler():
    email = request.form.get('login-form-email')
    password = request.form.get('login-form-password')

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.senha, password):
        # Armazena o ID do usuário na sessão
        session['user_id'] = user.id
        return redirect(url_for('index'))  # Login bem-sucedido
    return redirect(url_for('login'))  # Login mal-sucedido

# Render Register (exibe a página de registro)
from flask import flash  # Certifique-se de importar flash

# ... (outras importações)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form.get('register-form-name')
        email = request.form.get('register-form-email')
        password = request.form.get('register-form-password')
        repassword = request.form.get('register-form-repassword')

        # Verifica se o e-mail já está cadastrado
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Este e-mail já está em uso!', 'error')
            return redirect(url_for('register'))
        
        # Verifica se as senhas coincidem
        if password != repassword:
            flash('As senhas não coincidem!', 'error')
            return redirect(url_for('register'))

        # Cria o novo usuário se tudo estiver válido
        try:
            senha_hash = generate_password_hash(password)
            user = User(
                nome=nome, 
                email=email, 
                username=nome,  # Assume que username = nome
                phone='', 
                senha=senha_hash
            )
            
            db.session.add(user)
            db.session.commit()
            flash('Registro realizado com sucesso! Faça login.', 'success')
            return redirect(url_for('login'))
            
        except Exception as e:
            db.session.rollback()
            flash('Erro ao registrar usuário. Tente novamente.', 'error')
            return redirect(url_for('register'))

    # Caso seja GET, exibe o formulário
    return render_template('register.html')

@app.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))
    user = User.query.get(user_id)
    if not user:
        return redirect(url_for('login'))
    return render_template('profile.html', user_html=user)

# Render Cart
@app.route('/cart')
def cart():
    return render_template('cart.html')

# Render Cart
@app.route('/add_to_cart')
def add_to_cart():
    return render_template('cart.html')

@app.route('/shop_single')
def shop_single(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('shop_single.html')

# Render shop
@app.route('/shop')
def shop():
    return render_template('shop.html')

# Render 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Banco de dados criado com sucesso!")
    app.run(debug=True)
