
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








































