# SUPER CONSOLE CALCULATOR WITH 50 FUNCTIONS AND MENU

import time  # delays and timers
import math  # math functions
import random  # random numbers and games
import string  # password generator characters
from datetime import datetime  # date/time functions
import calendar  # calendar display
from fractions import Fraction  # decimal to fraction conversion

# === FUNCTION DEFINITIONS ===

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Cannot divide by zero"
def modulo(a, b): return a % b if b != 0 else "Cannot modulo by zero"
def gcd(a, b): return a if b == 0 else gcd(b, a % b)
def lcm(a, b): return abs(a * b) // gcd(a, b)
def percentage(a, b): return (a / b * 100) if b != 0 else "Cannot divide by zero"
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True
def divisible_by(start, end, d):
    return [i for i in range(start, end + 1) if d != 0 and i % d == 0]
def factorial(n): return math.factorial(n) if n >= 0 else "Undefined for negative"
def nth_root(a, r): return a ** (1 / r) if r != 0 else "Root degree cannot be zero"
def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
def pi(): return math.pi
def square_cube_table(n):
    return [(i, i**2, i**3) for i in range(1, n + 1)]
def multiplication_table(num):
    return [f"{num} x {i} = {num * i}" for i in range(1, 11)]
def average(nums): return sum(nums) / len(nums) if nums else 0
def digit_sum_product(n):
    digits = [int(i) for i in str(abs(n))]
    prod = 1
    for d in digits: prod *= d
    return sum(digits), prod
def is_armstrong(n):
    power = len(str(n))
    return n == sum(int(d) ** power for d in str(n))
def is_palindrome(n): return str(n) == str(n)[::-1]
def decimal_to_binary(n): return bin(n)[2:]
def binary_to_decimal(b): return int(b, 2)
def decimal_to_hex(n): return hex(n)[2:]
def decimal_to_octal(n): return oct(n)[2:]
def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total, prev = 0, 0
    for ch in reversed(s):
        val = roman.get(ch, 0)
        total += val if val >= prev else -val
        prev = val
    return total
def int_to_roman(n):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ""
    for i in range(len(val)):
        while n >= val[i]:
            roman += syms[i]
            n -= val[i]
    return roman
def rock_paper_scissors(user):
    options = ["rock", "paper", "scissors"]
    comp = random.choice(options)
    if user == comp: return "Tie"
    elif (user == "rock" and comp == "scissors") or (user == "paper" and comp == "rock") or (user == "scissors" and comp == "paper"):
        return f"You win! (Computer chose {comp})"
    elif user in options: return f"You lose! (Computer chose {comp})"
    else: return "Invalid input"
def guessing_game(secret, guess):
    if guess < secret: return "Too low"
    elif guess > secret: return "Too high"
    else: return "Correct!"
def dice_roll(sides): return random.randint(1, sides)
def coin_flip(): return random.choice(["Heads", "Tails"])
def magic_8_ball():
    responses = ["Yes", "No", "Maybe", "Ask again", "Definitely"]
    return random.choice(responses)
def word_scramble(word):
    w = list(word)
    random.shuffle(w)
    return ''.join(w)
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def typing_test(start, end, text):
    duration = end - start
    wpm = (len(text.split()) / duration) * 60
    return f"Typing speed: {wpm:.2f} WPM"
def age_calculator(birth_str):
    birth = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.today()
    years = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    return years
def stopwatch():
    input("Press ENTER to start...")
    start = time.time()
    input("Press ENTER to stop...")
    end = time.time()
    return f"Elapsed: {end - start:.2f} sec"
def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)
    return "Time's up!"
def alarm_clock(target_time):
    print(f"Alarm set for {target_time}... Waiting...")
    while datetime.now().strftime("%H:%M") != target_time:
        time.sleep(30)
    return "⏰ Wake up!"
def c_to_f(c): return (c * 9 / 5) + 32
def f_to_c(f): return (f - 32) * 5 / 9
def c_to_k(c): return c + 273.15
def password_generator(length=12, special=True):
    chars = string.ascii_letters + string.digits
    if special: chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))
def number_to_words(n):
    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    def convert(x):
        if x < 10: return units[x]
        elif x < 20: return teens[x - 10]
        elif x < 100: return tens[x // 10] + ("-" + units[x % 10] if x % 10 else "")
        elif x < 1000: return units[x // 100] + " hundred" + (" and " + convert(x % 100) if x % 100 else "")
        else: return units[x // 1000] + " thousand" + (" " + convert(x % 1000) if x % 1000 else "")
    return convert(n)
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
def decimal_to_fraction(d):
    return Fraction(d).limit_denominator()
def triangle_area(base, height):
    return 0.5 * base * height
def solve_quadratic(a, b, c):
    disc = b ** 2 - 4 * a * c
    if disc < 0:
        return "No real roots"
    elif disc == 0:
        root = -b / (2 * a)
        return f"One root: {root}"
    else:
        r1 = (-b + math.sqrt(disc)) / (2 * a)
        r2 = (-b - math.sqrt(disc)) / (2 * a)
        return f"Two roots: {r1} and {r2}"
def meters_to_feet(m):
    return m * 3.28084
def bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    if height_m <= 0:
        return "Invalid height"
    bmi_value = weight_kg / (height_m ** 2)
    if bmi_value < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi_value < 25:
        category = "Normal weight"
    elif 25 <= bmi_value < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return round(bmi_value, 2), category
def show_calendar_month(year, month):
    return calendar.month(year, month)

def save_result(result):
    with open("calculator_history.txt", "a") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{now}] {result}\n")

def load_results():
    try:
        with open("calculator_history.txt", "r") as f:
            content = f.read().strip()
            if content:
                print("\n--- Saved Calculation Results ---")
                print(content)
                print("---------------------------------\n")
            else:
                print("No saved results found.")
    except FileNotFoundError:
        print("No saved results file found.")

# === MENU SYSTEM ===

def calculator_menu():
    menu_items = [
        "1: Add", "2: Subtract", "3: Multiply", "4: Divide", "5: Modulo",
        "6: GCD", "7: LCM", "8: Percentage", "9: Prime Check", "10: Divisible By",
        "11: Factorial", "12: nth Root", "13: Fibonacci Sequence", "14: Pi Constant", "15: Square & Cube Table",
        "16: Multiplication Table", "17: Average Calculator", "18: Digit Sum & Product", "19: Armstrong Number Check", "20: Palindrome Check",
        "21: Decimal to Binary", "22: Binary to Decimal", "23: Decimal to Hexadecimal", "24: Decimal to Octal", "25: Roman to Integer",
        "26: Integer to Roman", "27: Rock Paper Scissors Game", "28: Number Guessing Game", "29: Dice Roll", "30: Coin Flip",
        "31: Magic 8 Ball", "32: Word Scramble", "33: Leap Year Check", "34: Typing Speed Test", "35: Age Calculator",
        "36: Stopwatch", "37: Countdown Timer", "38: Alarm Clock", "39: Celsius to Fahrenheit", "40: Fahrenheit to Celsius",
        "41: Celsius to Kelvin", "42: Password Generator", "43: Number to Words", "44: Prime Factorization", "45: Decimal to Fraction",
        "46: Triangle Area", "47: Quadratic Equation Solver", "48: Meters to Feet", "49: BMI Calculator", "50: Show Calendar Month",
        "51: Load Saved Results", "0: Exit"
    ]

    while True:
        print("\n=== SUPER CONSOLE CALCULATOR MENU ===")
        # Print menu in 5 rows of 10 items max per row (for neatness)
        for i in range(0, len(menu_items), 10):
            print(" | ".join(menu_items[i:i+10]))

        choice = input("\nSelect a function (0 to exit): ").strip()
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        choice = int(choice)

        if choice == 0:
            print("Goodbye!")
            break

        try:
            if choice == 1:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                res = add(a,b)
                print("Result:", res)
                save_result(f"Add: {a} + {b} = {res}")

            elif choice == 2:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                res = subtract(a,b)
                print("Result:", res)
                save_result(f"Subtract: {a} - {b} = {res}")

            elif choice == 3:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                res = multiply(a,b)
                print("Result:", res)
                save_result(f"Multiply: {a} * {b} = {res}")

            elif choice == 4:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                res = divide(a,b)
                print("Result:", res)
                save_result(f"Divide: {a} / {b} = {res}")

            elif choice == 5:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                res = modulo(a,b)
                print("Result:", res)
                save_result(f"Modulo: {a} % {b} = {res}")

            elif choice == 6:
                a = int(input("Enter integer A: "))
                b = int(input("Enter integer B: "))
                res = gcd(a,b)
                print("GCD:", res)
                save_result(f"GCD: gcd({a}, {b}) = {res}")

            elif choice == 7:
                a = int(input("Enter integer A: "))
                b = int(input("Enter integer B: "))
                res = lcm(a,b)
                print("LCM:", res)
                save_result(f"LCM: lcm({a}, {b}) = {res}")

            elif choice == 8:
                a = float(input("Enter value A: "))
                b = float(input("Enter value B: "))
                res = percentage(a,b)
                if isinstance(res,float):
                    print(f"{a} is {res:.2f}% of {b}")
                    save_result(f"Percentage: {a} is {res:.2f}% of {b}")
                else:
                    print(res)
                    save_result(f"Percentage error with values: {a}, {b}")

            elif choice == 9:
                n = int(input("Enter integer: "))
                res = "Prime" if is_prime(n) else "Not prime"
                print(res)
                save_result(f"Prime check: {n} is {res}")

            elif choice == 10:
                start = int(input("Start of range: "))
                end = int(input("End of range: "))
                d = int(input("Divisor: "))
                res = divisible_by(start,end,d)
                print("Numbers divisible by", d, ":", res)
                save_result(f"Divisible by {d} in range {start}-{end}: {res}")

            elif choice == 11:
                n = int(input("Enter non-negative integer: "))
                res = factorial(n)
                print("Factorial:", res)
                save_result(f"Factorial: {n}! = {res}")

            elif choice == 12:
                a = float(input("Enter number: "))
                r = float(input("Enter root degree: "))
                res = nth_root(a,r)
                print(f"{r}th root of {a} is {res}")
                save_result(f"nth Root: {r}th root of {a} = {res}")

            elif choice == 13:
                n = int(input("How many Fibonacci numbers?: "))
                res = fibonacci(n)
                print("Fibonacci sequence:", res)
                save_result(f"Fibonacci sequence length {n}: {res}")

            elif choice == 14:
                res = pi()
                print("Pi constant:", res)
                save_result(f"Pi constant: {res}")

            elif choice == 15:
                n = int(input("Enter number of rows: "))
                res = square_cube_table(n)
                for tup in res:
                    print(f"{tup[0]} | square: {tup[1]} | cube: {tup[2]}")
                save_result(f"Square & Cube Table for {n} rows")

            elif choice == 16:
                num = int(input("Enter number for multiplication table: "))
                res = multiplication_table(num)
                for line in res:
                    print(line)
                save_result(f"Multiplication table for {num}")

            elif choice == 17:
                raw = input("Enter numbers separated by space: ")
                nums = list(map(float, raw.split()))
                res = average(nums)
                print(f"Average: {res}")
                save_result(f"Average of {nums} = {res}")

            elif choice == 18:
                n = int(input("Enter integer: "))
                s, p = digit_sum_product(n)
                print(f"Sum of digits: {s}, Product of digits: {p}")
                save_result(f"Digit sum/product of {n}: sum={s}, product={p}")

            elif choice == 19:
                n = int(input("Enter integer: "))
                res = "Is Armstrong" if is_armstrong(n) else "Not Armstrong"
                print(res)
                save_result(f"Armstrong check {n}: {res}")

            elif choice == 20:
                n = input("Enter number or string: ")
                res = "Is palindrome" if is_palindrome(n) else "Not palindrome"
                print(res)
                save_result(f"Palindrome check {n}: {res}")

            elif choice == 21:
                n = int(input("Enter integer: "))
                res = decimal_to_binary(n)
                print(f"Binary: {res}")
                save_result(f"Decimal to binary {n}: {res}")

            elif choice == 22:
                b = input("Enter binary string: ")
                try:
                    res = binary_to_decimal(b)
                    print(f"Decimal: {res}")
                    save_result(f"Binary to decimal {b}: {res}")
                except:
                    print("Invalid binary number.")

            elif choice == 23:
                n = int(input("Enter integer: "))
                res = decimal_to_hex(n)
                print(f"Hexadecimal: {res}")
                save_result(f"Decimal to hex {n}: {res}")

            elif choice == 24:
                n = int(input("Enter integer: "))
                res = decimal_to_octal(n)
                print(f"Octal: {res}")
                save_result(f"Decimal to octal {n}: {res}")

            elif choice == 25:
                s = input("Enter Roman numeral (uppercase): ")
                res = roman_to_int(s)
                print(f"Integer: {res}")
                save_result(f"Roman to integer {s}: {res}")

            elif choice == 26:
                n = int(input("Enter integer: "))
                res = int_to_roman(n)
                print(f"Roman numeral: {res}")
                save_result(f"Integer to Roman {n}: {res}")

            elif choice == 27:
                user = input("Enter rock, paper or scissors: ").lower()
                res = rock_paper_scissors(user)
                print(res)
                save_result(f"Rock Paper Scissors: User {user}, Result: {res}")

            elif choice == 28:
                secret = random.randint(1, 100)
                print("Guess the number between 1 and 100.")
                while True:
                    guess = int(input("Your guess: "))
                    res = guessing_game(secret, guess)
                    print(res)
                    if res == "Correct!":
                        save_result(f"Number guessing game won with guess {guess}")
                        break

            elif choice == 29:
                sides = int(input("Enter number of sides on dice: "))
                res = dice_roll(sides)
                print(f"Dice roll result: {res}")
                save_result(f"Dice roll with {sides} sides: {res}")

            elif choice == 30:
                res = coin_flip()
                print(f"Coin flip result: {res}")
                save_result(f"Coin flip: {res}")

            elif choice == 31:
                res = magic_8_ball()
                print(f"Magic 8 Ball says: {res}")
                save_result(f"Magic 8 Ball: {res}")

            elif choice == 32:
                word = input("Enter word to scramble: ")
                res = word_scramble(word)
                print(f"Scrambled word: {res}")
                save_result(f"Word scramble {word} -> {res}")

            elif choice == 33:
                year = int(input("Enter year: "))
                res = "Leap year" if is_leap_year(year) else "Not a leap year"
                print(res)
                save_result(f"Leap year check {year}: {res}")

            elif choice == 34:
                print("Typing test: Type the sentence and press Enter.")
                sentence = "The quick brown fox jumps over the lazy dog"
                print(f"Type this: {sentence}")
                input("Press Enter when ready...")
                start = time.time()
                typed = input()
                end = time.time()
                res = typing_test(start, end, typed)
                print(res)
                save_result(f"Typing test result: {res}")

            elif choice == 35:
                birth_str = input("Enter birthdate (YYYY-MM-DD): ")
                try:
                    res = age_calculator(birth_str)
                    print(f"Age: {res}")
                    save_result(f"Age calculation for {birth_str}: {res}")
                except:
                    print("Invalid date format.")

            elif choice == 36:
                res = stopwatch()
                print(res)
                save_result(f"Stopwatch: {res}")

            elif choice == 37:
                seconds = int(input("Enter countdown seconds: "))
                res = countdown_timer(seconds)
                print(res)
                save_result(f"Countdown timer {seconds} seconds ended")

            elif choice == 38:
                target_time = input("Set alarm time (HH:MM 24h): ")
                print(alarm_clock(target_time))
                save_result(f"Alarm clock set for {target_time}")

            elif choice == 39:
                c = float(input("Enter Celsius temperature: "))
                res = c_to_f(c)
                print(f"{c}°C = {res:.2f}°F")
                save_result(f"Celsius to Fahrenheit {c}°C = {res:.2f}°F")

            elif choice == 40:
                f = float(input("Enter Fahrenheit temperature: "))
                res = f_to_c(f)
                print(f"{f}°F = {res:.2f}°C")
                save_result(f"Fahrenheit to Celsius {f}°F = {res:.2f}°C")

            elif choice == 41:
                c = float(input("Enter Celsius temperature: "))
                res = c_to_k(c)
                print(f"{c}°C = {res:.2f}K")
                save_result(f"Celsius to Kelvin {c}°C = {res:.2f}K")

            elif choice == 42:
                length = int(input("Enter password length: "))
                special = input("Include special characters? (y/n): ").lower() == 'y'
                res = password_generator(length, special)
                print("Generated password:", res)
                save_result(f"Password generated: {res}")

            elif choice == 43:
                n = int(input("Enter number (0-9999): "))
                res = number_to_words(n)
                print("In words:", res)
                save_result(f"Number to words {n}: {res}")

            elif choice == 44:
                n = int(input("Enter integer: "))
                res = prime_factors(n)
                print("Prime factors:", res)
                save_result(f"Prime factors of {n}: {res}")

            elif choice == 45:
                d = float(input("Enter decimal number: "))
                res = decimal_to_fraction(d)
                print(f"Fraction: {res}")
                save_result(f"Decimal to fraction {d}: {res}")

            elif choice == 46:
                base = float(input("Enter base length: "))
                height = float(input("Enter height: "))
                res = triangle_area(base, height)
                print(f"Triangle area: {res}")
                save_result(f"Triangle area base={base} height={height}: {res}")

            elif choice == 47:
                a = float(input("Enter a: "))
                b = float(input("Enter b: "))
                c = float(input("Enter c: "))
                res = solve_quadratic(a, b, c)
                print(res)
                save_result(f"Quadratic equation {a}x² + {b}x + {c}: {res}")

            elif choice == 48:
                m = float(input("Enter meters: "))
                res = meters_to_feet(m)
                print(f"{m} meters = {res:.2f} feet")
                save_result(f"Meters to feet {m}m = {res:.2f}ft")

            elif choice == 49:
                weight = float(input("Enter weight (kg): "))
                height_cm = float(input("Enter height (cm): "))
                res = bmi(weight, height_cm)
                if isinstance(res, tuple):
                    print(f"BMI: {res[0]}, Category: {res[1]}")
                    save_result(f"BMI for {weight}kg, {height_cm}cm: {res[0]}, {res[1]}")
                else:
                    print(res)
                    save_result(f"BMI calculation error for {weight}kg, {height_cm}cm")

            elif choice == 50:
                y = int(input("Year (e.g. 2023): "))
                m = int(input("Month (1-12): "))
                try:
                    cal = show_calendar_month(y, m)
                    print(cal)
                    save_result(f"Calendar for {m}/{y}")
                except:
                    print("Invalid year/month")
            
            elif choice == 51:
                load_results()

            else:
                print("Invalid choice. Try again.")

        except Exception as e:
            print("Error:", e)
            print("Try again.")

if __name__ == "__main__":
    calculator_menu()

