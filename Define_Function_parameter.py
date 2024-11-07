#Understanding F-String
#Basic Example
price = 59
text = (f"The Price is {price}")
print(text)
def Happy_Birthday(name):
    print(f"Happy Birthday {name}")
#While defining Function we can make to do like as below
#Without F-String Output will be Happy Birthday{name}
#F-string will take the values inside the parameter, {} dictionary color will change show as enabled
Happy_Birthday("Susan")
#Below is better complicated example
def happy_birthday(name,age):
    print(f"Happy Birthday {name}")
    print(f"You Turned {age} Today!!")
happy_birthday("Susan",32)
