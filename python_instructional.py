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
    Python is a littler looser in variable declaration than other stronger typed languages.
    
    Variables are critical to development, used to store hard-coded or dynamic values.
    
	Names: 
		Variables can be named anything, you can literally use a variable called 'ShitBag'.
        It does not matter to the machine one bit.
        
        That said there is a ton of debate and discussion around variable names, 
        for professional work and general code maintainability it's best to use concise but descriptive names.
        (Many hours are burnt just picking the appropriate variable name...)

        I recommened reviewing python PEP-8 for python standards that are accepted by most professional python devs.
        Following PEP-8 standards means most python code you review should follow similar patterns and make it easier to read.
        
        e.g., EcamaScript (Javascript) it's standard to camelCase vars, in python underscore_notation is preferred.
    
    Key Notes:
		You can declare a variable by writing a name and assigning a variable, you can't declare a unassigned variable
        but you can create a placeholder by giving it a null or empty value.
"""
# Examples:
ThisIsAValidVariableName = True
print(f"Printing Variable 'ThisIsAValidVariableName': {ThisIsAValidVariableName}")
this_is_a_valid_variable_name = True
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

string_variable = 'Hi, this is a representation of a string!'

int_variable = 12345

list_variable = [1,2,'lists can comprise various items', 4, 5, 'comma seperated', 'though not ideal to mix data-types in a list', 9999]

dict_variable = {'Key1':'value', 'Key2':'Value2'}

tuple_variable = (1,2)

# Strings are characters, ints are numbers, lists are comma seperated elements which can be strings or numbers.
# dictionaries are JSON like key-value pairs.




