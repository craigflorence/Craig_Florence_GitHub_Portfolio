# Python dictionaries are called Associative arrays, as they display an array of data with a key and value.
# When creating a dict by using {} the Keys need to be in " ".
# When creating a dict by using dict() the keys do not need " ".
# When adding new Key/Values to a dict you use [] to name the key, then = the value.

# user_id = 209
# message = "D5 E5 C5 C4 G4"
# language = "English"

user_post = {"user_id": 209, "message": "D5 E5 C5 C4 G4"}
user_post2 = dict(message="101010110101011110101", language="Binary")
print(user_post2)
user_post2["user_id"] = 210
print(user_post2)

# You can view a key value by calling it, but if the key doesn't exist you will get a KeyValue error.

print(user_post2["user_id"])

# Alternatively you can use the get() method to look for a key, get the value and give a default response if it fails.

print(user_post2.get("language", None))

value = "Hello"
