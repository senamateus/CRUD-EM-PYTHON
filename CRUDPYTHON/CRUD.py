import mysql.connector
from flask import Flask, render_template, request, redirect;

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mateusSena'


@app.route('/')
def index():
   return render_template('index.html')

#CREATE
@app.route('/paginacreate') 
def paginacreate():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def create():
    #crie sua conexao com o BD (precisa do host, user, password e o database ):    
    conexao = mysql.connector.connect(host='localhost', database='bdcrud', user='root', password='')
    #crie sua conexao com o "cursor" (ele é responsável por executar os comandos):
    cursor = conexao.cursor()
    nome_produto = request.form.get('nomeProduto')
    valor = request.form.get('precoProduto')
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect('/paginaread')

#READ
@app.route('/paginaread')
def paginaread():
    conexao = mysql.connector.connect(host='localhost', database='bdcrud', user='root', password='')
    cursor = conexao.cursor()
    comando = f'select * from vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template('read.html', produtos=resultado)

    
#UPDATE
@app.route('/paginaupdate') 
def paginaupdate():
    conexao = mysql.connector.connect(host='localhost', database='bdcrud', user='root', password='')
    cursor = conexao.cursor()
    comando = f'select * from vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template('update.html', produtos=resultado)

@app.route('/paginaeditarproduto',)
def editarproduto():
    return render_template('editarproduto.html')

@app.route('/editando', methods=['POST'])
def editando():
    conexao = mysql.connector.connect(host='localhost', database='bdcrud', user='root', password='')
    cursor = conexao.cursor()
    nome_produto = request.form.get('nomeProduto')
    valor = request.form.get('precoProduto')
    comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conexao.commit()
    return render_template('editarproduto.html')






#nome_produto = "chocolate"
#valor = 8
#comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit()

#DELETE
#nome_produto = "bola"
#comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit()






#encerrando a conexão



if __name__ in '__main__':
    app.run(debug=True)