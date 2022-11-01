A = 1
B = 2
C = 3

print(A == B & B == C)
print (A == B | B == C)

A = "water"
B = "melon"
C = "papaya"

print(A.lower() == B.lower())
print(A.lower() != B.lower() | B == C.lower())

things = ['water', 'melon', 'papaya', 'banana', 'fruit', 'salad']

if 'melon' in things:
    print("shemay shemay")
if 'water' not in things:
    print("eme eme")