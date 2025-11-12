from datetime import datetime, date, time, timedelta


# ===== Creating and Getting Current Date/Time =====
print("1. CURRENT DATE AND TIME")
print("-" * 40)

# Get current datetime
now = datetime.now()
print(f"Current datetime: {now}")

# Get current date only
today = date.today()
print(f"Current date: {today}")

# Create specific datetime
specific_date = datetime(2025, 12, 25, 15, 30, 0)
print(f"Specific datetime: {specific_date}")

print("\n")

# ===== Formatting Dates =====
print("2. FORMATTING DATES")
print("-" * 40)

# Common formats
print(f"Format 1: {now.strftime('%Y-%m-%d')}")  # 2025-11-11
print(f"Format 2: {now.strftime('%B %d, %Y')}")  # November 11, 2025
print(f"Format 3: {now.strftime('%d/%m/%Y %H:%M:%S')}")  # 11/11/2025 15:23:00
print(f"Format 4: {now.strftime('%A, %b %d')}")  # Tuesday, Nov 11

print("\n")

# ===== Date Arithmetic =====
print("3. DATE ARITHMETIC")
print("-" * 40)

# Add/subtract days
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print(f"Tomorrow: {tomorrow}")
print(f"Yesterday: {yesterday}")

# Add weeks, hours, minutes
next_week = now + timedelta(weeks=1)
in_3_hours = now + timedelta(hours=3)
print(f"Next week: {next_week}")
print(f"In 3 hours: {in_3_hours}")

# Calculate difference between dates
new_year = datetime(2026, 1, 1)
days_until = (new_year - now).days
print(f"Days until New Year 2026: {days_until}")

print("\n")

# ===== Extracting Components =====
print("4. EXTRACTING DATE/TIME COMPONENTS")
print("-" * 40)

print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")
print(f"Weekday: {now.strftime('%A')}")

print("\n")

# ===== Parsing Strings to Dates ==