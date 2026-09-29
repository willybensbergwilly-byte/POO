from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from models.avaliacoes import Avaliacoes
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato
from models.usuario import Usuario
from repositories import usuario_repository, restaurante_repository, avaliacao_repository, cardapio_repository

app = Flask(__name__)
app.secret_key = '~~WrbdskmNN777'

def login_required(funcao):
    @wraps(funcao)
    def verificar(*args, **kwargs):
        if 'id_usuario' not in session:
            return redirect(url_for('login'))
        else:
            return funcao(*args, *kwargs)
    return verificar


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha_hash = generate_password_hash(request.form['senha'])
        if usuario_repository.buscar_por_email(email) is not None:
            return render_template('cadastro.html', erro='Este e-mail já esta cadastrado.')
        else:
            usuario = Usuario(nome, email, senha_hash)
            usuario_repository.criar_usuario(usuario)
            return redirect(url_for('login'))
    else:
        return render_template('cadastro.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        usuario = usuario_repository.buscar_por_email(email)
        if usuario and check_password_hash(usuario._senha_hash, senha):
            session['id_usuario'] = usuario.id
            return redirect(url_for('painel'))
        else:
            return render_template('login.html', erro='E-mail ou senha inválidos.')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('id_usuario', None)
    return redirect(url_for('login'))

@app.route('/painel')
@login_required
def painel():
    usuario = usuario_repository.buscar_por_email(session['id_usuario'])
    return render_template('painel.html', usuario=usuario)

@app.route('/restaurantes')
@login_required
def restaurantes():
    lista_restaurantes = restaurante_repository.listar_restaurantes()
    return render_template('restaurantes.html', restaurantes=lista_restaurantes)

@app.route('/restaurante/<int:id_restaurante>/avaliar', methods=['GET','POST'])
@login_required
def avaliar_restaurante(id_restaurante):
    restaurante = restaurante_repository.buscar_por_id(id_restaurante)
    if restaurante is None:
        return redirect(url_for('restaurantes'))
    elif request.method == 'POST':
        cliente = request.form['cliente']
        nota = float(request.form['nota'])
        avalicao = Avaliacoes(cliente, nota)
        avaliacao_repository.criar_avaliacao(id_restaurante, avalicao)
        return redirect(url_for('listar_avaliacoes',id_restaurante=id_restaurante))
    return render_template('avaliar.html', restaurante=restaurante)

@app.route('/restaurante/<int:id_restaurante>/avaliacoes')
@login_required
def listar_avaliacoes(id_restaurante):
    restaurante = restaurante_repository.listar_completo(id_restaurante)
    if restaurante is None:
        return redirect(url_for('restaurantes'))
    return render_template('avaliacoes.html', restaurante=restaurante)

@app.route('/restaurante/<int:id_restaurante>/cardapio')
@login_required
def listar_cardapio(id_restaurante):
    restaurante = restaurante_repository.buscar_por_id(id_restaurante)
    if restaurante is None:
        return redirect(url_for('restaurantes'))
    itens = cardapio_repository.listar_por_restaurante(id_restaurante)

    pratos = [item for item in itens if isinstance(item, Prato)]
    bebidas = [item for item in itens if isinstance(item, Bebida)]

    return render_template('cardapio.html', restaurante=restaurante, pratos=pratos, bebidas=bebidas)

if __name__ == '__main__':
    restaurante_repository.tabela_restaurante()
    avaliacao_repository.tabela_avaliacao()
    cardapio_repository.tabela_item_cardapio()
    usuario_repository.tabela_usuario()
    app.run(debug=True)