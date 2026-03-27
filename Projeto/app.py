from flask import Flask, render_template, request, jsonify
import sqlite3
import ast
import os

app = Flask(__name__)

# Função para conectar ao banco
def conectar():
    # Usando check_same_thread=False para evitar erros no servidor
    conn = sqlite3.connect('database.db', check_same_thread=False)
    return conn

# Criar a tabela se não existir
with conectar() as conn:
    conn.execute('''CREATE TABLE IF NOT EXISTS dados 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                     tipo TEXT, 
                     conteudo TEXT)''')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coletar', methods=['POST'])
def coletar():
    try:
        dados = request.json
        tipo = dados.get("tipo")
        conteudo = str(dados)

        with conectar() as conn:
            conn.execute("INSERT INTO dados (tipo, conteudo) VALUES (?, ?)", (tipo, conteudo))
        
        return jsonify({"status": "sucesso"})
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": str(e)}), 500

@app.route('/usuarios')
def lista_usuarios():
    try:
        with conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT conteudo FROM dados WHERE tipo = 'perfil'")
            registros = cursor.fetchall()

        perfis = []
        for r in registros:
            try:
                # Converte a string do banco em dicionário
                perfis.append(ast.literal_eval(r[0]))
            except:
                continue

        return render_template("usuarios.html", perfis=perfis)
    except Exception as e:
        return f"Erro ao carregar usuários: {e}", 500

if __name__ == '__main__':
    # O Render usa a variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)