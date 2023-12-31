"""
	Intro to Brogramming in Python.
    Note: This is not a comprehensive instructional, there is a plethora
	    	of solid trainings that can better deep dive concepts - so I will just
        brush over what I consider core concepts and try to relate them in a way
        that would have better helped me when I started out...
"""

"""
VARIABLES
	Variables are just objects you can assign a varying "variable" number of values to.
    Python is a little looser in variable declaration than other stronger typed languages.
    
    Variables are critical to development, used to store hard-coded or dynamic values.
    
	Names: 
		Variables can be named anything, you can literally use a variable called 'ShitBag'.
        It does not matter to the machine one bit.
        
        That said there is a ton of debate and discussion around variable names, 
        for professional work and general code maintainability it's best to use concise but descriptive names.
        (Many hours are burnt just picking the appropriate variable name...)

        I recommened reviewing python PEP-8 https://peps.python.org/pep-0008/
        for python standards that are accepted by most professional python devs.
        Following PEP-8 standards means most python code you review should follow similar patterns and make it easier to read.
        
        e.g., EcmaScript (Javascript) it's standard to camelCase vars, in python underscore_notation is preferred.
    
    Key Notes:
		You can declare a variable by writing a name and assigning a variable, you can't declare a unassigned variable
        but you can create a placeholder by giving it a null or empty value.
"""
# Examples:
ThisIsAValidVariableName = True
print(f"Printing Variable 'ThisIsAValidVariableName': {ThisIsAValidVariableName}")
this_is_a_valid_variable_name = True
print(f"Printing Variable 'this_is_a_valid_variable_name': {this_is_a_valid_variable_name}")

# You can then re-assign variables values after initial use:
this_is_a_valid_variable_name = False
#You'll notice when ran, the printed output will now be False...
print(f"Printing Variable 'this_is_a_valid_variable_name': {this_is_a_valid_variable_name}")


"""
DATA TYPES

	Theres several key data-types which are almost universal across all programming languages, though
	their name may and is likely different.
    
    Text Type: str
	Numeric Types: int, float, complex
	Sequence Types: list, tuple, range
	Mapping Type: dict
	Set Types: set, frozenset
	Boolean Type: bool
	Binary Types: bytes, bytearray, memoryview
	None Type: NoneType
    
    The key datatypes would be strings, integers, lists, dicts, tuples, bools, bytes and Nones.
    
    Key Notes:
		Each data type will give you different functionality and trying to assign different types can cause error.
        Variables don't care what they receive in python so you may want to check if what you dynamically receive is the correct type.
"""
# Examples:
string_example = 'Hi, this is a representation of a string!'

int_example = 12345

float_example = 3.14

#lists are wrapped in square brackets [ ]
list_example = [1,2, 4, 5, 9999]
list_example_2 = ['list', 'of', 'strings']
# you can also have lists of tuples, dicts and other objects!

#dicts are wrapped in curly braces { } and comprise of Key:Value pairs. 
dict_variable = {'Key1':'value', 'Key2':'17827881238', 'Name':'John Doe', 'Age':39}

#tuples are wrapped in parenthesis ( ) and are immutable.
tuple_variable = (1,2)

"""FUNCTIONALITY
		Even the most complex code can be boiled down to a few key functions,
        typically if/else statements and some form of loops. (oversimplification, but still valid)
"""

"""
	If/Elif/Else:
        if/else statements are pretty self explanitory.
			Say you're going to the store to buy your spouse Whole milk, but "IF they don't have whole milk, get 2%."
            Congrats, you just completed a if/else block.

            You can enhance this with elif (else-if) allowing you to daisy chain if statements.
        
        Once a condition is met, the code indented under that conditional will begin running.
"""
# Examples

# variable with value of "Whole Milk" for the if/else examples.
milk_store_stock = 'Whole Milk'

if milk_store_stock == 'Whole Milk':
    print("Woah! they've got whole milk")
    # code to purchase the whole milk goes here
elif milk_store_stock == '2% milk':
    print("Damn! no whole milk, but they've got 2%.")
	# code to handle 2% milk here
else:
    print("no whole milk nor 2%, what should we do?")
    # code to handle there being no Whole Milk or 2% milk goes here...

"""
	For Loop:
		the amazing for loop.     
"""


# TO BE CONTINUED...