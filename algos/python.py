thisdic = {
    "brand": "ford",
    "model": "F-150",
    "year": 2014,
    "color": "blue"
}
print(thisdic["brand"])
print(len(thisdic))
print(type(thisdic))
thisdic["year"] = 2022
print(thisdic["year"])
thisdic.pop("year")
print(thisdic)
thisdic.popitem()
print(thisdic)

food = ["car", "bat", "apple", "dog"]
for x in food:
    if x == "apple":
        print("found it")
    else:
        print(x)
print(6 + 7 + int('7'))

food = 5
good = "bob"
print(food)
print(str(good))
print(type(good))


# Declare a function that can handle ZeroDivisionError
def divide_twelve(number):
    try:
        print(f"Result: {12/number}")
    except ZeroDivisionError:
        print("You can't divide 12 by zero.")


# Use the function
divide_twelve(6)
# Result: 2.0
divide_twelve(0)
# You can't divide 12 by zero.
