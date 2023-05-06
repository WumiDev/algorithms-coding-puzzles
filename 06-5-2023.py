runners = {
    "John": {"speed": 10, "run_time": 6, "rest_time": 20},
    "James": {"speed": 8, "run_time": 8, "rest_time": 25},
    "Jenna": {"speed": 12, "run_time": 5, "rest_time": 16},
    "Josh": {"speed": 7, "run_time": 7, "rest_time": 23},
    "Jacob": {"speed": 9, "run_time": 4, "rest_time": 32},
    "Jerry": {"speed": 5, "run_time": 9, "rest_time": 18}
}

total_time = 1234
distances = {}

for name, data in runners.items():
    speed = data["speed"]
    run_time = data["run_time"]
    rest_time = data["rest_time"]
    distance = 0
    time_left = total_time
    while time_left > 0:
        if time_left >= run_time:
            distance += speed * run_time
            time_left -= run_time
        else:
            distance += speed * time_left
            time_left = 0
        time_left -= rest_time
    distances[name] = distance

winner = max(distances, key=distances.get)
print(f"The distance of the winning runner after 1234 seconds is {distances[winner]}m and the winner is {winner}!")
