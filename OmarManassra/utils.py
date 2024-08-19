# The Date Exception Handling 
def validate_date(date_str):
    if date_str=="20-8-2024":
        print ("the Date is right")
    else:
        raise ValueError("the value Date is not right ")
# The input Exception Handling
def get_valid_input(prompt):
    In_val=input(prompt)
    if In_val:
        print ("the value is Valid")
    else:
        raise ValueError("the Input Value is incorrect")
# The Status Exception Handling 
def validate_status(status):
    if status=="Complate" or status=="InProgress":
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
