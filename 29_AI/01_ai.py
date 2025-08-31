import re

def convert_to_dash(text):
    # Remove all non-alphanumeric characters except spaces
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Replace spaces (one or more) with a single dash
    dashed = re.sub(r'\s+', '-', cleaned)
    return dashed.lower()  # optional: convert to lowercase

# Example usage
text = "hey this is good!"
result = convert_to_dash(text)
print(result)  # Output: hey-this-is-good
