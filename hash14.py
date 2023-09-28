#questão 14
def hash_function(key):
    return key % 10

def main():
    table = {}
    table[1] = 10
    table[2] = 6
    table[4] = 5

    del table[2]

    print(table)

if __name__ == "__main__":
    main()
