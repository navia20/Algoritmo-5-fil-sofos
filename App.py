import threading
import time
import random

# Atributos inicio
num_filosofos = 5
tenedores = [False] * num_filosofos
condicion = threading.Condition()

def coger_tenedores(i):
    #El ciclo de vida de un filósofo que alterna entre pensar y comer
    with condicion:
        # Esperar mientras cualquiera de los tenedores está en uso
        while tenedores[i] or tenedores[i - 1]:
            condicion.wait()
        # Marcar ambos tenedores como en uso
        tenedores[i] = tenedores[i - 1] = True

#El filósofo deja los tenedores izquierdo y derecho.
def dejar_tenedores(i):
    
    with condicion:
        # Marcar ambos tenedores como libres
        tenedores[i] = tenedores[i - 1] = False
        # Notificar a todos los filósofos en espera
        condicion.notify_all()

#El ciclo de vida de un filósofo que alterna entre pensar y comer
def filosofo(i):
    while True:
        print(f"Filosofo {i + 1} está pensando")
        time.sleep(random.uniform(0, 4))  # Tiempo para pensar que varian entre 0 y 4 tiempos 
        coger_tenedores(i)
        print(f"Filosofo {i + 1} está comiendo")
        time.sleep(random.uniform(0, 4))  # Tiempo para comer que varian entre 0 y 4 tiempos 
        print(f"Filosofo {i + 1} deja de comer, tenedores libres {i + 1}, {i if i > 0 else num_filosofos}")
        dejar_tenedores(i)

# Crear y iniciar los hilos de los filósofos
filosofos = []
for i in range(num_filosofos):
    hilo = threading.Thread(target=filosofo, args=(i,))
    filosofos.append(hilo)
    hilo.start()