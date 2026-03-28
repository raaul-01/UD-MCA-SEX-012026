from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

def conectar():
    return sqlite3.connect('database.db', check_same_thread=False)

# Cria a tabela inicial
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

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)