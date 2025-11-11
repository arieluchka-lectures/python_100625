from datetime import datetime, date


def calculate_age(birth_date):
    """Calculate age in years, months, and days"""
    today = date.today()

    # Calculate years
    years = today.year - birth_date.year

    # Adjust if birthday hasn't occurred this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        years -= 1

    # Calculate months
    months = today.month - birth_date.month
    if today.day < birth_date.day:
        months -= 1
    if months < 0:
        months += 12

    # Calculate days
    if today.day >= birth_date.day:
        days = today.day - birth_date.day
    else:
        # Get days in previous month
        prev_month = today.month - 1 if today.month > 1 else 12
        prev_year = today.year if today.month > 1 else today.year - 1

        # Days in previous month
        if prev_month in [1, 3, 5, 7, 8, 10, 12]:
            days_in_prev = 31
        elif prev_month in [4, 6, 9, 11]:
            days_in_prev = 30
        else:  # February
            days_in_prev = 29 if prev_year % 4 == 0 and (prev_year % 100 != 0 or prev_year % 400 == 0) else 28

        days = days_in_prev - birth_date.day + today.day

    return years, months, days


def days_until_birthday(birth_date):
    """Calculate days until next birthday"""
    today = date.today()

    # Get this year's birthday
    this_year_birthday = date(today.year, birth_date.month, birth_date.day)

    # If birthday already passed, get next year's
    if this_year_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
    else:
        next_birthday = this_year_birthday

    days_left = (next_birthday - today).days
    return days_left, next_birthday


def main():
    print("=" * 50)
    print("AGE CALCULATOR")
    print("=" * 50)

    print()

    # Example person 1
    print("Example 1: Person born on January 15, 1990")
    print("-" * 50)
    birth_date1 = date(1990, 1, 15)
    years, months, days = calculate_age(birth_date1)
    days_left, next_bday = days_until_birthday(birth_date1)

    print(f"Birth Date: {birth_date1.strftime('%B %d, %Y')}")
    print(f"Age: {years} years, {months} months, and {days} days")
    print(f"Next Birthday: {next_bday.strftime('%B %d, %Y')}")
    print(f"Days until birthday: {days_left} days")
    print()

    # Example person 2
    print("Example 2: Person born on December 25, 2000")
    print("-" * 50)
    birth_date2 = date(2000, 12, 25)
    years, months, days = calculate_age(birth_date2)
    days_left, next_bday = days_until_birthday(birth_date2)

    print(f"Birth Date: {birth_date2.strftime('%B %d, %Y')}")
    print(f"Age: {years} years, {months} months, and {days} days")
    print(f"Next Birthday: {next_bday.strftime('%B %d, %Y')}")
    print(f"Days until birthday: {days_left} days")
    print()

    # Example person 3 - today's birthday!
    print("Example 3: Person born on November 11, 1995")
    print("-" * 50)
    birth_date3 = date(1995, 11, 11)
    years, months, days = calculate_age(birth_date3)
    days_left, next_bday = days_until_birthday(birth_date3)

    print(f"Birth Date: {birth_date3.strftime('%B %d, %Y')}")
    print(f"Age: {years} years, {months} months, and {days} days")

    if days_left == 0:
        print("🎉 HAPPY BIRTHDAY! 🎉")
    else:
        print(f"Next Birthday: {next_bday.strftime('%B %d, %Y')}")
        print(f"Days until birthday: {days_left} days")

if __name__ == "__main__":
    main()