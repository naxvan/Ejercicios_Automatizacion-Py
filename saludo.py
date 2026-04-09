
import time

# esto es un script que da un saludo por consola cada 2 segundos 

MENSAJE = "Hola Buen dia"
PARAR = "Pare el mensaje con CTRL + C"
SEGUNDOS = 3

def saludar():
    print(MENSAJE)

while True:
   saludar()
   print(PARAR)
   time.sleep(SEGUNDOS)

