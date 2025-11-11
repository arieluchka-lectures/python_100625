import pyfiglet
from datetime import datetime
import platform

def create_welcome_banner(app_name, version, tagline=""):
    """
    Creates a professional welcome banner for CLI applications.

    Args:
        app_name (str): Name of the application
        version (str): Version number
        tagline (str): Optional tagline or description
    """
    # Terminal width
    terminal_width = 80

    # Create the main title with ASCII art
    title = pyfiglet.figlet_format(app_name, font='slant')

    # Print top border
    print("=" * terminal_width)
    print(title)

    # Print version and tagline
    print(f"{'Version: ' + version:^{terminal_width}}")
    if tagline:
        print(f"{tagline:^{terminal_width}}")

    # Print system information
    print("-" * terminal_width)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    system_info = f"Python {platform.python_version()} | {platform.system()}"
    print(f"Started: {current_time}")
    print(f"System: {system_info}")
    print("=" * terminal_width)

def create_section_header(section_name):
    """
    Creates a section header for different parts of the application.

    Args:
        section_name (str): Name of the section
    """
    header = pyfiglet.figlet_format(section_name, font='small')
    print(header)

# Example Usage
if __name__ == "__main__":
    # Main application banner
    create_welcome_banner(
        app_name="DataApp",
        version="v2.1.0",
        tagline="Your Data Analysis Companion"
    )

    print("\nInitializing application...")
    print("Loading modules...")
    print("\n")

    # Section headers throughout the app
    create_section_header("Settings")
    print("- Database: Connected")
    print("- Cache: Enabled")
    print("- Debug Mode: Off")
    print("\n")

    create_section_header("Dashboard")
    print("Welcome to your dashboard!")
    print("- Total Users: 1,234")
    print("- Active Sessions: 56")
    print("\n")

    # Exit message
    print("=" * 80)
    exit_message = pyfiglet.figlet_format("Thank You!", font='digital')
    print(exit_message)
    print("=" * 80)

