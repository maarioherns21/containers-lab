# # Python Containers - Lab

# **This lab is a deliverable**

# ## Setup


# ## Exercises

# #### Exercise 1

# - Create a list named `students` containing some student names (strings).
# - Print out the second student's name.
# - Print out the last student's name.
students = ['robert', 'chirstopher', 'cheepy']
print(students[1])
print(students[2])


# #### Exercise 2
# - Create a tuple named `foods` containing the same number of foods (strings) as there are names in the `students` list.
# - Use a `for` loop to print out the string "_food goes here_ is a good food".
foods = ('tomatoes', 'carrots', 'bananas')
for item in (foods):
    print(f"{item} is a good food")

# #### Exercise 3
# - Using a `for` loop, print just the last two food strings from `foods`.
foods = ('tomatoes', 'carrots', 'bananas')
for item in (foods[1:]):
    print(f"{item} is a good food")


# #### Exercise 4

# - Create a dictionary named `home_town` containing the keys of `city`, `state` and `population`.
# - Print a string with this format:<br>"I was born in _city_, _state_ - population of _population_"
home_town = [{
    'city': 'Oakland',
    'state': 'CA',
    'population': 3432
}]
for thing in home_town:
    print(
        f"I was born in {thing['city']}, {thing['state']} population of {thing['population']}")
# #### Exercise 5

# - Iterate over the _key: value_ pairs in `home_town` and print a string for each item, for example:<br>"city = Arcadia"<br>"state = California"<br>"population = 58000"
home_town = {
    'city': 'Oakland',
    'state': 'CA',
    'population': 3432
}
for key, val in home_town.items():
    print(f"{key} = {val} ")
# #### Exercise 6
# - Create an empty list named `cohort`.
# - Using a `for` loop, add one dictionary to the `cohort` list for each student name. Each dictionary should have this shape:
# - Iterate over `cohort` printing out each element.
cohort = []
cohort.append({'student': 'laura', 'fav_food': 'cheeseburgers'})
for item in cohort:
  print(cohort)




# #### Exercise 7

# - Using the list of `students` and list comprehension, assign to a variable named `awesome_students` a new list containing strings similar to this:<br>`["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]`
# - Iterate over `awesome_students` printing out each string.
cohort = []
cohort.append({'student': 'laura', 'fav_food': 'cheeseburgers'})
cohort.append({'student': 'monica', 'fav_food': 'pizza'})
for item in cohort:
  print(f"{item['student']} loves {item['fav_food']}")

awesome_students = cohort
print(f"{item['student']} loves {item['fav_food']}")

# #### Exercise 8

# - Using the tuple `foods` and list comprehension within a `for` loop, print each food string that contains the letter `a`.
foods = ('tomatoes', 'carrots', 'bananas')
for food in [food for food in foods if 'a' in food]:
  print(food)
