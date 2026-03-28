from flask import Flask, render_template, request, jsonify
import sqlite3
import ast

app = Flask(__name__)

# 🔌 Conexão com banco
def conectar():
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
        dado = ast.literal_eval(r[0])

        elemento = dado.get("elemento")
        texto = dado.get("texto")

        # 🔄 Traduzir nomes técnicos
        mapa = {
            "H1": "Título",
            "H2": "Seção",
            "BUTTON": "Botão",
            "A": "Link",
            "INPUT": "Campo de texto"
        }

        elemento = mapa.get(elemento, elemento)

        # 🚫 Ignorar elementos irrelevantes
        if elemento in ["BODY", "DIV", "FORM", "SELECT", "HTML"]:
            continue

        # 🧹 Limpar texto
        if texto:
            texto = texto.strip()

        if not texto:
            texto = elemento

        # 🚫 Ignorar textos muito grandes
        if len(texto) > 50:
            continue

        chave = (elemento, texto)

        if chave in contagem:
            contagem[chave] += 1
        else:
            contagem[chave] = 1

    return render_template("dashboard.html", contagem=contagem)

# 📥 Receber dados do frontend
@app.route('/coletar', methods=['POST'])
def coletar():
    data = request.json

    print("Recebido:", data)

    conn = conectar()
    c = conn.cursor()

    c.execute("INSERT INTO dados (tipo, conteudo) VALUES (?, ?)",
              (data.get("tipo"), str(data)))

    conn.commit()
    conn.close()

    return jsonify({"status": "ok"})

# ▶️ Rodar servidor
app.run(host="0.0.0.0", port=5000, debug=True)