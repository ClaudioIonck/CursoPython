#questão 15
def hash_function(key):
    return key % 10

def main():
    table = {}
    table[1] = 10
    table[2] = 6
    table[4] = 5

    table[2] = None

    print(table)

if __name__ == "__main__":
    main()
