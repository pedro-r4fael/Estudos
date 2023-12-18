# try, except, else e finally

try:
    print("Abrir arquivo")
    8/0

except ZeroDivisionError:
    print("Dividiu zero")    

else: # o else vai ser executado caso não ocorra erro no código
    print("Não deu erro")

finally: # sempre será executado, msm com erro a partir do try
    print("Fechar arquivo")

# link das hierarquia da exceções (para tratar erros com except)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions