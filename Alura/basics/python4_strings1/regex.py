import re 

a = "Olá, ligue me em 924593-4443"
b = "Meu telefone é 942593-4443"
c = "Boa tarde,23433-2341 estou ligadno no numero 12111-5555 devido a 1222-32223"

padrao = "[0-9]{4,5}-?[0-9]{4}"

telefone = re.search(padrao, a)
print(telefone.group())

telefone = re.search(padrao, b)
print(telefone.group())

telefone = re.findall(padrao, c)
print(telefone)

#https://realpython.com/regex-python/


if url == "bytebank.com.br":
    return True
else:
    return False
