# create method to find a value in a list that is closest to the passed value
def get_closest_in_list(ref_val, comp_list):
    """Find the value in given list that is closest to given target, return it's index."""
    target_value = find_closest_value(ref_val, comp_list)
    target_index = comp_list.index(target_value)
    return target_index


def find_closest_value(target, ordered_list):
    """Find first value in given list that is smaller than given target."""
    if len(ordered_list) > 2:
        middle = len(ordered_list) // 2

        if target < ordered_list[middle]:
            low_half = ordered_list[: middle + 1]
            high_half = ordered_list[middle:]
            return find_closest_value(target, low_half)
        elif target > ordered_list[middle]:
            low_half = ordered_list[:middle]
            high_half = ordered_list[middle:]
            return find_closest_value(target, high_half)
        else:  # target == ordered_list[middle]
            return ordered_list[middle]
    else:
        if abs(target - ordered_list[0]) < abs(target - ordered_list[1]):
            return ordered_list[0]
        else:
            return ordered_list[1]
