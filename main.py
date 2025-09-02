from fibonacci import generate_fibonacci

def main():
    # Ask user for the number of terms
    n = int(input("Enter the number of Fibonacci terms: "))

    # Generate the Fibonacci sequence
    sequence = generate_fibonacci(n)

    # Display the sequence
    print("Fibonacci sequence:")
    print(", ".join(map(str, sequence)))


if __name__ == "__main__":
    main()
