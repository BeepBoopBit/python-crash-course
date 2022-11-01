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
