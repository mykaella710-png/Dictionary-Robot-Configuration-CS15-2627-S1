robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}
robot["battery"] = 100
removed = robot.pop("mode")
robot["color"] = "pink"
print("Robot Name:", robot["name"])
print("Robot Model:", robot["model"])
print("Number of keys:", len(robot))
for key, value in robot.items():
    print(f"{key}: {value}")