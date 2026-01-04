def sum_of_digits(no):
    total = 0
    no = abs(no)
    while no > 0:
        total += no % 10
        no //= 10
    return total

def main():
    num = int(input("Enter number: "))
    print("Addition of digits:", sum_of_digits(num))

if __name__ == "__main__":
    main()