def is_prime(no):
    if no <= 1:
        return False
    for i in range(2, int(no ** 0.5) + 1):
        if no % i == 0:
            return False
    return True

def main():
    num = int(input("Enter number: "))
    if is_prime(num):
        print("It is Prime Number")
    else:
        print("It is Not Prime Number")

if __name__ == "__main__":
    main()