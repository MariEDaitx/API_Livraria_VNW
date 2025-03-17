import sqlite3
from flask import Flask, request, jsonify # type: ignore

app = Flask(__name__)

def int_db():
    with sqlite3.connect("database.db") as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS LIVROS(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                titulo TEXT NOT NULL,
                categoria TEXT NOT NULL,
                autor TEXT NOT NULL,
                image_url TEXT NOT NULL
            )
            """
        )
int_db()

@app.route("/")
def livrosvnw():
    return "Seja bem vindo!"

@app.route("/Doar", methods=["POST"])
def Doar():
    dados = request.get_json()
    print(f"AQUI ESTARÃO TODOS OS LIVROS DOADOS {dados}")

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor =  dados.get("autor")
    image_url = dados.get("image_url")

    if not titulo or not categoria or not image_url:
        return jsonify({"erro":"É obrigatório preencher todos os campos"}),400
    
    with sqlite3.connect("database.db") as conn:
        conn.execute(f"""
        INSERT INTO LIVROS (titulo, categoria, autor, image_url)
        VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
        """)

    conn.commit()
    return jsonify({"Mensagem": "Livro cadastrado com sucesso obrigada!"}), 201

if __name__ == "__main__":
   app.run(debug=True)
