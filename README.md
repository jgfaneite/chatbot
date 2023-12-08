# chatbot
Ejemplo simple de un chatbot creado el Phyton, Computacion Emergentes

* * *
## chatbot.py - Documentación ##

### Descripción ###
El archivo chatbot.py implementa un simple chatbot en Python utilizando la biblioteca NLTK para procesamiento 
de lenguaje natural. El chatbot responde a ciertas entradas del usuario y proporciona respuestas predefinidas.

### Estructura del Código ###
El código está estructurado de la siguiente manera:

  *   1-Importación de bibliotecas:
    
            import nltk
            from nltk.chat.util import Chat, reflections

Importamos las bibliotecas necesarias para la implementación del chatbot. 
  
  *   2-Configuración de pares de entrada y salida:
  
            pairs = [
            ["Hola", ["¡Hola!", "¿Cómo estás?"]],
            ["¿Cuál es tu nombre?", ["Soy un chatbot.", "Mi nombre es Bot."]],
            ["Despedida", ["Hasta luego.", "¡Adiós!", "Chao", "Nos vemos", "Salir"]],
            ["Tengo una pregunta", ["Claro, pregunta lo que quieras."]],
            ["", ["No entiendo. ¿Puedes reformular tu pregunta?"]],
            ] 


Definimos los pares de entrada y salida que el chatbot utilizará para responder a ciertas interacciones.

   *  3-Creación del objeto Chat:   

            chatbot = Chat(pairs, reflections)

Creamos un objeto de la clase Chat con los pares definidos y las reflexiones.

   *  4-Función principal de interacción: 

            def chat():
                # ...
    
Implementamos una función principal llamada chat que controla la interacción del usuario con el chatbot.

   *  5-Llamada a la función principal: 

            if __name__ == "__main__":
                # ...
    
Descargamos los recursos necesarios de NLTK y llamamos a la función principal chat si el script se ejecuta directamente.

* * *
#### Uso ####

Para ejecutar el chatbot, simplemente ejecuta el archivo chatbot.py desde la línea de comandos.

         python chatbot.py

El chatbot saludará al usuario y esperará entradas. Puedes interactuar con él y salir escribiendo alguna de las opciones de despedida definidas.

