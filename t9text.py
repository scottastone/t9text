# This dictionary maps each character to its single T9 key.
# This is for "predictive" style input, not multi-tap.
T9_MAP = {
    'A': '2', 'B': '2', 'C': '2',
    'D': '3', 'E': '3', 'F': '3',
    'G': '4', 'H': '4', 'I': '4',
    'J': '5', 'K': '5', 'L': '5',
    'M': '6', 'N': '6', 'O': '6',
    'P': '7', 'Q': '7', 'R': '7', 'S': '7',
    'T': '8', 'U': '8', 'V': '8',
    'W': '9', 'X': '9', 'Y': '9', 'Z': '9',
    ' ': '0'
}

def text_to_t9_simple(text):
    """
    Converts a string of text into its corresponding single-press
    T9 key sequence.
    """
    output_sequence = []
    
    # Process each character in the input text, converted to uppercase
    for char in text.upper():
        if char in T9_MAP:
            sequence = T9_MAP[char]
            output_sequence.append(sequence)
        else:
            # If the character is not in our map (like punctuation),
            # we can just append it as is or ignore it.
            # Let's append it to keep punctuation.
            output_sequence.append(char)
            
    # Join all the pieces into a single string and return it
    return "".join(output_sequence)

def main():
    """
    Main function to run the T9 converter loop.
    """
    print("Enter your text below. Type '--q' to exit.")
    
    while True:
        # Get input from the user
        user_input = input("\n>>> ")
        
        # Check for quit condition
        if user_input.lower() == '--q':
            break
            
        # Convert the text and print the result
        t9_output = text_to_t9_simple(user_input)
        print(f"    {t9_output}")

# Standard check to run the main() function when the script is executed
if __name__ == "__main__":
    main()
