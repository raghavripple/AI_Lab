from decimal import Decimal, getcontext, ROUND_HALF_UP
import ast
import re
import socket

getcontext().prec = 28
TWO = Decimal("0.01")

# ---------------- BILL SYSTEM ----------------

def customer_items_bill():
    name = input("Enter customer name: ").strip()
    if not name:
        print("No customer name entered.")
        return

    items = []
    while True:
        item_name = input("Enter item name (leave blank to finish): ").strip()
        if not item_name:
            break
        try:
            price = Decimal(input(f"Enter price for '{item_name}': ").strip())
            if price < 0:
                raise ValueError
        except:
            print("Invalid price. Item skipped.")
            continue
        items.append((item_name, price))

    if not items:
        print("No items entered.")
        return

    gst_rate = Decimal("18")
    discount_rate = Decimal("30")

    subtotal = Decimal("0.00")
    total_gst = Decimal("0.00")
    total_with_gst = Decimal("0.00")

    print("\n------ Customer Bill ------")
    print(f"Customer: {name}")
    print("----------------------------")

    for item_name, price in items:
        price_q = price.quantize(TWO, rounding=ROUND_HALF_UP)
        gst = (price_q * gst_rate / Decimal("100")).quantize(TWO, rounding=ROUND_HALF_UP)
        line_total = (price_q + gst).quantize(TWO, rounding=ROUND_HALF_UP)

        subtotal += price_q
        total_gst += gst
        total_with_gst += line_total

        print(f"{item_name:20} ${price_q:8,.2f} GST ${gst:7,.2f} Total ${line_total:8,.2f}")

    discount = (total_with_gst * discount_rate / Decimal("100")).quantize(TWO, rounding=ROUND_HALF_UP)
    amount_due = (total_with_gst - discount).quantize(TWO, rounding=ROUND_HALF_UP)

    print("----------------------------")
    print(f"Subtotal: ${subtotal:,.2f}")
    print(f"Total GST: ${total_gst:,.2f}")
    print(f"Discount: -${discount:,.2f}")
    print(f"Amount Due: ${amount_due:,.2f}")
    print("----------------------------")


# ---------------- FIBONACCI ----------------

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


def run_fibonacci_prompt():
    n = int(input("How many Fibonacci numbers: "))
    print(fibonacci(n))


# ---------------- REVERSE LIST ----------------

def reverse_list_prompt():
    s = input("Enter Python list: ")
    try:
        lst = ast.literal_eval(s)
        print("Reversed:", lst[::-1])
    except:
        print("Invalid list input")


# ---------------- SENTENCE CHECK ----------------

def check_sentence_prompt():
    s = input("Enter sentence: ")
    if s and s[0].isupper() and s.endswith("."):
        print("Valid sentence ✅")
    else:
        print("Invalid sentence ❌")


# ---------------- EMAIL VALIDATION ----------------

def is_valid_email(email):
    pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}$")
    return bool(pattern.match(email))


def run_email_validation_prompt():
    e = input("Enter email: ")
    print("Valid Email ✅" if is_valid_email(e) else "Invalid Email ❌")


# ---------------- SUM OF DIGITS ----------------

def sum_digits_prompt():
    s = input("Enter number: ")
    digits = [int(c) for c in s if c.isdigit()]
    if digits:
        print("Sum of digits:", sum(digits))
    else:
        print("No digits found")


# ---------------- MAIN MENU ----------------

def main():
    while True:
        print("\n===== PYTHON MINI PROGRAMS =====")
        print("1. Customer Bill System")
        print("2. Fibonacci Series")
        print("3. Reverse List")
        print("4. Sentence Validator")
        print("5. Email Validator")
        print("6. Sum of Digits")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            customer_items_bill()
        elif choice == "2":
            run_fibonacci_prompt()
        elif choice == "3":
            reverse_list_prompt()
        elif choice == "4":
            check_sentence_prompt()
        elif choice == "5":
            run_email_validation_prompt()
        elif choice == "6":
            sum_digits_prompt()
        elif choice == "0":
            print("Bye 👋")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
