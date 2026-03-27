import os
import sqlite3
import ast
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Função para conectar ao banco de dados
def conectar():
    conn = sqlite3.connect('database.db')
    return conn

# Criar a tabela se não existir
conn = conectar()
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS dados (id INTEGER PRIMARY KEY AUTOINCREMENT, tipo TEXT, conteudo TEXT)''')
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coletar', methods=['POST'])
def coletar():
    dados = request.json
    tipo = dados.get("tipo")
    conteudo = str(dados)

    conn = conectar()
    c = conn.cursor()
    c.execute("INSERT INTO dados (tipo, conteudo) VALUES (?, ?)", (tipo, conteudo))
    conn.commit()
    conn.close()
    
    return jsonify({"status": "sucesso"})

# NOVA ROTA: Listar perfis cadastrados
@app.route('/usuarios')
def lista_usuarios():
    conn = conectar()
    c = conn.cursor()
    # Busca apenas os registros do tipo 'perfil'
    c.execute("SELECT conteudo FROM dados WHERE tipo = 'perfil'")
    registros = c.fetchall()
    conn.close()

    perfis = []
    for r in registros:
        try:
            # Converte a string do banco de volta para dicionário Python
            perfis.append(ast.literal_eval(r[0]))
        except:
            continue

    return render_template("usuarios.html", perfis=perfis)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)