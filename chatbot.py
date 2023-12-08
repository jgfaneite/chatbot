import nltk
from nltk.chat.util import Chat, reflections

# Configuración de pares de entrada y salida para el chatbot
pairs = [
    ["Hola", ["¡Hola!", "¿Cómo estás?"]],
    ["¿Cuál es tu nombre?", ["Soy un chatbot.", "Mi nombre es Bot."]],
    ["Despedida", ["Hasta luego.", "¡Adiós!", "Chao", "Nos vemos", "Salir"]],
    ["Tengo una pregunta", ["Claro, pregunta lo que quieras."]],
    ["", ["No entiendo. ¿Puedes reformular tu pregunta?"]],
]

# Crea un objeto Chat con los pares definidos
chatbot = Chat(pairs, reflections)

# Función principal para interactuar con el chatbot
def chat():
    print("¡Hola! Soy un chatbot. Puedes preguntarme lo que quieras. Para salir, escribe una de las siguientes opciones: 'Despedida'")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ["adiós", "hasta luego", "chao", "nos vemos", "salir"]:
            print("¡Hasta luego!")
            break
        response = chatbot.respond(user_input)
        print(f"Bot: {response}")

# Llama a la función principal
if __name__ == "__main__":
    nltk.download("punkt")
    chat()

