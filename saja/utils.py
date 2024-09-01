def get_valid_input(prompt):
    """
    Prompts the user for input and ensures it is not empty.

    Parameters:
    - prompt: A string that will be displayed to the user.

    Returns:
    - The user's input if it is not empty.

    Raises:
    - ValueError: If the input is empty.
    """
    user_input = input(prompt).strip()  
    if not user_input:
        raise ValueError("Input cannot be empty. Please enter a valid input.")
    return user_input
