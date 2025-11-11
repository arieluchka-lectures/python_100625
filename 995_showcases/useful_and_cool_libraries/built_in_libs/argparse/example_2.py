import argparse
import os
from pathlib import Path

def list_files(args):
    """List files in a directory"""
    path = Path(args.directory)

    if not path.exists():
        print(f"Error: Directory '{args.directory}' does not exist")
        return

    if not path.is_dir():
        print(f"Error: '{args.directory}' is not a directory")
        return

    print(f"\nContents of '{args.directory}':")
    print("-" * 50)

    items = list(path.iterdir())

    if args.filter:
        items = [item for item in items if args.filter in item.name]

    if args.files_only:
        items = [item for item in items if item.is_file()]
    elif args.dirs_only:
        items = [item for item in items if item.is_dir()]

    for item in sorted(items):
        item_type = "DIR " if item.is_dir() else "FILE"
        size = f"({item.stat().st_size} bytes)" if item.is_file() else ""
        print(f"  [{item_type}] {item.name} {size}")

    print(f"\nTotal items: {len(items)}")

def create_file(args):
    """Create a new file"""
    path = Path(args.filename)

    if path.exists() and not args.force:
        print(f"Error: File '{args.filename}' already exists. Use --force to overwrite.")
        return

    try:
        with open(path, 'w') as f:
            if args.content:
                f.write(args.content)
        print(f"✓ Created file: {args.filename}")
    except Exception as e:
        print(f"Error creating file: {e}")

def delete_file(args):
    """Delete a file"""
    path = Path(args.filename)

    if not path.exists():
        print(f"Error: File '{args.filename}' does not exist")
        return

    if not args.confirm:
        print(f"Would delete '{args.filename}' (use --confirm to actually delete)")
        return

    try:
        path.unlink()
        print(f"✓ Deleted file: {args.filename}")
    except Exception as e:
        print(f"Error deleting file: {e}")

def main():
    # Create main parser
    parser = argparse.ArgumentParser(
        description='File Manager CLI - Manage files from the command line',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python file_manager.py list . --files-only
  python file_manager.py create test.txt --content "Hello World"
  python file_manager.py delete old_file.txt --confirm"""
    )

    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # List command
    list_parser = subparsers.add_parser('list', help='List files in a directory')
    list_parser.add_argument('directory', default='.', nargs='?', help='Directory to list (default: current)')
    list_parser.add_argument('--filter', '-f', help='Filter files by name')

    # Mutually exclusive group for file type filtering
    list_group = list_parser.add_mutually_exclusive_group()
    list_group.add_argument('--files-only', action='store_true', help='Show only files')
    list_group.add_argument('--dirs-only', action='store_true', help='Show only directories')

    # Create command
    create_parser = subparsers.add_parser('create', help='Create a new file')
    create_parser.add_argument('filename', help='Name of the file to create')
    create_parser.add_argument('--content', '-c', help='Content to write to the file')
    create_parser.add_argument('--force', action='store_true', help='Overwrite if file exists')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a file')
    delete_parser.add_argument('filename', help='Name of the file to delete')
    delete_parser.add_argument('--confirm', '-y', action='store_true', help='Skip confirmation prompt')

    # Parse arguments
    args = parser.parse_args()

    # Execute command
    if args.command == 'list':
        list_files(args)
    elif args.command == 'create':
        create_file(args)
    elif args.command == 'delete':
        delete_file(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()