def register_user(name):
    capitalized_name = name.capitalize()
    print(f"User registered as: {capitalized_name}")

register_user("john doe")  # Output: "User registered as: John doe"

def process_text(text):
    if text.isspace():
        print("Input contains only spaces.")
    else:
        print("Valid input received.")

process_text("   ")  # Output: "Input contains only spaces."
process_text("Hello")  # Output: "Valid input received."

def check_password_strength(password):
    if password.islower():
        print("Password is too weak. Include uppercase letters.")
    else:
        print("Password strength is good.")

check_password_strength("password")  # Output: "Password is too weak. Include uppercase letters."
check_password_strength("Password123")  # Output: "Password strength is good."

def format_heading(heading):
    if not heading.isupper():
        print("Heading should be in uppercase.")
    else:
        print("Heading format is correct.")

format_heading("SECTION HEADING")  # Output: "Heading format is correct."
format_heading("Section Heading")  # Output: "Heading should be in uppercase."

def format_book_title(title):
    formatted_title = title.title()
    print(f"Formatted Title: {formatted_title}")

format_book_title("harry potter and the goblet of fire")  # Output: "Formatted Title: Harry Potter And The Goblet Of Fire"

def clean_input(user_input):
    cleaned_input = user_input.strip()
    print(f"Cleaned Input: '{cleaned_input}'")

clean_input("   Hello World   ")  # Output: "Cleaned Input: 'Hello World'"

def validate_username(username):
    if username.isalnum():
        print("Username is valid.")
    else:
        print("Username should only contain letters and numbers.")

validate_username("User123")  # Output: "Username is valid."
validate_username("User_123")  # Output: "Username should only contain letters and numbers."

def validate_amount(amount):
    if amount.isdigit():
        print("Amount is valid.")
    else:
        print("Amount should be a numeric value.")

validate_amount("100")  # Output: "Amount is valid."
validate_amount("10a0")  # Output: "Amount should be a numeric value."

def validate_name(name):
    if name.isalpha():
        print("Name is valid.")
    else:
        print("Name should only contain letters.")

validate_name("JohnDoe")  # Output: "Name is valid."
validate_name("John Doe")  # Output: "Name should only contain letters."

def search_item(database, query):
    normalized_query = query.lower()
    results = [item for item in database if normalized_query in item.lower()]
    print(f"Search results: {results}")

database = ["Apple", "banana", "Cherry"]
search_item(database, "APPLE")  # Output: "Search results: ['Apple']"

