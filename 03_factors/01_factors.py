# Functions go here

# Puts series of symbols at start and end of text
def statement_generator(text, decoration):

    # make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    

    return ""

# Displays instructions / information
def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Enter the number you would like to find the factors of. The number can be from 1-200")

    return ""

# checks input is a number more than a given value
def num_check (question, low):

    valid = False
    while not valid:

        error = "Please enter a number that is more than or equal to {}".format(low)
        
        try:
            

            # ask user to enter a number
            response = int(input(question))
            
            
            # checks number is more than zero
            if 1<= response >=200:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()
        
        except ValueError:
            print(error)

# Gets factors, returns a sorted list
def get_factors(to_factor):
    # List to hold factors
    factors_list = []

    # Square root to_factor to find 'half way'
    limit = int(to_factor ** 0.5)

    # find factor pairs and add to list
    for item in range (1, limit + 1):

        # check factor is not 1 (unity)
        if to_factor == 1:
            break

        # check if number is a factor
        result = to_factor % item 
        factor_1 = int(to_factor // item)

        # add factor to list if its not already in there
        if result == 0:
            factors_list.append(item)

        if factor_1 != item and result == 0:
            factors_list.append(factor_1)

    # Sort list
    factors_list.sort()

    return(factors_list)



# Main routine 

# Heading
statement_generator("Factors Calculator","-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see instructions, or any key to continue: ")


if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":


    comment = ""

    # ask user for number to be factored...

    var_to_factor = num_check("Number?:  ", 1)
    

    if var_to_factor != 1:
        factors_list = get_factors(var_to_factor)

    else:
        factors_list = ""
        comment = "One is UNITY! It has only one factor. Itself."


    # comments for squares / primes
    if len(factors_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)

    elif len(factors_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)

    # Output factors and comment

    # Generate heading...

    if var_to_factor == 1:
        heading = "One is special..."

    else:
        heading="factors of {}".format(var_to_factor)

    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factors_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit")

    

print()
print("Thankyou for using the factors calculator")































































