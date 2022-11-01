guest_list = ["water", "melon", "papaya"]

message = "I would like to invite you to a dinner party"

print(f"Hello {guest_list[0]}, {message}")
print(f"Hello {guest_list[1]}, {message}")
print(f"Hello {guest_list[2]}, {message}")

print(f"I'm sorry but {guest_list[1]} can't make it to the dinner party")

guest_list[1] = "fruit"

print(f"Hello {guest_list[0]}, {message}")
print(f"Hello {guest_list[1]}, {message}")
print(f"Hello {guest_list[2]}, {message}")

print("Good day everyone, since I found a bigger table, I would invite more guest to the dinner party")


guest_list.insert(0,"banana")
guest_list.insert(2, "melon")
guest_list.append("salad")

print("Yes I know, melon is back again")


print(f"Hello {guest_list[0]}, {message}")
print(f"Hello {guest_list[1]}, {message}")
print(f"Hello {guest_list[2]}, {message}")
print(f"Hello {guest_list[3]}, {message}")
print(f"Hello {guest_list[4]}, {message}")
print(f"Hello {guest_list[5]}, {message}")


print("I'm sorry guys, but I can't invite more people since the table wouldn't arrive in time")

print(f"I'm sorry {guest_list.pop()}, you can't come to the dinner party anymore")
print(f"I'm sorry {guest_list.pop()}, you can't come to the dinner party anymore")
print(f"I'm sorry {guest_list.pop()}, you can't come to the dinner party anymore")
print(f"I'm sorry {guest_list.pop()}, you can't come to the dinner party anymore")


message = "You are still invited to the dinner party"
print(f"Hello {guest_list[0]}, {message}")
print(f"Hello {guest_list[1]}, {message}")

del guest_list[0]
del guest_list[1]

print(guest_list)
