import re

filename = "registration_info.txt"
result_file = "result.txt"

def get_valid_phone():
    while True:
        phone = input("Enter your phone number (10 digits only): ")
        if phone.isdigit() and len(phone) == 10 and phone[0] in "6789":
            return phone
        print("Invalid phone number.")

def get_valid_name():
    while True:
        name = input("Enter your name (alphabets only): ")
        if name.isalpha():
            return name
        print("Invalid name. Please enter alphabets only.")

def get_valid_email():
    while True:
        email = input("Enter your email (e.g., xyz@gmail.com): ")
        if re.match(r'^[\w\.-]+@gmail\.com$', email):
            return email
        print("Invalid email format. Please enter a valid email.")

def get_valid_password():
    while True:
        password = input("Enter your password (at least 8 characters, 1 uppercase letter, 1 number, and 1 special character): ")
        if re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            return password
        print("Password must be at least 8 characters long, contain at least one uppercase letter, one number, and one special character.")

def save_registration_info(filename, phone, name, email, password):
    with open(filename, 'a') as file:
        file.write(f"Phone: {phone}\nName: {name}\nEmail: {email}\nPassword: {password}\n\n")
    print("Registration successful!")

def check_login_credentials(filename, email, password):
    with open(filename, 'r') as file:
        content = file.read()
    entries = re.findall(r"Email:\s*(\S+)\nPassword:\s*(\S+)", content)
    for stored_email, stored_password in entries:
        if email.strip().lower() == stored_email.lower() and password.strip() == stored_password:
            return True
    return False

def registration():
    print("Registration Form")
    name = get_valid_name()
    email = get_valid_email()
    password = get_valid_password()
    phone = get_valid_phone()
    save_registration_info(filename, phone, name, email, password)

def login():
    while True:
        print("Login Form")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if check_login_credentials(filename, email, password):
            print("Login successful!")
            return email
        print("Invalid email or password. Please try again.")
        exit_choice = input("Do you want to exit? (yes/no): ").strip().lower()
        if exit_choice == 'yes':
            print("Exiting the system.")
            break

def show_quiz(email):
    print("\nChoose quiz type:")
    print("1. Python")
    print("2. DBMS")
    print("3. DSA")
    quiz_choice = input("Enter your choice (1, 2, or 3): ")
    questions = {
        "python": [
            {"question": "What is the output of 2 + 2?", "options": ["4", "5", "6", "3"], "answer": "4"},
            {"question": "Which of the following is a mutable data type?", "options": ["List", "Tuple", "Set", "String"], "answer": "List"},
            {"question": "What is the correct syntax for a function in Python?", "options": ["def function_name():", "function function_name():", "function():", "def: function_name"], "answer": "def function_name():"},
            {"question": "Which of the following is a Python keyword?", "options": ["if", "yes", "none", "foreach"], "answer": "if"},
            {"question": "What is the default return value of a function in Python?", "options": ["None", "0", "1", "null"], "answer": "None"}
        ],
        "dbms": [
            {"question": "What does DBMS stand for?", "options": ["Database Management System", "Data Base Management System", "Database Managed System", "Data Base Managed System"], "answer": "Database Management System"},
            {"question": "Which is not a DBMS model?", "options": ["Network Model", "Hierarchical Model", "Relational Model", "Tree Model"], "answer": "Tree Model"},
            {"question": "What is normalization?", "options": ["Process of reducing redundancy", "Process of creating tables", "Process of defining relations", "Process of deleting records"], "answer": "Process of reducing redundancy"},
            {"question": "Which of the following is a relational database?", "options": ["MySQL", "MongoDB", "PostgreSQL", "Both MySQL and PostgreSQL"], "answer": "Both MySQL and PostgreSQL"},
            {"question": "Which SQL command is used to retrieve data from a database?", "options": ["SELECT", "INSERT", "UPDATE", "DELETE"], "answer": "SELECT"}
        ],
        "dsa": [
            {"question": "What is the time complexity of binary search?", "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"], "answer": "O(log n)"},
            {"question": "Which data structure is used to implement a breadth-first search?", "options": ["Stack", "Queue", "Tree", "Graph"], "answer": "Queue"},
            {"question": "Which sorting algorithm is the fastest in the average case?", "options": ["QuickSort", "BubbleSort", "MergeSort", "SelectionSort"], "answer": "QuickSort"},
            {"question": "What is the space complexity of merge sort?", "options": ["O(1)", "O(n)", "O(n log n)", "O(log n)"], "answer": "O(n)"},
            {"question": "Which data structure is used for recursion?", "options": ["Stack", "Queue", "Array", "Linked List"], "answer": "Stack"}
        ]
    }
    if quiz_choice == '1':
        quiz = questions["python"]
    elif quiz_choice == '2':
        quiz = questions["dbms"]
    elif quiz_choice == '3':
        quiz = questions["dsa"]
    else:
        print("Invalid choice.")
        return
    score = 0
    for idx, question in enumerate(quiz):
        print(f"\nQ{idx + 1}: {question['question']}")
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")
        answer = input("Enter the option number: ")
        if question['options'][int(answer) - 1] == question['answer']:
            score += 1
    print(f"\nYou scored {score} out of 5.")
    with open(result_file, 'a') as result_file_obj:
        result_file_obj.write(f"Email: {email}\nQuiz Type: {quiz_choice}\nScore: {score}/5\n\n")

def show_result():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if not check_login_credentials(filename, email, password):
        print("Invalid email or password.")
        return
    with open(result_file, 'r') as file:
        records = file.read()
    email_results = re.findall(rf"Email: {email}\nQuiz Type: (\d+)\nScore: (\d+)/5", records)
    if email_results:
        print(f"Results for {email}:")
        for quiz_type, score in email_results:
            quiz_name = {"1": "Python", "2": "DBMS", "3": "DSA"}.get(quiz_type, "Unknown")
            print(f"Quiz Type: {quiz_name}, Score: {score}/5")
    else:
        print("No quiz attempts found for this email.")

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Attempt Quiz (if not logged in, log in first)")
        print("4. Show Result")
        print("5. Exit")
        choice = input("Enter your choice (1, 2, 3, 4, or 5): ")
        if choice == '1':
            registration()
        elif choice == '2':
            email = login()
        elif choice == '3':
            if 'email' in locals():
                show_quiz(email)
            else:
                print("Please log in first.")
        elif choice == '4':
            show_result()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
