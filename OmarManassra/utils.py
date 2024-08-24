from datetime import datetime
# The Date Exception Handling 
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        print ("the date is valid ")
    except ValueError:
        raise ValueError("The date is not valid,use the format YYYY-MM-DD. ")
# The input Exception Handling
def get_valid_input(prompt):
    in_val=input(prompt)
    if in_val:
        print ("the value is Valid")
    else:
        raise ValueError("the Input Value is incorrect")
# The Status Exception Handling 
def validate_status(status):
    if status=="Completed" or status=="InProgress":
        print ("Valid ")
    else:
        raise ValueError("InValid Input Status")
# The priority Exception Handling 
def validate_priority(priority):
    if priority=="High":
        print ("Valid -High")
    elif priority=="Medium":
        print ("Valid -Medium")
    elif priority=="Low":
        print ("Valid -Low")
    else:
        raise ValueError("Invalid priority")
