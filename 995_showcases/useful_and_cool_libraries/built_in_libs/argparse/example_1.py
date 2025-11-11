import argparse

# Step 1: Create the parser
parser = argparse.ArgumentParser(description='A friendly greeting app')

# Step 2: Add arguments
# This is a required argument (no dashes)
parser.add_argument('name', type=str, help='Your name')

# These are optional arguments (have dashes)
parser.add_argument('--age', type=int, help='Your age')

parser.add_argument('--greeting',
                    default='Hello',
                    help='Type of greeting (default: Hello)')

# This is a flag - it's either True or False
parser.add_argument('--excited', action='store_true',
                    help='Add excitement to the greeting!')

parser.add_argument('--uppercase', action='store_true',
                    help='Make the greeting LOUD')

# Step 3: Parse the arguments
args = parser.parse_args()

# Step 4: Build the greeting message
message = f"{args.greeting}, {args.name}!"

# Add age if provided
if args.age:
    message += f" You are {args.age} years old."

# Add excitement if flag is set
if args.excited:
    message += " 🎉"

# Make uppercase if flag is set
if args.uppercase:
    message = message.upper()

# Step 5: Show the result
print(message)