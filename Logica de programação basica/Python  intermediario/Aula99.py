import importlib
import Aula99_m 

print(Aula99_m.variavel)

for i in range(10):
    importlib.reload(Aula99_m)
    print(i)

print("Fim")