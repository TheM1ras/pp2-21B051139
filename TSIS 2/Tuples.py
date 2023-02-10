names = ("Nikita", "Ivan", "Askar")
faculty = ("FIT", "ISE", "BS")
names_and_faculty  = names + faculty
print(names_and_faculty)
(a, b, *c) = names_and_faculty
print(a)
print(b)
print(c)