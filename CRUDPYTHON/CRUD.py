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

@app.route('/paginaeditarproduto/<int:idVendas>', methods=['GET'])
def editarproduto(idVendas):
    conexao = mysql.connector.connect(host='localhost', database='bdcrud', user='root', password='')
    cursor = conexao.cursor()
    comando = 'SELECT nome_produto, valor FROM vendas WHERE idVendas = %s'
    cursor.execute(comando, (idVendas,))
    produto = cursor.fetchone()
    cursor.close()
    conexao.close()
    if produto:
        nome, valor = produto
    else:
        nome, valor = '', 0
    return render_template('editarproduto.html', idVendas=idVendas, nome=nome, valor=valor)

@app.route('/editando', methods=['POST'])
def editando():
    idVendas = request.form['id']
    nome = request.form['nomeProduto']
    valor = request.form['precoProduto']
    
    conexao = mysql.connector.connect(host='localhost', database='bdcrud', user='root', password='')
    cursor = conexao.cursor()
    comando = 'UPDATE vendas SET nome_produto = %s, valor = %s WHERE idVendas = %s'
    cursor.execute(comando, (nome, valor, idVendas))
    conexao.commit()
    cursor.close()
    conexao.close()
    
    return redirect('/paginaupdate')

#EXCLUIR
@app.route('/paginaexcluir') 
def paginaexcluir():
    conexao = mysql.connector.connect(host='localhost', database='bdcrud', user='root', password='')
    cursor = conexao.cursor()
    comando = f'select * from vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template('delete.html', produtos=resultado)

@app.route('/excluirproduto/<int:idVendas>', methods=['GET'])
def excluirproduto(idVendas):
    conexao = mysql.connector.connect(host='localhost', database='bdcrud', user='root', password='')
    cursor = conexao.cursor()
    comando = 'DELETE FROM vendas WHERE idVendas = %s'
    cursor.execute(comando, (idVendas,))
    conexao.commit()
    cursor.close()
    conexao.close()
    
    return redirect('/paginaexcluir')

if __name__ in '__main__':
    app.run(debug=True)