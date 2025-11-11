import os

print("=" * 60)
print("OS MODULE BASICS - Key Capabilities")
print("=" * 60)

# 1. Get current working directory
print("\n1. DIRECTORY OPERATIONS")
print(f"Current working directory: {os.getcwd()}")

# 2. List directory contents
print(f"\nContents of current directory:")
contents = os.listdir('.')
for item in contents[:5]:  # Show first 5 items
    print(f"  - {item}")

# 3. Environment variables
print("\n2. ENVIRONMENT VARIABLES")
print(f"Home directory: {os.environ.get('HOME', 'Not set')}")
print(f"Path variable: {os.environ.get('PATH', 'Not set')[:50]}...")

# 4. Path operations
print("\n3. PATH OPERATIONS")
sample_path = "/home/user/documents/file.txt"
print(f"Sample path: {sample_path}")
print(f"  Directory name: {os.path.dirname(sample_path)}")
print(f"  Base name: {os.path.basename(sample_path)}")
print(f"  Split extension: {os.path.splitext(sample_path)}")
print(f"  Join paths: {os.path.join('folder', 'subfolder', 'file.txt')}")

# 5. File/Directory checks
print("\n4. FILE/DIRECTORY CHECKS")
print(f"  Current directory exists: {os.path.exists('.')}")
print(f"  Is directory: {os.path.isdir('.')}")
print(f"  Is file: {os.path.isfile('.')}")

# 6. System information
print("\n5. SYSTEM INFORMATION")
print(f"  Operating system: {os.name}")
print(f"  Path separator: '{os.sep}'")
print(f"  Line separator: {repr(os.linesep)}")

# 7. Process information
print("\n6. PROCESS INFORMATION")
print(f"  Process ID: {os.getpid()}")

print("\n" + "=" * 60)
print("Common os module capabilities:")
print("  - Directory navigation (chdir, getcwd, listdir)")
print("  - File operations (remove, rename, stat)")
print("  - Directory management (mkdir, rmdir, makedirs)")
print("  - Path manipulation (join, split, exists, isfile)")
print("  - Environment variables (environ, getenv)")
print("  - Process management (system, exec, fork)")
print("=" * 60)
