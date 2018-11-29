# create method to find a value in a list that is closest to the passed value
def get_closest_in_list(ref_val, comp_list, default_smaller=None, default_larger=None):
    """
    This method finds the value in the passed list that is closest to the passed value and
    returns it's index

    * ref_val: the value to be used for comparison
    * list: the list to find the closest match to value in
    * default_smaller: a value to use if no value smaller than ref_val has been found
        must be int or float!
    * default_larger: a value to use if no value larger than ref_val has been found
        must be int or float!
    """
    # This first section finds the two surrounding values in a list
    try:
        # this finds the biggest value that is smaller or equal to ref_val
        next_smaller_than_ref = max(i for i in comp_list if i <= ref_val)
    # This happens when no value smaller than the ref_val is found in the com_list
    except ValueError:
        # checks if there is a value given to use when no smaller value is found
        if default_smaller:
            next_smaller_than_ref = default_smaller
        # if there isn't, use value with lowest index
        else:
            next_smaller_than_ref = comp_list[0]
    try:
        # This finds the smallest value that is bigger or equal to ref_val
        next_larger_than_ref = min(i for i in comp_list if i >= ref_val)
    # Happens when no value that satisfies the condition is found
    except ValueError:
        # check if there is value to use if no larger value is found
        if default_larger:
            next_larger_than_ref = default_larger
        # if there isn't, use the value with the largest index
        else:
            next_larger_than_ref = comp_list[len(comp_list) - 1]

    # This second section finds which of the surrounding values is closer
    diff_to_smaller = ref_val - next_smaller_than_ref
    diff_to_larger = next_larger_than_ref - ref_val

    # if there is no smaller value than ref_val
    if diff_to_smaller < 0:
        try:
            return comp_list.index(next_smaller_than_ref)
        except ValueError:
            print("No index found for value!")
            return None
    # this means the roast is over, since there is no time value bigger than ref_val
    elif diff_to_larger < 0:
        return (-1)
    # this means there is an exact match
    elif diff_to_smaller == 0:
        try:
            return comp_list.index(next_smaller_than_ref)
        except ValueError:
            print("No index found for value!")
            return None
    elif diff_to_larger == 0:
        try:
            return comp_list.index(next_larger_than_ref)
        except ValueError:
            print("No index found for value!")
            return None
    # the value is right in between the two surrounding values, choose the bigger
    elif diff_to_smaller == diff_to_larger:
        try:
            return comp_list.index(next_larger_than_ref)
        except ValueError:
            print("No index found for value!")
            return None
    # the value is closer to the lower surrounding value
    elif diff_to_larger > diff_to_smaller:
        try:
            return comp_list.index(next_smaller_than_ref)
        except ValueError:
            print("No index found for value!")
            return None
    # the value is closer to the larger surrounding value
    elif diff_to_larger < diff_to_smaller:
        try:
            return comp_list.index(next_larger_than_ref)
        except ValueError:
            print("No index found for value!")
            return None
    # dunno, in case I forgot anything
    else:
        return None
