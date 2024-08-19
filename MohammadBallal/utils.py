#Function for validate the format of date
def validate_date(datestr):
    from datetime import datetime
    try: 
        #Validates if the date matches dd/mm/yyyy format by strptime() method 
        datetime.strptime(datestr, '%d/%m/%Y')
    except ValueError: 
        raise ValueError("Date form must be dd/mm/yyyy")

#Function to get valid details input by user    
def get_valid_input(prompt):
    userInput= input(prompt)
    if not userInput:
        raise ValueError("It's empty!")
    return userInput

#Function for validate status if its in the valid status list or not
def validate_status(status):
    validStatus= ['InProgress','Completed']
    if status not in validStatus:
        raise ValueError(f"Ststus should be one of : {validate_status}")

#Function for validate priority if its in the valid priority list or not
def valid_priority(priority):
    validPriority= ['High', 'Medium', 'Low']
    if priority not in validPriority:
        raise ValueError(f"Priority should be one of : {valid_priority}")
