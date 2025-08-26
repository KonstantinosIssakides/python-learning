from datetime import datetime

name = input("What is your name? ")
age_text = (input("How old are you? "))
try:
    age = int(age_text)
except ValueError:
    print("Please enter a valid number for your age.")
    raise SystemExit   

current_year = datetime.now().year
year_of_birth = current_year - age

while True:
    output_mode = input("Choose output: [1] simple year [2] fun message: ").strip().lower()
    if output_mode in ['1', 'simple year']:
        print(f"You were born in {year_of_birth}.")
    elif output_mode in ['2', 'fun message']:
        print(f"Wow {name}, you were born in {year_of_birth}! That's amazing!")
        break
    else:
        print("Please choose 1 (simple) or 2 (fun message).")