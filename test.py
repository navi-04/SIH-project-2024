import re 
def is_valid_email(email: str) -> bool:
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

print("enter : ")
email = input()
print(is_valid_email(email))
