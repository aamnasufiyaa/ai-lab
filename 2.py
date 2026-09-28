# Vacuum Cleaner Agent

room_A = input("Enter status of Room A (Dirty/Clean): ")
room_B = input("Enter status of Room B (Dirty/Clean): ")

rooms = {
    "A": room_A,
    "B": room_B
}

for room in rooms:
    print("\nCurrent room:", room)
    print("Status:", rooms[room])

    if rooms[room].lower() == "dirty":
        print("Cleaning", room)
        rooms[room] = "Clean"
    else:
        print(room, "is already clean")

print("\nFinal room status:", rooms)
