#!/usr/bin/env python3

from pretty_str import pretty_str

# Pass in a string and an attribute:
message1 = pretty_str("Hello world!", "bold")
print(message1)  # bold

# Multiple attributes can be passed in as an iterable:
attrs = ["bold", "italic", "blue", "bg_red"]
message2 = pretty_str("Multiple attributes can be used.", attrs)
print(message2)  # blue bold-italic on red background

# Attributes that are not mutually exclusive can be composed:
b = pretty_str("bold", "bold")
i = pretty_str("italic", "italic")
u = pretty_str("underline", "underline")
message3 = pretty_str(f"Attributes can be composed: {b}, {i}, {u}", "blue")
print(message3)  # blue with different faces for each word

# Attributes that are mutually exclusive get overwritten:
message4 = pretty_str("Only one color at a time!", ["blue", "red"])
print(message4)  # red

# Attributes can be reset with the 'default' attributes:
default_attrs = ["default_face", "default_color", "default_bg_color"]
defaults = pretty_str("defaults", default_attrs)
message5 = pretty_str(f"Use {defaults} mid-string.", ["bold", "blue", "bg_red"])
print(message5)  # blue bold on a red background, with 'hello' as normal

# Non-existent attributes will raise a ValueError:
try:
    message6 = pretty_str("This will not work!", "NonAttr")
except ValueError as error:
    print(error)
else:
    print(message6)
