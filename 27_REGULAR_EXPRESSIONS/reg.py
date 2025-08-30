# used in string matching!

import re
text = "The quick brown fox jumps over the lazy dog fox."

# match = re.search("brown", text)
# print(match)

# string = ""
# if string:

# if match:
#   print("Match Found!")
#   print("Start Index: ", match.start())
#   print("End Index: ", match.end())

# matches = re.findall("the", text, re.IGNORECASE)  
# print(matches)
# print(type(matches))

# to replace all occurences:

new_text = re.sub("fox", "cat", text)
print(new_text)
print(type(new_text))