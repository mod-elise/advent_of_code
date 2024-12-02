with open('input.txt') as f:
    reports = f.read().splitlines()

def checkSafe(report, direction):
    for idx in range(1, len(report)):
        if checkDirection(report, idx-1, idx) != direction:
            return False
        if abs(report[idx-1] - report[idx]) > 3 or report[idx-1] == report[idx]:
            return False
    return True

def dampener(report):
    values_removed = set()
    for idx, value in enumerate(report):
        temp = report[:idx] + report[idx+1:]
        direction = checkDirection(temp, 0, len(temp) - 1)
        if checkSafe(temp, direction):
            values_removed.add(value)
    return len(values_removed) > 0

def checkDirection(report, first, second):
    return 'down' if report[first] > report[second] else 'up' if report[first] < report[second] else 'same'

sum = 0
dampener_sum = 0

for report in reports:
    dampener_triggered = False
    report = report.split()
    report = [int(x) for x in report]
    direction = checkDirection(report, 0, len(report) - 1)
    isSafe = checkSafe(report, direction)
    if isSafe:
        sum += 1
    else:
        isSafe = dampener(report)
        if isSafe:
            dampener_sum += 1

print (f'The number of safe reports with no dampener is {sum}')
print (f'The number of safe reports with dampener is {sum + dampener_sum}')
