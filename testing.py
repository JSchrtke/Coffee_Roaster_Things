"""
prototype for profile comparison method
"""
# reference_time_list = []
# live_time_list = [0, 0.1, 0.5, 2, 3, 3.6, 4, 5, 5.4, 303]

# for i in range(0, 600, 5):
#     reference_time_list.append(i)

# for time_value in live_time_list:
#     print("time_value: " + str(time_value))
#     bigger_than_current_time = 0
#     smaller_than_current_time = max(i for i in reference_time_list if i <= time_value)
#     bigger_than_current_time = min(i for i in reference_time_list if i >= time_value)
#     print("smaller_current_time :" + str(smaller_than_current_time))
#     print("bigger_current_time: " + str(bigger_than_current_time))
#     difference_to_smaller_value = time_value - smaller_than_current_time
#     difference_to_bigger_value = bigger_than_current_time - time_value
#     print("diff_to_smaller: " + str(difference_to_smaller_value))
#     print("diff_to_bigger: " + str(difference_to_bigger_value))
#     result = -1
#     if difference_to_bigger_value == 0 and difference_to_smaller_value == 0:
#         result = time_value
#     elif difference_to_bigger_value == difference_to_smaller_value:
#         result = bigger_than_current_time
#     elif difference_to_bigger_value < difference_to_smaller_value:
#         result = bigger_than_current_time
#     elif difference_to_smaller_value < difference_to_bigger_value:
#         result = smaller_than_current_time
#     else:
#         result = "error"
#     print("result: " + str(result))
