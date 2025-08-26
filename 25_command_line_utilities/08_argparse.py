import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("num1", type=float, help="First Number")
    parser.add_argument("num2", type=float, help="Second Number")
    parser.add_argument("operation", choices=["add", "sub", "div", "mul"], help="Operation to perform")

    args = parser.parse_args()
    print(args)
    print(type(args))

    if args.operation == "add":
        print(f"The result is {args.num1 + args.num2}")
    elif args.operation == "sub":
        print(f"The result is {args.num1 - args.num2}")  
    elif args.operation == "mul":
        print(f"The result is {args.num1 * args.num2}")
    elif args.operation == "div":
        if args.num2 != 0:
            print(f"The result is {args.num1 / args.num2}")
        else:
            print("Error: Division by zero")

if __name__ == "__main__":
    print("Hello World!!")
    main()
