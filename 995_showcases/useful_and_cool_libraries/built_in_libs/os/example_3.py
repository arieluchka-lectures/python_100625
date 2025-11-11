import os
from datetime import datetime

def get_size(path):
    """Get size of a file or directory in bytes."""
    total = 0
    try:
        if os.path.isfile(path):
            total = os.path.getsize(path)
        elif os.path.isdir(path):
            for entry in os.scandir(path):
                if entry.is_file(follow_symlinks=False):
                    total += entry.stat().st_size
                elif entry.is_dir(follow_symlinks=False):
                    total += get_size(entry.path)
    except PermissionError:
        pass
    except Exception:
        pass
    return total

def format_size(bytes_size):
    """Convert bytes to human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} PB"

def analyze_directory(directory, top_n=10):
    """
    Analyze directory and display statistics about files and subdirectories.
    """
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist!")
        return

    print("="*70)
    print(f"DISK SPACE ANALYSIS: {os.path.abspath(directory)}")
    print("="*70)

    # Collect information about all items
    items = []
    file_count = 0
    dir_count = 0

    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            try:
                size = get_size(item_path)
                is_dir = os.path.isdir(item_path)

                if is_dir:
                    dir_count += 1
                else:
                    file_count += 1

                # Get modification time
                mod_time = os.path.getmtime(item_path)
                mod_date = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M')

                items.append({
                    'name': item,
                    'size': size,
                    'formatted_size': format_size(size),
                    'is_dir': is_dir,
                    'modified': mod_date
                })
            except (PermissionError, OSError):
                continue

        # Sort by size (largest first)
        items.sort(key=lambda x: x['size'], reverse=True)

        # Calculate total size
        total_size = sum(item['size'] for item in items)

        # Display summary
        print(f"\nSUMMARY:")
        print(f"  Total items: {len(items)} ({dir_count} directories, {file_count} files)")
        print(f"  Total size: {format_size(total_size)}")

        # Display top items
        print(f"\nTOP {min(top_n, len(items))} LARGEST ITEMS:")
        print(f"{'Item':<40} {'Size':<15} {'Type':<10} {'Modified'}")
        print("-"*70)

        for item in items[:top_n]:
            item_type = "DIR" if item['is_dir'] else "FILE"
            name = item['name'][:37] + "..." if len(item['name']) > 40 else item['name']
            print(f"{name:<40} {item['formatted_size']:<15} {item_type:<10} {item['modified']}")

        # File type breakdown (for files only)
        print(f"\nFILE TYPE BREAKDOWN:")
        extensions = {}
        for item in items:
            if not item['is_dir']:
                _, ext = os.path.splitext(item['name'])
                ext = ext.lower() if ext else 'no extension'
                extensions[ext] = extensions.get(ext, 0) + item['size']

        sorted_extensions = sorted(extensions.items(), key=lambda x: x[1], reverse=True)
        for ext, size in sorted_extensions[:5]:
            print(f"  {ext:<20}: {format_size(size)}")

        print("="*70)

    except PermissionError:
        print(f"Error: Permission denied to access '{directory}'")
    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Analyze current directory
    current_dir = 'C:\\personal\\!obsidian_limudey_huts\\100625 (ramat gan)\\python_100625'
    print(f"Analyzing current directory: {current_dir}\n")
    analyze_directory(current_dir, top_n=10)

    print("\n" + "="*70)
    print("TIP: Call analyze_directory('/path/to/directory') to analyze any folder!")
    print("="*70)
