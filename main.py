import openai as ai #Importamos Open_ai

ai.api_key = "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" #Usamos nuestra API Key
from txt_pdf import convertir as c

def table():
    while True: #Creamos un bucle para repetir la pregunta a la preposición
        prompt = input("Preposicion: ") #Recivimos una preposición
        if prompt == "exit": 
            break #Si la preposición es exit, saldremos del programa
        else: #Si la preposición no es exit
            imprimir = int(input("¿Deseas imprimir la tabla en pdf? \n 1- si \n 2- no \n")) #Preguntamos si desea imprimir
            #Request es la petición al modelo de OpenAI
            request = "Haz una tabla de verdad con la siguiente preposición: " + prompt + " usando 'V' para representar True y 'F' para False" 
            #Response es la respuesta a la petición
            response = ai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125", #Modelo
                messages=[
                    {"role": "system", "content": "You are a chat model."},
                    {"role": "user", "content": request}#Pedimos que request sea enviada a un modelo de chat
                ])
            with open("out/tabla.txt", "w") as archivo:
                archivo.write(response["choices"][0]["message"]["content"])
                
            
            if imprimir == 1:#Si queremos imprimir, lo hacemos en un txt:
                archivo = open("out/tabla.txt", "r")
                c(archivo)
                print("Tabla creada")
            else:
                #Caso contrario, imprimimos en la consola
                print(" \n\n", response["choices"][0]["message"]["content"], "\n")

table()