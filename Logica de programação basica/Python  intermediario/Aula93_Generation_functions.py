# Introdução ás Generator functions em Python
# generator = (n for n in range(100))

def generator(n=0):
    yield 1 # Pausar
    print("Continuando...")
    yield 2 # Pausar
    print("Mais uma...")
    yield 3 # Pausar
    print("Vou terminar")
    return "Acabou!"

gen = generator(n=0)

for n in gen:
    print(n)

## outro exemplo

# def generator(n=0, maximum=10):
#     while True:
#         yield n
#         n += 1

#         if n >= maximum:
#             return


# gen = generator(maximum=1000000)
# for n in gen:
#     print(n)