# age_converter.py

first_name = "Jake"
# give "first name" variable a name
age_years = 24

age_secs = age_years * 60 * 60 * 24 * 365

print(f"Hello, my name is {first_name}.")
# f string in print function allows one to display message with current value of the variable "first_name"
print(f"I am {age_years} years old", end=", ")
# f string shows message containing current value of "age_years" variable, with a space at the end
print(f"which is {age_secs:,} seconds.")
# ":," makes sure commas separate thousands (e.g. 1,000,000 vs 1000000)
