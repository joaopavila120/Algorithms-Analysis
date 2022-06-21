import random
from mergesort import mergesort

any_number = random.sample(range(1,1000), 42)

already_sorted = [1, 2, 3, 4, 5, 9, 20, 22, 38, 42, 87, 88, 89, 112]

inversed = [112, 89, 88, 87, 42, 38, 22, 20, 9, 5, 4, 3, 2, 1]

repeated = [7, 7, 7, 7,7,7,7,1,1,1,1,1,1, 9,9,9,9,9, 0, 4, 6, 9]

if __name__ == "__main__":
    test_cases = {'Números aleatórios': any_number,
                  'Já ordenados': already_sorted,
                  'Ordem inversa': inversed,
                  'Repetidos': repeated}
    
    for name, lista in test_cases.items():
        print("\nCaso de teste: {}".format(name))
        print(lista)
        mergesort(lista)
        print("\n Ordenados: ")
        print(lista)
    print("**************************** FIM ***************************")
