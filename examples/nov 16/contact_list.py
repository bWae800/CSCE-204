from person import Person

#friend = Person("Sally", "White", "803-656-6677")

#friend.display()

people = []
people.append(Person("Amy", "Anderson", "803-444-3343"))
people.append(Person("Bobby", "Blat", "803-375-6969"))
people.append(Person("Carl", "Dave", "803-129-3343"))
people.append(Person("Doug", "Dimmadome", "803-420-4207"))
#loop through the list and display the people

for person in people:
    person.display()