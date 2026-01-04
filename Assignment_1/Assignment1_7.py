def DivisibleByFive(no):
    return no % 5 == 0

def main():
    num = int(input("Enter number: "))
    print(DivisibleByFive(num))

if __name__ == "__main__":
    main()