def count_digits(no):
    return len(str(abs(no)))

def main():
    num = int(input("Enter number: "))
    print("Number of digits:", count_digits(num))

if __name__ == "__main__":
    main()