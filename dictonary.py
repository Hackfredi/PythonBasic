#**Creating a Dictionary:**
#   Think of a dictionary like a phone book. It has a list of names (keys) and their corresponding phone numbers (values).
# In Python, you can create a dictionary by putting these pairs inside curly braces `{}`.

my_dict = {
       "name": "John",       # Key: "name", Value: "John"
       "age": 30,            # Key: "age", Value: 30
       "city": "New York"    # Key: "city", Value: "New York"
   }

# **Accessing Values:**
#  If you want to find someone's phone number in the phone book (dictionary), you look up their name (key) to get their number (value).

name = my_dict["name"]  # Get the value associated with the key "name"
age = my_dict.get("age")  # Get the value associated with the key "age" using the get() method

# **Modifying a Dictionary:**
#  If someone's age changes or they move to a different city, you can update their information in the phone book.

my_dict["age"] = 31  # Update the value associated with the key "age" to 31
my_dict["city"] = "Los Angeles"  # Update the value associated with the key "city" to "Los Angeles"

#**Adding New Key-Value Pairs:**
#  You can add a new person to the phone book by providing their name (key) and phone number (value).


my_dict["country"] = "USA"  # Add a new key-value pair: Key "country" with Value "USA"


#**Removing Key-Value Pairs:**
#  If you want to remove someone from the phone book, you can delete their entry.

del my_dict["age"]  # Remove the key "age" and its associated value
country = my_dict.pop("country")  # Remove the key "country" and get its associated value

#**Iterating Over a Dictionary:**
#If you want to go through the entire phone book to see all the names and phone numbers, you can use a loop.

for key in my_dict:
    print(key, my_dict[key])  # Print each name (key) and its corresponding phone number (value)

for value in my_dict.values():
       print(value)  # Print each phone number (value)

for key, value in my_dict.items():
       print(key, value)  # Print each name (key) and its corresponding phone number (value)


#**Checking if a Key Exists:**
#You can check if a specific name (key) is in the phone book.

if "name" in my_dict:
 print("Name:", my_dict["name"])  # Check if "name" is a key in the phone book and print the associated value

#In summary, dictionaries in Python work like a phone book, where you store pairs of information (keys and values).
#You can add, modify, remove, and search for this information easily using Python's dictionary features.