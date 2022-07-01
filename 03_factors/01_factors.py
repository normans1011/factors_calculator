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




# Checks input is a number more than a given value



# Gets factors, returns a sorted list



# Main routine 

# Heading
statement_generator("Factors Calculator","-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see instructions, or any key to continue")

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # ask user for number to be factored...
    var_to_factor = num_check("Number? ")

    if var_to_factor != 1:
        factors_list = get_factors(var_to_factor)

    else:
        factor_list = ""
        comment = "One is UNITY! It has only one factor. Itself."


    # comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)

    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)































































