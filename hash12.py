#questao12
A_comprimento = 10

def hash_function(key):
    return key % A_comprimento

chave = 12

posicao = hash_function(chave)

print(f"{chave} {posicao}")