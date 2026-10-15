
#! Task 1
#* 1. Compare Two Numbers
#* • Read two integers from the user.
#* • Use if / elif / else to display which number is greater, or display "Numbers are equal"
def compare_numbers():
    
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    if num1 > num2:
        print(f"{num1} is greater than {num2}.")
    elif num1 < num2:
        print(f"{num2} is greater than {num1}.")
    else:
        print("Numbers are equal.")

#! Task 2
#* 2. Positive, Negative or Zero
#* • Read one number from the user.
#* • Use if / elif / else to display whether it is positive, negative, or equal to zero.

def check_number():
    num = float(input("Enter a number: "))

    if num > 0:
        print(f"{num} is positive.")
    elif num < 0:
        print(f"{num} is negative.")
    else:
        print("The number is zero.")

#! Task 3
#* 3. Odd or Even
#* • Read one integer from the user.
#* • Use the % operator to determine whether the number is even or odd.

def check_odd_even():
    num = int(input("Enter an integer: "))

    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

#! Task 4 
#* • Read an integer score from the user.
#* • 91-100 = A; 81-90 = B; 71-80 = C; 61-70 = D; 51-60 = E; 0-50 = F.
#* • If the score is below 0 or above 100, display "Invalid score".
#* • Use if / elif / else. Do not use the and operator.

def grade_score():
    score = int(input("Enter the score (0-100): "))

    if score < 0 or score > 100:
        print("Invalid score.")
    elif score >= 91:
        print("Grade: A")
    elif score >= 81:
        print("Grade: B")
    elif score >= 71:
        print("Grade: C")
    elif score >= 61:
        print("Grade: D")
    elif score >= 51:
        print("Grade: E")
    else:
        print("Grade: F")

#! Task 5
#* • Read three different numbers from the user.
#* • Find and display the largest using only if / elif / else and comparison operators.
#* • Do not use max().

def find_largest():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

    print(f"The largest number is: {largest}")

#! Task 6
#* • Read two numbers and an operation symbol.
#* • Supported operations: +, -, *, /, %, **, //.
#* • Use match / case to select the operation. Use case _ for "Invalid operation".
#* • For /, %, and //, reject a zero second number. Also reject 0 raised to a negative power and a negative base raised to a
#* non-integer power.
#* • Otherwise, perform the operation and display the result.

def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /, %, **, //): ")

    if operation == '+':
        result = num1 + num2
        print(f"Result: {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"Result: {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"Result: {result}")
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Result: {result}")
    elif operation == '%':
        if num2 == 0:
            print("Error: Modulus by zero is not allowed.")
        else:
            result = num1 % num2
            print(f"Result: {result}")
    elif operation == '**':
        if num1 == 0 and num2 < 0:
            print("Error: 0 cannot be raised to a negative power.")
        elif num1 < 0 and not num2.is_integer():
            print("Error: Negative base cannot be raised to a non-integer power.")
        else:
            result = num1 ** num2
            print(f"Result: {result}")
    elif operation == '//':
        if num2 == 0:
            print("Error: Floor division by zero is not allowed.")
        else:
            result = num1 // num2
            print(f"Result: {result}")
    else:
        print("Invalid operation.")

#! Task 7
#* • Read the user's age as an integer.
#* • 0-12 = Child; 13-17 = Teenager; 18-64 = Adult; 65 and above = Senior.
#* • Use if / elif / else. If age is negative, display "Invalid age".

def categorize_age():
    age = int(input("Enter your age: "))

    if age < 0:
        print("Invalid age.")
    elif age <= 12:
        print("You are a Child.")
    elif age <= 17:
        print("You are a Teenager.")
    elif age <= 64:
        print("You are an Adult.")
    else:
        print("You are a Senior.")

#! Task 8
#* • Read the purchase amount in AZN. Reject negative amounts.
#* • Below 100 = no discount; 100 to below 300 = 10%; 300 to below 500 = 15%; 500 or more = 20%.
#* • Use if / elif / else. Display the original price, discount amount, and final price.

def calculate_discount():
    amount = float(input("Enter the purchase amount in AZN: "))

    if amount < 0:
        print("Invalid amount. Please enter a non-negative value.")
        return

    if amount < 100:
        discount = 0
    elif amount < 300:
        discount = 0.10 * amount
    elif amount < 500:
        discount = 0.15 * amount
    else:
        discount = 0.20 * amount

    final_price = amount - discount

    print(f"Original Price: {amount:.2f} AZN")
    print(f"Discount Amount: {discount:.2f} AZN")
    print(f"Final Price: {final_price:.2f} AZN")

#! Task 9
#* • Read three different integers and display them from smallest to largest.
#* • Use conditional statements. Do not use lists, sort(), sorted(), min(), or max().

def sort_three_numbers():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    num3 = int(input("Enter the third integer: "))

    if num1 <= num2 and num1 <= num3:
        smallest = num1
        if num2 <= num3:
            middle = num2
            largest = num3
        else:
            middle = num3
            largest = num2
    elif num2 <= num1 and num2 <= num3:
        smallest = num2
        if num1 <= num3:
            middle = num1
            largest = num3
        else:
            middle = num3
            largest = num1
    else:
        smallest = num3
        if num1 <= num2:
            middle = num1
            largest = num2
        else:
            middle = num2
            largest = num1

    print(f"Numbers in ascending order: {smallest}, {middle}, {largest}")

#! Task 10
#* • Assume the account balance is 1000 AZN. Read the withdrawal amount.
#* • Zero or negative amount: "Invalid amount". Amount above the balance: "Insufficient balance".
#* • Otherwise, subtract the amount and display the remaining balance.

def withdraw_amount():
    balance = 1000.0
    amount = float(input("Enter the withdrawal amount in AZN: "))

    if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"Withdrawal successful. Remaining balance: {balance:.2f} AZN")

#! Task 11
#* • Read monthly electricity usage in kWh. Negative usage is invalid.
#* • 0-100 kWh: 0.08 AZN/kWh; above 100 up to 300: 0.12 AZN/kWh; above 300: 0.15 AZN/kWh.
#* • Apply the selected rate to the full usage amount, not separately to each band.
#* • Display usage, applied rate, and total bill. These are fictional exercise rates.

def calculate_electricity_bill():
    usage = float(input("Enter monthly electricity usage in kWh: "))

    if usage < 0:
        print("Invalid usage. Please enter a non-negative value.")
        return

    if usage <= 100:
        rate = 0.08
    elif usage <= 300:
        rate = 0.12
    else:
        rate = 0.15

    total_bill = usage * rate

    print(f"Electricity Usage: {usage:.2f} kWh")
    print(f"Applied Rate: {rate:.2f} AZN/kWh")
    print(f"Total Bill: {total_bill:.2f} AZN")

#! Task 12
#* • Read travel distance in km. Reject negative distances.
#* • Starting fee: 2 AZN. 0-5 km: 0.70 AZN/km; above 5 up to 15 km: 0.60 AZN/km; above 15 km: 0.50 AZN/km.
#* • Apply the selected distance rate to the full distance, then add the starting fee.
#* • Display the starting fee, distance fee, and total fare.

def calculate_taxi_fare():
    distance = float(input("Enter travel distance in km: "))

    if distance < 0:
        print("Invalid distance. Please enter a non-negative value.")
        return

    starting_fee = 2.0

    if distance <= 5:
        rate = 0.70
    elif distance <= 15:
        rate = 0.60
    else:
        rate = 0.50

    distance_fee = distance * rate
    total_fare = starting_fee + distance_fee

    print(f"Starting Fee: {starting_fee:.2f} AZN")
    print(f"Distance Fee: {distance_fee:.2f} AZN")
    print(f"Total Fare: {total_fare:.2f} AZN")

#! Task 13
#* • Read integer age, monthly salary, and requested loan amount.
#* • Reject negative age or salary and a loan amount of zero or less as invalid input.
#* • Otherwise, reject in this order: age below 18; salary below 500 AZN; requested loan above 10 times the salary.
#* • Approve only if all checks pass. Display the decision and the first applicable reason.
#* • Do not use and. Use nested if statements. These are fictional exercise rules.

def loan_approval():
    age = int(input("Enter your age: "))
    salary = float(input("Enter your monthly salary in AZN: "))
    loan_amount = float(input("Enter the requested loan amount in AZN: "))

    if age < 0 or salary < 0 or loan_amount <= 0:
        print("Invalid input. Age and salary must be non-negative, and loan amount must be greater than zero.")
    else:
        if age < 18:
            print("Loan rejected: Age below 18.")
        else:
            if salary < 500:
                print("Loan rejected: Salary below 500 AZN.")
            else:
                if loan_amount > 10 * salary:
                    print("Loan rejected: Requested loan exceeds 10 times the salary.")
                else:
                    print("Loan approved.")

#! Task 14
#* • Read three side lengths: a, b, and c. All lengths must be positive.
#* • Check a + b > c, a + c > b, and b + c > a using nested if statements without and.
#* • All sides equal = Equilateral; exactly two equal = Isosceles; all different = Scalene.
#* • If any required check fails, display "Triangle cannot be created".

def triangle_type():
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Invalid input. All side lengths must be positive.")
    else:
        if a + b > c:
            if a + c > b:
                if b + c > a:
                    if a == b and b == c:
                        print("The triangle is Equilateral.")
                    elif a == b or a == c or b == c:
                        print("The triangle is Isosceles.")
                    else:
                        print("The triangle is Scalene.")
                else:
                    print("Triangle cannot be created.")
            else:
                print("Triangle cannot be created.")
        else:
            print("Triangle cannot be created.")

#! Task 15
#* • Read integer exam score, school score, and age. Reject negative age and scores outside 0-700 and 0-100
#* respectively.
#* • For valid input, reject an applicant younger than 16.
#* • Exam score 600-700 = Scholarship; 450-599 = Accepted.
#* • Exam score 300-449 = Accepted only if school score is at least 80; otherwise Rejected. Below 300 = Rejected.
#* • Use if / elif / else. Display the result and the reason.

def admission_decision():
    exam_score = int(input("Enter the exam score (0-700): "))
    school_score = int(input("Enter the school score (0-100): "))
    age = int(input("Enter your age: "))

    if age < 0 or exam_score < 0 or exam_score > 700 or school_score < 0 or school_score > 100:
        print("Invalid input. Age must be non-negative, exam score must be between 0-700, and school score must be between 0-100.")
    else:
        if age < 16:
            print("Rejected: Applicant is younger than 16.")
        else:
            if exam_score >= 600:
                print("Scholarship awarded.")
            elif exam_score >= 450:
                print("Accepted.")
            elif exam_score >= 300:
                if school_score >= 80:
                    print("Accepted based on school score.")
                else:
                    print("Rejected: School score below 80.")
            else:
                print("Rejected: Exam score below 300.")

#! Task 16
#* • Read an integer exam score. Reject values outside 0-100 using if / else.
#* • For a valid score, use one ternary expression to assign "Pass" for 51 or above, or "Fail" otherwise.
#* • Display the assigned result. Do not use if / elif / else to choose Pass or Fail.

def pass_fail():
    score = int(input("Enter the exam score (0-100): "))

    if score < 0 or score > 100:
        print("Invalid score. Please enter a value between 0 and 100.")
    else:
        result = "Pass" if score >= 51 else "Fail"
        print(f"Result: {result}")

#! Task 17
#* • Read a non-negative order total in AZN and a membership answer: exactly "yes" or "no".
#* • Reject a negative total or any other membership answer.
#* • Delivery is free when the total is at least 50 AZN or membership is "yes"; otherwise it costs 5 AZN.
#* • Use a ternary expression to assign the delivery fee. Display the fee and final total.

def calculate_delivery_fee():
    total = float(input("Enter the order total in AZN: "))
    membership = input("Are you a member? (yes/no): ").strip().lower()

    if total < 0 or membership not in ["yes", "no"]:
        print("Invalid input. Please enter a non-negative total and 'yes' or 'no' for membership.")
        return

    delivery_fee = 0 if total >= 50 or membership == "yes" else 5
    final_total = total + delivery_fee

    print(f"Delivery Fee: {delivery_fee:.2f} AZN")
    print(f"Final Total: {final_total:.2f} AZN")

#! Task 18
#* • Read an integer day number: 1 = Monday through 7 = Sunday.
#* • Use match / case to display the day name.
#* • Also display "Study day" for 1-5 or "Weekend" for 6-7.
#* • Use case _ to display "Invalid day" for other numbers.

def day_of_week():
    day_number = int(input("Enter the day number (1-7): "))

    match day_number:
        case 1:
            print("Monday - Study day")
        case 2:
            print("Tuesday - Study day")
        case 3:
            print("Wednesday - Study day")
        case 4:
            print("Thursday - Study day")
        case 5:
            print("Friday - Study day")
        case 6:
            print("Saturday - Weekend")
        case 7:
            print("Sunday - Weekend")
        case _:
            print("Invalid day.")

#! Task 19
#* • Read a drink code and an integer quantity: T = Tea (2 AZN), C = Coffee (4 AZN), J = Juice (3 AZN).
#* • Only the uppercase codes shown above are accepted. Quantity must be from 1 to 10.
#* • Use match / case to select the drink and price. Reject an unknown code or invalid quantity.
#* • Display the drink, quantity, and total. Use a ternary expression to assign "Large order" if total is at least 20 AZN, or
#* "Regular order" otherwise.

def drink_order():
    drink_code = input("Enter the drink code (T/C/J): ").strip().upper()
    quantity = int(input("Enter the quantity (1-10): "))

    if quantity < 1 or quantity > 10:
        print("Invalid quantity. Please enter a value between 1 and 10.")
        return

    match drink_code:
        case 'T':
            price_per_unit = 2
            drink_name = "Tea"
        case 'C':
            price_per_unit = 4
            drink_name = "Coffee"
        case 'J':
            price_per_unit = 3
            drink_name = "Juice"
        case _:
            print("Invalid drink code. Please enter T, C, or J.")
            return

    total = price_per_unit * quantity
    order_type = "Large order" if total >= 20 else "Regular order"

    print(f"Drink: {drink_name}")
    print(f"Quantity: {quantity}")
    print(f"Total: {total} AZN")
    print(f"Order Type: {order_type}")

#TODO Input validation for Tasks 20-25: Read input as text first. Use len(), .isascii(), .isdecimal(), and slicing where needed. An
#TODO ASCII-digit string must pass both .isascii() and .isdecimal(). Convert only after validation. Do not remove spaces to make
#TODO invalid input valid.

#! Task 20
#* • Read a student ID as a string. It must contain exactly 8 ASCII digits (0-9).
#* • Letters, spaces, signs, decimal points, and other characters are not allowed. Empty input is invalid.
#* • Check these rules before any numeric conversion. Leading zeros are allowed and must be preserved.
#* • Use if / elif / else to display "Student ID accepted" or a clear reason for rejection.
#* • Examples: "00123456" is valid; "12A45678", "1234567", and "1234 678" are invalid.

def validate_student_id():
    student_id = input("Enter the student ID (8 digits): ")

    if len(student_id) != 8:
        print("Invalid ID: Must be exactly 8 characters long.")
    elif not student_id.isascii():
        print("Invalid ID: Must contain only ASCII characters.")
    elif not student_id.isdecimal():
        print("Invalid ID: Must contain only digits (0-9).")
    else:
        print("Student ID accepted.")

#! Task 21
#* • Use a fictional stored PIN of "0427". Read one PIN attempt as a string.
#* • The input must contain exactly 4 ASCII digits. Do not allow letters, spaces, signs, or decimal points.
#* • Check for empty input first, then wrong length, then forbidden characters, then compare with the stored PIN.
#* • Display the first applicable message: "PIN is required", "PIN must have 4 digits", "Digits only", "Access granted",
#* or "Incorrect PIN".
#* • Use if / elif / else. Allow one attempt only; preserve leading zeros.

def validate_pin():
    stored_pin = "0427"
    pin_attempt = input("Enter your PIN (4 digits): ")

    if not pin_attempt:
        print("PIN is required.")
    elif len(pin_attempt) != 4:
        print("PIN must have 4 digits.")
    elif not pin_attempt.isascii() or not pin_attempt.isdecimal():
        print("Digits only.")
    elif pin_attempt == stored_pin:
        print("Access granted.")
    else:
        print("Incorrect PIN.")

#! Task 22
#* • Read a phone number as a string in the local format 0XXXXXXXXX: exactly 10 ASCII digits, beginning with 0.
#* • Spaces, letters, +, hyphens, and brackets are not allowed. Empty input is invalid.
#* • For this exercise, accepted three-digit prefixes are 050, 051, 055, 070, 077, and 099 only.
#* • Validate length and characters with if / elif / else before checking the prefix. Use match / case on the first three
#* characters to accept or reject it.
#* • Display "Phone number accepted" or the first applicable error. Example: "0501234567" is valid; "+994501234567"
#* is invalid for this format.

def validate_phone_number():
    phone_number = input("Enter the phone number (0XXXXXXXXX): ")

    if len(phone_number) != 10:
        print("Invalid number: Must be exactly 10 characters long.")
    elif not phone_number.isascii() or not phone_number.isdecimal():
        print("Invalid number: Must contain only ASCII digits.")
    elif not phone_number.startswith('0'):
        print("Invalid number: Must start with 0.")
    else:
        prefix = phone_number[:3]
        match prefix:
            case '050' | '051' | '055' | '070' | '077' | '099':
                print("Phone number accepted.")
            case _:
                print("Invalid number: Unrecognized prefix.")

#! Task 23
#* • Assume balance = 1000 AZN and stored PIN = "0427". Read the PIN and withdrawal amount as strings.
#* • Validate in order: PIN format (exactly 4 ASCII digits), PIN match, amount format, amount range, banknote rule,
#* available balance. Display only the first error.
#* • The amount must be non-empty and contain ASCII digits only. Letters, spaces, signs, and decimal points are
#* forbidden; validate before int().
#* • The amount must be between 10 and 500 AZN inclusive and divisible by 10.
#* • Use a ternary expression to set the fee: 0 AZN for withdrawals up to 200 AZN, otherwise 2 AZN.
#* • Use if / elif / else to check that amount + fee does not exceed the balance. Deduct nothing if any check fails.
#* • On success, display the withdrawal amount, fee, and new balance. Process only one transaction.

def atm_withdrawal():
    balance = 1000
    stored_pin = "0427"

    pin_attempt = input("Enter your PIN (4 digits): ")
    if len(pin_attempt) != 4 or not pin_attempt.isascii() or not pin_attempt.isdecimal():
        print("Invalid PIN format: Must be exactly 4 ASCII digits.")
        return
    elif pin_attempt != stored_pin:
        print("Incorrect PIN.")
        return

    amount_str = input("Enter withdrawal amount (10-500 AZN, divisible by 10): ")
    if not amount_str or not amount_str.isascii() or not amount_str.isdecimal():
        print("Invalid amount format: Must contain only ASCII digits.")
        return

    amount = int(amount_str)
    if amount < 10 or amount > 500:
        print("Invalid amount: Must be between 10 and 500 AZN.")
        return
    elif amount % 10 != 0:
        print("Invalid amount: Must be divisible by 10.")
        return

    fee = 0 if amount <= 200 else 2
    total_deduction = amount + fee

    if total_deduction > balance:
        print("Insufficient balance for this transaction.")
        return

    new_balance = balance - total_deduction
    print(f"Withdrawal successful. Amount: {amount} AZN, Fee: {fee} AZN, New Balance: {new_balance} AZN")

#! Task 24
#* • Read product code, quantity, coupon code, and delivery code as strings.
#* • Use match / case for products: K = Keyboard (40 AZN), M = Mouse (20 AZN), H = Headphones (60 AZN). Only
#* these uppercase codes are valid.
#* • Quantity must contain ASCII digits only and represent a value from 1 to 5. Reject empty input, letters, spaces, signs,
#* and decimal points before conversion.
#* • Coupon must be exactly NONE or SAVE10. SAVE10 gives a 10% discount only when the subtotal is at least 100
#* AZN; otherwise reject it as ineligible.
#* • Use match / case for delivery: P = Pickup (free), S = Standard. Any other code is invalid.
#* • For Standard delivery, use a ternary expression: free when the discounted subtotal is at least 80 AZN, otherwise 5
#* AZN.
#* • Validate in this order: product, quantity format, quantity range, coupon code, coupon eligibility, delivery code. Print
#* the first error and no receipt if invalid.
#* • On success, display product, quantity, subtotal, discount, delivery fee, and final total.

def process_order():
    product_code = input("Enter product code (K/M/H): ").strip().upper()
    quantity_str = input("Enter quantity (1-5): ").strip()
    coupon_code = input("Enter coupon code (NONE/SAVE10): ").strip().upper()
    delivery_code = input("Enter delivery code (P/S): ").strip().upper()

    match product_code:
        case 'K':
            product_name = "Keyboard"
            unit_price = 40
        case 'M':
            product_name = "Mouse"
            unit_price = 20
        case 'H':
            product_name = "Headphones"
            unit_price = 60
        case _:
            print("Invalid product code. Please enter K, M, or H.")
            return

    if not quantity_str or not quantity_str.isascii() or not quantity_str.isdecimal():
        print("Invalid quantity format: Must contain only ASCII digits.")
        return

    quantity = int(quantity_str)
    if quantity < 1 or quantity > 5:
        print("Invalid quantity: Must be between 1 and 5.")
        return

    subtotal = unit_price * quantity

    if coupon_code not in ["NONE", "SAVE10"]:
        print("Invalid coupon code. Please enter NONE or SAVE10.")
        return

    discount = 0
    if coupon_code == "SAVE10":
        if subtotal >= 100:
            discount = 0.10 * subtotal
        else:
            print("Coupon SAVE10 is ineligible for this order.")
            return

    discounted_subtotal = subtotal - discount

    match delivery_code:
        case 'P':
            delivery_fee = 0
        case 'S':
            delivery_fee = 0 if discounted_subtotal >= 80 else 5
        case _:
            print("Invalid delivery code. Please enter P or S.")
            return

    final_total = discounted_subtotal + delivery_fee

    print(f"Product: {product_name}")
    print(f"Quantity: {quantity}")
    print(f"Subtotal: {subtotal:.2f} AZN")
    print(f"Discount: {discount:.2f} AZN")
    print(f"Delivery Fee: {delivery_fee:.2f} AZN")
    print(f"Final Total: {final_total:.2f} AZN")

#! Task 25
#* • Read student ID, age, workshop code, and payment amount as strings. Use the validation order shown below and
#* report only the first error.
#* • Student ID: exactly 8 ASCII digits. Leading zeros are allowed. Empty input, letters, spaces, signs, and decimal
#* points are forbidden.
#* • Age: non-empty ASCII digits only, then convert to int(). The allowed age range is 16-65 inclusive.
#* • Use match / case for workshop codes: PY = Python Basics (30 AZN, minimum age 16); WEB = Web Development
#* (40 AZN, minimum age 16); CY = Cybersecurity (50 AZN, minimum age 18). Reject other codes.
#* • After checking the workshop code, reject an applicant who does not meet its minimum age.
#* • Use a ternary expression to give a 20% discount to applicants aged 16-18 inclusive; otherwise give no discount.
#* • Payment must be a non-empty string of ASCII digits representing whole AZN. Letters, spaces, signs, and decimal
#* points are not allowed. Validate before conversion.
#* • If payment is below the discounted fee, display "Insufficient payment" and the missing amount. Otherwise, display
#* "Registration confirmed", student ID, workshop, discount, final fee, and change.
#* • Do not print a confirmation or calculate change when any earlier validation fails.
