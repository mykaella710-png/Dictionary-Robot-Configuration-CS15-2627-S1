robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}

while True:
    print("Setting Menu:\n1. View All Settings\n2. Look Up a Setting\n3. Change a Setting\n4. Add a Setting\n5. Exit")
    decision = input("Selected option: ")
    if decision == "1":
        for key, value in robot.items():
            print(f"{key}: {value}")
    elif decision == "2":
        while True:
            choice = input("Which setting would you like to look up?\nSetting: ")
            choice = choice.lower()
            if choice in robot:
                print(f"{choice}: {robot.get(choice)}")
                break
            else:
                print("Setting is not in menu")
    elif decision == "3":
        while True:
            choice = input("Which setting would you like to change?\nSetting: ")
            choice = choice.lower()
            if choice in robot:
                robot[choice] = input("New value: ")
                print(f"{choice}: {robot[choice]}")
                break
            else:
                print("Setting is not in menu")
    elif decision == "4":
        new_sc = input("Input a new setting\nSetting: ")
        new_sc = new_sc.lower()
        if new_sc in robot:
            print("Setting is already in menu")
        else:
            robot[new_sc] = input("New value: ")
    elif decision == "5":
        break
    else:
        print("Invalid option")