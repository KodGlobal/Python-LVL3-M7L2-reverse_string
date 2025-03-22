# Function to reverse a string
def reverse_string(s):
    # Task: Complete the function here
    '''
    Create an empty string to store the result
    Iterate through each character in the input string
    Add the current character to the beginning of the result string
    This way, the last character becomes the first, the second-to-last becomes the second, and so on
    Return the reversed string
    '''
    return


# Main function of the program
def main():
    # Prompt the user to enter a string to reverse
    user_input = input("Enter a string to reverse: ")
    # Call the reverse_string function, passing the user's input string
    # Print the reversed string
    print("Reversed string:", reverse_string(user_input))


# Check if the program is run directly and not imported as a module
if __name__ == "__main__":
    main()  # Call the main function if the program is run directly