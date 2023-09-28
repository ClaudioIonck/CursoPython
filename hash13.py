def hash(key, tamanho):
  return key % tamanho

def main():
  chave = 12
  tamanho = 10
  posicao = hash(chave, tamanho)
  print(f" {chave} {posicao}")

if __name__ == "__main__":
  main()
