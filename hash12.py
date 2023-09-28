def hash_function(key):
    return key % A.length

def main():
    A = [None] * 10
    A[hash_function(12)] = 10

    print(A[hash_function(12)])

if __name__ == "__main__":
    main()
