from flask import Flask, render_template, request, jsonify
import sqlite3
import ast
import os

app = Flask(__name__)

def conectar():
    return sqlite3.connect('database.db', check_same_thread=False)

# Garante que a tabela suporte todos os tipos de dados (click, tempo, feedback, perfil)
with conectar() as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS dados (id INTEGER PRIMARY KEY AUTOINCREMENT, tipo TEXT, conteudo TEXT)')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coletar', methods=['POST'])
def coletar():
    try:
        dados = request.json
        tipo = dados.get("tipo")
        with conectar() as conn:
            conn.execute("INSERT INTO dados (tipo, conteudo) VALUES (?, ?)", (tipo, str(dados)))
        return jsonify({"status": "sucesso"})
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": str(e)}), 500

@app.route('/usuarios')
def lista_usuarios():
    try:
        with conectar() as conn:
            cursor = conn.cursor()
            # Filtra apenas o que for 'perfil' para a lista não virar uma bagunça de cliques
            cursor.execute("SELECT conteudo FROM dados WHERE tipo = 'perfil'")
            registros = cursor.fetchall()

        perfis = [ast.literal_eval(r[0]) for r in registros]
        return render_template("usuarios.html", perfis=perfis)
    except Exception as e:
        return f"Erro ao listar: {e}", 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)