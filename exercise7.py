runner_speeds = []
count = 1
i = "y"
while i == "y":
    distance = float(input("How far did person {} run (in metres)? ".format(count)))
    time = float(input("How long did it take for person {} to run {} metres? ".format(count, distance)))
    speed =  distance / (time*60)
    runner_speeds.append(speed)
    count += 1
    i = input("Keep going? (y/n) ")


def fastest_person(runner_speeds):
    fastest_so_far = 0
    for speed in runner_speeds:
        if speed > fastest_so_far:
            fastest_so_far = speed
    return fastest_so_far


winner = fastest_person(runner_speeds)
winner_number = runner_speeds.index(winner) + 1
print("Person {} was the fastest at {:.2f} m/s".format(winner_number, winner))
