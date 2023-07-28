# Python 3: Fibonacci series up to n
def fib(n):
   a, b = 0, 1
   while a < n:
       print(a, end=' ')
       a, b = b, a+b

def main():
    n = int(input("Enter an integer number n  = "))
    print("Fibonacci series up to ", n, ":")
    fib(n)
if __name__ == "__main__":
    main()
