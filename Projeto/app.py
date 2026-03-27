from flask import Flask, render_template, request, jsonify
import sqlite3
import ast
import os  # Essencial para ler a porta do Render

app = Flask(__name__)

# 🔌 Conexão com banco
def conectar():
    # Nota: No Render, o banco será resetado a cada deploy no plano gratuito
    return sqlite3.connect("database.db")

# 🧱 Criar banco
def criar_banco():
    conn = conectar()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS dados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT,
        conteudo TEXT
    )
    """)
    conn.commit()
    conn.close()

# Executa a criação do banco ao iniciar o app
criar_banco()

# 🏠 Página inicial
@app.route('/')
def home():
    return render_template("index.html")

# 🛍️ Página de produtos
@app.route('/produtos')
def produtos():
    lista_produtos = [
        {"nome": "Notebook", "preco": "R$ 3500"},
        {"nome": "Celular", "preco": "R$ 2000"},
        {"nome": "Fone de ouvido", "preco": "R$ 160"},
        {"nome": "Mouse Pad", "preco": "R$ 10,50"},
        {"nome": "Cadeira Gamer", "preco": "R$ 1200"},
        {"nome": "Quadro", "preco": "R$ 300"}
    ]
    return render_template("produtos.html", produtos=lista_produtos)

# 📊 Dashboard
@app.route('/dashboard')
def dashboard():
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT conteudo FROM dados WHERE tipo = 'click'")
    registros = c.fetchall()
    conn.close()

    contagem = {}
    for r in registros:
        try:
            dado = ast.literal_eval(r[0])
            elemento = dado.get("elemento")
            texto = dado.get("texto")

            mapa = {
                "H1": "Título",
                "H2": "Seção",
                "BUTTON": "Botão",
                "A": "Link",
                "INPUT": "Campo de texto"
            }

            elemento = mapa.get(elemento, elemento)

            if elemento in ["BODY", "DIV", "FORM", "SELECT", "HTML"]:
                continue

            if texto:
                texto = texto.strip()

            if not texto:
                texto = elemento

            if len(texto) > 50:
                continue

            chave = (elemento, texto)
            contagem[chave] = contagem.get(chave, 0) + 1
        except:
            continue

    return render_template("dashboard.html", contagem=contagem)

# 📥 Receber dados do frontend
@app.route('/coletar', methods=['POST'])
def coletar():
    data = request.json
    conn = conectar()
    c = conn.cursor()
    c.execute("INSERT INTO dados (tipo, conteudo) VALUES (?, ?)",
              (data.get("tipo"), str(data)))
    conn.commit()
    conn.close()
    return jsonify({"status": "ok"})

# ▶️ Rodar servidor (AJUSTADO PARA O RENDER)
if __name__ == "__main__":
    # Tenta pegar a porta do servidor (Render), se não existir (PC), usa a 5000
    port = int(os.environ.get("PORT", 5000))
    # No PC (porta 5000) o debug fica ligado, no Render (outra porta) ele desliga
    app.run(host="0.0.0.0", port=port, debug=(port == 5000))