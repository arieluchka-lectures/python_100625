
import argparse

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(
        description='Demo script showing argparse usage',
        epilog='Example: python argparse_demo.py --name John --age 25 --verbose'
    )

    # Add positional arguments (required by default)
    parser.add_argument(
        'operation',
        help='Operation to perform: greet, calculate, or info'
    )

    # Add optional arguments with -- prefix
    parser.add_argument(
        '--name',
        '-n',
        type=str,
        default='User',
        help='Your name (default: User)'
    )

    parser.add_argument(
        '--age',
        '-a',
        type=int,
        help='Your age'
    )

    # Add a flag (boolean) argument
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Enable verbose output'
    )

    # Arguments for calculator operation
    parser.add_argument(
        '--num1',
        type=float,
        help='First number for calculation'
    )

    parser.add_argument(
        '--num2',
        type=float,
        help='Second number for calculation'
    )

    parser.add_argument(
        '--operator',
        choices=['+', '-', '*', '/'],
        help='Operator for calculation: +, -, *, /'
    )

    # Parse the arguments
    args = parser.parse_args()

    # Use the parsed arguments
    print("=" * 60)
    print("Argparse Demo - Parsed Arguments")
    print("=" * 60)

    if args.verbose:
        print(f"\n[VERBOSE] Operation: {args.operation}")
        print(f"[VERBOSE] Name: {args.name}")
        print(f"[VERBOSE] Age: {args.age}")
        print(f"[VERBOSE] Verbose mode: {args.verbose}")

    print()

    # Execute based on operation
    if args.operation == 'greet':
        print(f"Hello, {args.name}!")
        if args.age:
            print(f"You are {args.age} years old.")

    elif args.operation == 'calculate':
        if args.num1 is not None and args.num2 is not None and args.operator:
            if args.operator == '+':
                result = args.num1 + args.num2
            elif args.operator == '-':
                result = args.num1 - args.num2
            elif args.operator == '*':
                result = args.num1 * args.num2
            elif args.operator == '/':
                result = args.num1 / args.num2 if args.num2 != 0 else "Error: Division by zero"

            print(f"Calculation: {args.num1} {args.operator} {args.num2} = {result}")
        else:
            print("Error: For calculate operation, provide --num1, --num2, and --operator")

    elif args.operation == 'info':
        print(f"User: {args.name}")
        print(f"Age: {args.age if args.age else 'Not provided'}")
        print(f"Verbose: {'Enabled' if args.verbose else 'Disabled'}")

    else:
        print(f"Unknown operation: {args.operation}")
        print("Available operations: greet, calculate, info")

if __name__ == "__main__":
    main()
