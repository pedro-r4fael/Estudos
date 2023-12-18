
import Aula100_package.modulo # Módulo é o arquivo que fica todo o conteudo digitado pelo Dev 
from Aula100_package import modulo
from Aula100_package.modulo import * #má pratica de prog, nao utilzar
# from Aula100_package.modulo import soma_do_modulo

# https://stackoverflow.com/questions/2386714/why-is-import-bad

print(soma_do_modulo(5,1))
print(Aula100_package.modulo.soma_do_modulo(5,1))
print(modulo.soma_do_modulo(5,1))
print(variavel)
print(nova_variavel)

