name = "Bob"

print (f"Hello, {name}")

name = "Rolf"

print (f"Hello, {name}")

name = "Bob"
gretting = "Hello, {}"
with_name = gretting.format(name)
with_name_two = gretting.format("Rolf")

print (with_name)
print (with_name_two)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf","Monday")
print (formatted)