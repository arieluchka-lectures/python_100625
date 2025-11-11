import pyfiglet
import time

class MenuSystem:
    """An interactive menu system with ASCII art styling."""

    def __init__(self, app_title):
        """Initialize the menu system with an application title."""
        self.app_title = app_title
        self.running = True

    def clear_screen(self):
        """Simulate clearing screen with newlines."""
        print("\n" * 2)

    def display_title(self):
        """Display the main application title."""
        title = pyfiglet.figlet_format(self.app_title, font='banner3')
        print("=" * 70)
        print(title)
        print("=" * 70)

    def display_menu(self, options):
        """
        Display menu options.

        Args:
            options (list): List of menu options
        """
        print("\nMAIN MENU")
        print("-" * 70)
        for i, option in enumerate(options, 1):
            print(f"  [{i}] {option}")
        print(f"  [0] Exit")
        print("-" * 70)

    def display_success(self, message):
        """Display a success message with ASCII art."""
        print("\n")
        success = pyfiglet.figlet_format("SUCCESS", font='small')
        print(success)
        print(f"✓ {message}")
        time.sleep(1)

    def display_error(self, message):
        """Display an error message with ASCII art."""
        print("\n")
        error = pyfiglet.figlet_format("ERROR", font='small')
        print(error)
        print(f"✗ {message}")
        time.sleep(1)

    def process_file(self):
        """Simulate file processing."""
        print("\nProcessing file...")
        processing = pyfiglet.figlet_format("Processing", font='digital')
        print(processing)

        # Simulate work
        for i in range(3):
            print(f"Step {i+1}/3 completed...")
            time.sleep(0.5)

        self.display_success("File processed successfully!")

    def display_stats(self):
        """Display statistics with ASCII art."""
        print("\n")
        stats_header = pyfiglet.figlet_format("STATS", font='slant')
        print(stats_header)
        print("-" * 70)
        print(f"{'Total Operations:':<30} {'1,234':>10}")
        print(f"{'Success Rate:':<30} {'98.5%':>10}")
        print(f"{'Average Time:':<30} {'2.3s':>10}")
        print(f"{'Last Updated:':<30} {'2025-11-11':>10}")
        print("-" * 70)
        input("\nPress Enter to continue...")

    def show_settings(self):
        """Display settings menu."""
        print("\n")
        settings_header = pyfiglet.figlet_format("Settings", font='small')
        print(settings_header)
        print("-" * 70)
        print("Current Settings:")
        print("  • Auto-save: Enabled")
        print("  • Theme: Dark")
        print("  • Language: English")
        print("  • Notifications: On")
        print("-" * 70)
        input("\nPress Enter to continue...")

    def run(self):
        """Run the main menu loop."""
        menu_options = [
            "Process New File",
            "View Statistics",
            "Settings",
            "About"
        ]

        while self.running:
            self.clear_screen()
            self.display_title()
            self.display_menu(menu_options)

            try:
                choice = input("\nEnter your choice: ").strip()

                if choice == "1":
                    self.process_file()
                elif choice == "2":
                    self.display_stats()
                elif choice == "3":
                    self.show_settings()
                elif choice == "4":
                    print("\n")
                    about = pyfiglet.figlet_format("FileApp", font='slant')
                    print(about)
                    print("Version 1.0.0 - A simple file processing application")
                    print("Created with Python and Pyfiglet")
                    input("\nPress Enter to continue...")
                elif choice == "0":
                    self.running = False
                    print("\n")
                    goodbye = pyfiglet.figlet_format("Goodbye!", font='bubble')
                    print(goodbye)
                    print("Thank you for using our application!\n")
                else:
                    self.display_error("Invalid choice. Please try again.")

            except KeyboardInterrupt:
                self.running = False
                print("\n\nExiting application...\n")
            except Exception as e:
                self.display_error(f"An error occurred: {str(e)}")

# Example Usage
if __name__ == "__main__":
    # Create and run the menu system
    menu = MenuSystem("FileApp")

    # Display welcome screen
    welcome = pyfiglet.figlet_format("WELCOME", font='banner')
    print(welcome)
    print("Loading application...")
    time.sleep(1)

    # Run the interactive menu
    menu.run()
