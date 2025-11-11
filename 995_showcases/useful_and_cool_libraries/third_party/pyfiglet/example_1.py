import pyfiglet

# 1. BASIC USAGE - Default font
print("=" * 60)
print("1. BASIC USAGE - Default Font")
print("=" * 60)
text = "Hello World"
result = pyfiglet.figlet_format(text)
print(result)

# 2. USING DIFFERENT FONTS
print("=" * 60)
print("2. DIFFERENT FONTS")
print("=" * 60)

# Slant font
print("\nSlant Font:")
result_slant = pyfiglet.figlet_format("Python", font="slant")
print(result_slant)

# Digital font
print("Digital Font:")
result_digital = pyfiglet.figlet_format("2025", font="digital")
print(result_digital)

# Bubble font
print("Bubble Font:")
result_bubble = pyfiglet.figlet_format("Bubble", font="bubble")
print(result_bubble)

# 3. USING FIGLET CLASS
print("=" * 60)
print("3. USING FIGLET CLASS")
print("=" * 60)
from pyfiglet import Figlet

f = Figlet(font='banner3')
print(f.renderText('Figlet Class'))

# 4. LISTING AVAILABLE FONTS
print("=" * 60)
print("4. AVAILABLE FONTS")
print("=" * 60)
fonts = pyfiglet.FigletFont.getFonts()
print(f"Total fonts available: {len(fonts)}")
print(f"\nFirst 20 fonts: {fonts[:20]}")

# 5. CUSTOM WIDTH
print("=" * 60)
print("5. CUSTOM WIDTH")
print("=" * 60)
f_custom = Figlet(font='standard', width=100)
print(f_custom.renderText('Custom Width'))

# 6. JUSTIFICATION
print("=" * 60)
print("6. JUSTIFICATION OPTIONS")
print("=" * 60)

# Left justified (default)
f_left = Figlet(font='small', justify='left')
print("Left Justified:")
print(f_left.renderText('Left'))

# Center justified
f_center = Figlet(font='small', justify='center', width=80)
print("\nCenter Justified:")
print(f_center.renderText('Center'))

# Right justified
f_right = Figlet(font='small', justify='right', width=80)
print("\nRight Justified:")
print(f_right.renderText('Right'))

print("\n" + "=" * 60)
print("Pyfiglet Basics Complete!")
print("=" * 60)