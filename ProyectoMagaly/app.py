import os
from flask import Flask, render_template, request, jsonify

# Esto soluciona el error de "No such file or directory"
base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, 
            template_folder=os.path.join(base_dir, 'templates'),
            static_folder=os.path.join(base_dir, 'static'))

INFO_HISTORIA = {
    "nombre": "Magaly",
    "aniversario": "21 de Julio de 2025",
    "brackets": "morado y celeste",
    "comida": "sushi (por lo que me has dicho)",
    "primer_beso": "en el grado, estabmos nerviosos",
    "recuerdo_lindo": "arreglar tu cuarto aun asi estando enfermo"
}

def respuesta_ia(texto):
    t = texto.lower()
    if "aniversario" in t:
        return f"Nuestro aniversario es el {INFO_HISTORIA['aniversario']} ❤️. ¡Supimos salir adelante y hoy somos más fuertes! ✨"
    elif "beso" in t:
        return "Aquel primer beso en el grado... ¡qué nervios de que nos vieran! 💋 Fue el mejor inicio."
    elif "cuarto" in t or "enfermo" in t:
        return "Ese momento fue muy especial... aunque estaba enfermo, arreglar tu cuarto y estar contigo fue lo mejor ❤️."
    elif "comer" in t or "plan" in t:
        return f"¿Qué tal un poco de {INFO_HISTORIA['comida']} 🍣 y jugamos algo juntos? ¡Me encanta pasar tiempo contigo! 🎮"
    elif "brackets" in t or "color" in t:
        return f"Me encantan tus ligas {INFO_HISTORIA['brackets']}, ¡te ves preciosa! 😍"
    else:
        return "¡Hola Magaly! Eres la niña más linda del mundo. ¿En qué puedo ayudarte hoy? ❤️✨"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    pregunta = data.get("msg", "")
    respuesta = respuesta_ia(pregunta)
    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    print("Servidor iniciado en http://127.0.0.1:5000")
    app.run(debug=True, port=5000)