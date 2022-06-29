# Use the list.sort() method.
# It modifies the list in-place (and returns None to avoid confusion).
a = [5, 2, 3, 1, 4]
print("Before...", a)
a.sort()
print("After...", a)

# sorted() function. It returns a new sorted list:
print("\nUsing sorted()...", sorted([5, 2, 3, 1, 4]))

# Another difference is that the list.sort() method is only defined for lists. 
# In contrast, the sorted() function accepts any iterable.
print("\nUsing sorted() to sort a dict: ", sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))

# Key Functions
# Both list.sort() and sorted() have a key parameter to specify a function (or other callable)
# to be called on each list element prior to making comparisons.
# For example, here’s a case-insensitive string comparison:
print("\nSort using key=str.lower...")
print(sorted("This is a test string from Andrew".split(), key=str.lower))

# The value of the key parameter should be a function (or other callable) that takes a single argument 
# and returns a key to use for sorting purposes.
# This technique is fast because the key function is called exactly once for each input record.
# A common pattern is to sort complex objects using some of the object’s indices as keys. For example:
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print("\nBefore (tuples): ", student_tuples)
print("\n Sort on age...")
print(sorted(student_tuples, key=lambda student: student[2]))   # sort by age
print("\nAfter: ", student_tuples)  # no change to the original list.

# The same technique works for objects with named attributes. For example:
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print("\nBefore (objects)...", student_objects)
print(sorted(student_objects, key=lambda student: student.age))   # sort by age

# Using itemgetter and attrgetter.
from operator import itemgetter, attrgetter
print("\nUsing itemgetter()...", sorted(student_tuples, key=itemgetter(2)))

print("\nUsing attrgetter()...", sorted(student_objects, key=attrgetter('age')))

# sort by grade then by age:
print("\nUsing itemgetter() sort on grade then age...", sorted(student_tuples, key=itemgetter(1,2)))

print("\nUsing attrgetter() sort on grade then age...", sorted(student_objects, key=attrgetter('grade', 'age')))

# ASC / DESC.
# get the student data in reverse age order:
print("\nUsing itemgetter() DESC...", sorted(student_tuples, key=itemgetter(2), reverse=True))
print("\nUsing attrgetter() DESC...", sorted(student_objects, key=attrgetter('age'), reverse=True))
