import mysql.connector
from flask import Flask, render_template, request, redirect;

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mateusSena'

#crie sua conexao com o BD (precisa do host, user, password e o database )
conexao = mysql.connector.connect(host='localhost', database='bdcrud', user='root', password='')
#crie sua conexao com o "cursor" (ele é responsável por executar os comandos)
cursor = conexao.cursor()

#CREATE
nome_produto ="refrigerante"
valor = 9
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()

#READ
comando = f'select * from vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

#UPDATE
nome_produto = "chocolate"
valor = 8
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

#DELETE
nome_produto = "bola"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()






#encerrando a conexão
cursor.close()
conexao.close()


if __name__ in '__main__':
    app.run(debug=True)