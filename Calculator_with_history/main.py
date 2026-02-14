HISTORY_FILE = "history.txt"

def show_history():
    with open(HISTORY_FILE, "r") as file:
        lines = file.readlines()
        if len(lines) == 0:
            print("History is empty")
        else:
            for line in reversed(lines):
                print(line.strip())

def clear_history():
    with open(HISTORY_FILE, "w") as file:
        file.write("")
    print("History cleared")

def save_to_history(equation, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{equation} = {result}\n")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Use formate: number operator number (e.g 2 + 3)")
        return
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator, Use only +, -, *, /")
        return
    
    if int(result) == result:
        result = int(result)

    print(f"Result: {result}")
    save_to_history(user_input, result)

def main():
    print("---Simple Calculator (type history, clear or exit)---")
    while True:
        user_input = input("Enter Calculation (+ = * /) or command (history, clear or exit): ")

        match user_input:
            case "history":
                show_history()
            case "clear":
                clear_history()
            case "exit":
                print("Goodbye")
                break
            case _:
                calculate(user_input)

main()
