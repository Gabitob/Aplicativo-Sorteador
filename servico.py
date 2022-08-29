import numpy as np

class Servico():
    def sortear(lista: list):
        result = np.random.choice(lista, 1)
        result = str(result)
        return result