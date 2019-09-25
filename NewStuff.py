age = 23
# str method
print("My age " + str(age) + " years")

# replacement field = {}
print("My age is  {0} years".format(age))
# Replace multiple things at once.
print("There are new day called {0}, {1}, {2}".format("Jackson", "Steve", "and Jerry"))
# string formating operated
print("""
Joke: {1}
Joke: {0}
""".format(1, 5))

# replace(old format)
print("My age is %d %s" % (age, "years"))

# for loop
for i in range(1, 12):
    print("No, %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))

# Better formating
for i in range(1, 12):
    print("No, {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

q = 10.0
p = 5.0
t = q * p
t1 = t / 5

T = t + t1
print(T)

parrot = "Blue McKaw"
print(parrot[0:6:2])