# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt
import os
import zipfile

#Extraing the zip file
if not os.path.exists("chicago.csv"):
    zfile = zipfile.ZipFile("chicago.csv.zip")
    zfile.extractall()
    print("chicago.csv extracted.")

if not os.path.exists("chicago.csv"):
    print("Please, extract the chicago.csv.zip file and try again.")

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# Done: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")
for i in range(20):
    print(data_list[i])

# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")
# TASK 2
# Done: Print the `gender` of the first 20 rows
print("\nTASK 2: Printing the genders of the first 20 samples")
for i, line in enumerate(data_list[:20], start=1):
    print("Line : {}\tGender: {}".format(i,line[-2]))

# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# Done: Create a function to add the columns(features) of a list in another list in the same order
def column_to_list(data, index):
    """
    This function convert an column from a list to another list.
    Args:
      data: The list with some colums.
      index: The index of collums that will be converted.
    Returns:
      List of values with index collumn
    """
    column_list = []
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    for colun in data:
        column_list.append(colun[index])
    return column_list

def get_gender_count(gender_list, gender: str):
    """
    This function return the count of gender.
    Args:
        gender_list: The gender list.
    Returns:
        gender_count: with sum of gender in the list.
    """
    gender_count: int = 0

    for i in gender_list:
        if i == gender:
            gender_count += 1

    return gender_count

# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

def get_gender_list(data):
    """
    This function get the gender list that is defined by -2 index.
    Args:
      data: The list with some columns.
    Returns:
      Gender list
    """
    return column_to_list(data_list, -2)

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
gender_list = get_gender_list(data_list)
# TASK 4
# Done: Count each gender. You should not use a function to do that.
male    = get_gender_count(gender_list, "Male")
female  = get_gender_count(gender_list, "Female")

# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# Done: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):
    """
    This function count the gender Male and Female.
    Args:
        data_list: The list with some columns.
    Returns:
        List with two index, Male and Female.
    """
    gender_list = get_gender_list(data_list)
    male   = get_gender_count(gender_list, "Male")
    female = get_gender_count(gender_list, "Female")
    return [male, female]

print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# Done: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list):
    """
    This function check the most popular gender.
    Args:
        data_list: The list with some columns data.
    Returns:
        answer: string with the most popular gender
    """
    male, female = count_gender(data_list)

    if(male > female):
        answer = "Male"
    elif(female > male):
        answer = "Female"
    else:
        answer = "Equal"
    return answer

print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# Should return a list with [subscriber, customer] (e.g., [10, 15] means 10 Subscriber, 15 Customer)
def get_user_type_count(user_types_list, user_type: str):
    """
    This function return the count of user types.
    Args:
        user_types_list: The user types list.
        user_type: user type.
    Returns:
        user_type_count: Sum of user type in the list.
    """
    user_type_count: int = 0

    for i in user_types_list:
        if i == user_type:
            user_type_count += 1

    return user_type_count

def count_user_types(user_types_list):
    """
    This function count how many user types there are.
    Args:
        user_types_list: The list with some columns data.
    Returns:
        List: with two index, Subscriber and Customer.
    """
    subscriber  = get_user_type_count(user_types_list, "Subscriber")
    customer    = get_user_type_count(user_types_list, "Customer")
    return [subscriber, customer]

# Done: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")
user_types_list = column_to_list(data_list, -3)
# Subscriber or Customer
types = ["Subscriber", "Customer"]
user_types_quantity = count_user_types(user_types_list)
print("\n result of user types count:")
print(user_types_quantity)
y_pos = list(range(len(types)))
plt.bar(y_pos, user_types_quantity)
plt.ylabel('Quantity')
plt.xlabel('User Types')
plt.xticks(y_pos, types)
plt.title('Quantity by User Types')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 8
# Done: Answer the following question
male, female = count_gender(data_list)
undefined_genders = len(data_list) - (male + female)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Because there are " + str(undefined_genders) + " registers that are not defined the gender."
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

def get_median(list):
    """
    This function return the median number of list.
    Args:
        list: The list with some columns data.
    Returns:
        median: media number of list.
    """
    if len(list) % 2 == 0:
        # even
        median = int(list[(len(list) // 2) - 1]) + int(list[len(list) // 2])
        median = median / 2
    else:
        #odd
        median = int(list[len(list) // 2])
    return median

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# Done: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = column_to_list(data_list, 2)
trip_duration_list = list(map(float,trip_duration_list))
trip_duration_list_ordened = sorted(trip_duration_list)

min_trip = int(trip_duration_list_ordened[0])
max_trip = int(trip_duration_list_ordened[-1])
mean_trip = round(sum(trip_duration_list_ordened) / len(trip_duration_list_ordened))
median_trip = get_median(trip_duration_list_ordened)

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# Done: Check types how many start_stations do we have using set()
start_stations_list = column_to_list(data_list, 3)
start_stations = set(start_stations_list)

print("\nTASK 10: Printing start stations:")
print(len(start_stations))
# print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(start_stations) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
"""
Example function with annotations.
Args:
  param1: The first parameter.
  param2: The second parameter.
Returns:
  List of X values

"""

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# Done: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"

def count_items(column_list):
    item_types = set(column_list)
    count_items = []

    for item in item_types:
        count_items.append(column_list.count(item))
    return item_types, count_items

if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 12: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 12: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 12: Returning wrong result!"
    # -----------------------------------------------------