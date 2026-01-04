def factorial(no):
    result = 1
    for i in range(1, no + 1):
        result *= i
    return result

def main():
    num = int(input("Enter number: "))
    print("Factorial:", factorial(num))

if __name__ == "__main__":
    main()