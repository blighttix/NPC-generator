import random
# introduction to the generator
print("Intelligence, charisma, and strength are all on a scale from 1 to 10\n")
amount = int(input("How many characters would you like? "))
counter = 0

# Attributes
first_name = ["Chris", "Joe", "Elissa", "Sarah", "Alex", "Edward", "Karl", "Melvin", "Kim", "Nicholas", "Lilly", "Jack", "Tom", "Julia", "Hank", "Zoe", "Makenzie", "Steve", "Dennis", "Kate", "Peter", "George", "Mabel"]
last_name = ["Reynolds", "Smith", "Stanley", "Green", "Columbus", "Taylor", "Walker", "Evans", "Kelley", "Grannis", "Thompson", "Simons", "Hawley", "Toledo", "Wilson", "Pilgrim", "Maxwell", "Franklin", "Bishop", "Parker", "Hill"]
age = random.randint(1, 99)
intelligence = random.randint(1, 10)
charisma = random.randint(1, 10)
strength = random.randint(1, 10)
print("\n")

# creates the amount of characters specified
while counter < amount:
    print(random.choice(first_name), random.choice(last_name), f" - Age: {age}    Intelligence: {intelligence}    Charisma: {charisma}    Strength: {strength}")
    age = random.randint(1, 99)
    intelligence = random.randint(1, 10)
    charisma = random.randint(1, 10)
    strength = random.randint(1, 10)
    counter += 1
