from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from models.usuario import Usuario
from repositories import usuario_rep, restaurante_rep, avaliacoes_rep, cardapio_rep
  
app = Flask(__name__) 
app.secret_key = '*&#&($¨(89729828D**#9873827074180908))'

def login_required(funcao):
    @wraps(funcao)
    def verificar(*args,**kwargs):
        if 'id_usuario' not in session:
            return redirect(url_for('login'))
        else:
            return (*args, *kwargs)
        return verificar
    
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro ():
    if request.methos  == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha_hash = generate_password_hash(request.form['senha'])
        if usuario_rep.buscar_email(email) is not None:
            return render_template('cadastro.html', erro = 'Este email já esta Cadastrado.')
        else:
            usuario = Usuario(nome, email, senha_hash)
            usuario_rep.criar_usuario(usuario)
            return redirect(url_for('login'))
        
    return render_template('cadastro.html')

@app.route('/login', method=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request['email']
        senha = request['senha']
        
        usuario = usuario_rep.buscar_email(email)
        if usuario and check_password_hash(usuario._senha_hash, senha):
            session['usuario_id'] = usuario.id
            return redirect(url_for('painel'))
        else:
            return render_template('login.html', erro='Email ou Senha Inválidos.')
    else:
        return render_template('login.html')
@app.route('/logout')
def logout():
    session.pop('id_usuario', None)
    return redirect(url_for('login.html'))

@app.route('/painel')
@login_required
def painnel():
    usuario = usuario_rep.buscar_por_email(session['usuario.id'])
    return render_template('painel.html', usuario=usuario)
@app.route('/restaurantes')
@login_required
def restaurantes():
    lista_restaurantes = restaurante_rep.listar_restaurantes()
    return render_template('restaurante.html', restaurantes=lista_restaurantes)

if __name__ == 'main':
    restaurante_rep.tabela_restaurante()
    avaliacoes_rep.tabela_avaliacoes()
    cardapio_rep.tabela_item_cardapio()
    usuario_rep.tabela_usuario()
     