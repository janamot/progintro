while True:
    n = int(input("výška:"))
    if n % 2 != 0:
        for i in range(n):
            if i <= int(n/2):
                p = 2*i+1
            else:
                p = 2*(n - i) -1
            mezera = int((n-p)/2)
            print(" " * mezera, "*" * p, " " * mezera)
        break    
    else:
        print("zadejte liché, nezáporné číslo")