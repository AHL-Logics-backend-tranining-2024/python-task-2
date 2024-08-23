from utils import validate_status, validate_date, validate_priority, get_valid_input

def read_credentials(file_path='credentials.txt'):
    credentials = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                key, value = line.strip().split(': ')
                credentials[key] = value
    except FileNotFoundError:
        print(f"Error:{file_path} not found")
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        exit()

    return credentials



def authenticate(credentials):
    username = get_valid_input("Enter username: ")
    password = get_valid_input("Enter password: ")

    if username == credentials.get('username') and password == credentials.get('password'):
        print("Authentication successful , Hi !")
        return True
    else:
        print("Authentication failed ,  Please try again.")
        return False

