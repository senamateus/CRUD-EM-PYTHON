import mysql.connector

#crie sua conexao com o BD (precisa do host, user, password e o database )
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bdcrud',
)

#crie o seu "cursor" (ele é responsável por executar os comandos)
cursor = conexao.cursor()


















#encerrando a conexão
cursor.close()
conexao.close(  )