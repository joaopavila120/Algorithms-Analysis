def fibonacci(n):
    ultimo=1
    penultimo=1

    if (n==1) or (n==2):
        print("1")
    else:
        for count in range(2,n):
            termo = ultimo + penultimo
            penultimo = ultimo
            ultimo = termo
            count += 1
        print(termo)
    
#fibonacci(6)

import cProfile
import re
cProfile.runctx('fibonacci(6)', None, locals())



#links
#https://wagnergaspar.com/comparando-o-algoritmo-de-fibonacci-recursivo-e-iterativo-tempo-de-execucao/
