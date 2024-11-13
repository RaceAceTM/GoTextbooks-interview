def calculate_check_digit(baseDigits, is13=True): #figures out what the check digit is to use later
    if is13:
        # This runs if its an isbn13, and multiplies each digit by alternating to 1 or 3, then adds them up
        weights = [1, 3] * 6  # alernates between 1 and 3, do it * 6 so it goes a total of 12 times
        wSum = sum(int(digit) * weight for digit, weight in zip(baseDigits, weights))
        return str((10 - wSum % 10) % 10)  # returns the check digit for a 13
    else:
        # This runs if its a isbn10, since otherwise the code won't get here. 
        # For isbn10 you multiply each number by subtracting weights by 1 from 10 to 2, then add them up 
        wSum = sum(int(digit) * (10 - index) for index, digit in enumerate(baseDigits))
        remainder = wSum % 11
        # Return 'X' if remainder is 1, otherwise return the difference from 11
        return 'X' if remainder == 1 else str((11 - remainder) % 11)


def convert(input):
    # detects if its a isbn10 or isbn13 then turns it into the opposite one. If its not a recognized format then return an error. 

    # check if its a isbn10 format
    if len(input) == 10 and input[:9].isdigit() and (input[-1].isdigit() or input[-1].upper() == 'X'):
        # convert isbn10 to isbn 13 by adding "978" to the front of the sequence and finding out the check digit
        isbn13_base_digits = "978" + input[:9]  #add 978 to the front of the first 9 digits (exclude the old check digit)
        new_check_digit = calculate_check_digit(isbn13_base_digits)  # get a new check digit
        return f"converted isbn10 to isbn13: {isbn13_base_digits}{new_check_digit}"  # return the isbn13 (complete :) )
    
    # check if its a isbn13 format
    elif len(input) == 13 and input.isdigit() and input.startswith("978"):
        # start by removing the 978 from the front, and find the new check digit soon after. 
        isbn10_base_digits = input[3:12]  # grab the 9 digits after the 978 (exclude the old check digit)
        new_check_digit = calculate_check_digit(isbn10_base_digits, is13=False)  # find a new check digit, also let the system know its not a isbn13
        return f"converted isbn13 to isbn10: {isbn10_base_digits}{new_check_digit}"  # return the isbn10 (complete :) )

    # if the input doesn't match either one, then return an error since its not a isbn10 or isbn13
    else:
        return "Not a good isbn format. Try again and enter a isbn13 or isbn10."


# ask for the input, run the conversion, and then print the results. 
user_input = input("Enter an ISBN-10 or ISBN-13: ")
print(convert(user_input))
#Time complexity should be O(1) which is what I assume to be the goal
#Space complexity is also O(1) which seems about right


#i added a lot of comments to this just to explain my thinking process. Im sure there are better ways to optimize this than I did, and probably better ways to
#preform the task that I am doing, but for the sake of what this specific program called for, I think this does it pretty well. 
#sorry if you have to read all of my comments, some of them are descriptive, some of them are just reminders for me 
