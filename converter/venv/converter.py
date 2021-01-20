import csv
from operator import itemgetter

def convert(path, config):
    with open(path[0], 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        print(path[0])

        with open(config, 'r') as c:
            reader = csv.reader(c)
            startingPoints = list(reader)

            xDiff = 0
            yDiff = 0
            zDiff = 0

            for i in startingPoints:
                if i[0] == path[1]:
                    xDiff = float(i[2])
                    yDiff = float(i[3])
                    zDiff = float(i[4])

            for line in data:
                if line != ['time', 'ax', 'ay', 'az', 'floor'] and line[0] != '':
                    time = float(line[0])
                    x = float(line[1])
                    y = float(line[2])
                    z = float(line[3])

                    if (time * 10) % 1 == 0:
                        newLine = [time, path[1], xDiff, yDiff, zDiff]
                        output.append(newLine)

                    else:
                        xDiff = xDiff + x
                        yDiff = yDiff + y
                        zDiff = zDiff + z

paths = [
    ['data/Group 1/4.csv', 'SW1'],
    ['data/Group 1/8.csv', 'SW2'],
    ['data/Group 1/12.csv', 'SW3'],
    ['data/Group 1/16.csv', 'SW4'],
    ['data/Group 1/20.csv', 'SW5'],
    ['data/Group 1/24.csv', 'SW6'],
    ['data/Group 1/28.csv', 'SW7'],
    ['data/Group 1/32.csv', 'SW8'],
    ['data/Group 1/36.csv', 'SW9'],
    ['data/Group 1/40.csv', 'SW10'],
    ['data/Group 1/44.csv', 'SW11'],
    ['data/Group 1/48.csv', 'SW12'],
    ['data/Group 1/52.csv', 'SW13'],
    ['data/Group 1/56.csv', 'SW14'],
    ['data/Group 1/60.csv', 'SW15'],
    ['data/Group 1/64.csv', 'SW16'],
    ['data/Group 1/68.csv', 'SW17'],
    ['data/Group 1/72.csv', 'SW18'],
    ['data/Group 1/76.csv', 'SW19'],
    ['data/Group 1/80.csv', 'SW20'],
    ['data/Group 2/5.csv', 'NW1'],
    ['data/Group 2/9.csv', 'NW2'],
    ['data/Group 2/13.csv', 'NW3'],
    ['data/Group 2/17.csv', 'NW4'],
    ['data/Group 2/21.csv', 'NW5'],
    ['data/Group 2/25.csv', 'NW6'],
    ['data/Group 2/29.csv', 'NW7'],
    ['data/Group 2/33.csv', 'NW8'],
    ['data/Group 2/37.csv', 'NW9'],
    ['data/Group 2/41.csv', 'NW10'],
    ['data/Group 2/45.csv', 'NW11'],
    ['data/Group 2/49.csv', 'NW12'],
    ['data/Group 2/53.csv', 'NW13'],
    ['data/Group 2/57.csv', 'NW14'],
    ['data/Group 2/61.csv', 'NW15'],
    ['data/Group 2/65.csv', 'NW16'],
    ['data/Group 2/69.csv', 'NW17'],
    ['data/Group 2/73.csv', 'NW18'],
    ['data/Group 2/77.csv', 'NW19'],
    ['data/Group 2/81.csv', 'NW20'],
    ['data/Group 3/6.csv', 'SE1'],
    ['data/Group 3/10.csv', 'SE2'],
    ['data/Group 3/14.csv', 'SE3'],
    ['data/Group 3/18.csv', 'SE4'],
    ['data/Group 3/22.csv', 'SE5'],
    ['data/Group 3/26.csv', 'SE6'],
    ['data/Group 3/30.csv', 'SE7'],
    ['data/Group 3/34.csv', 'SE8'],
    ['data/Group 3/38.csv', 'SE9'],
    ['data/Group 3/42.csv', 'SE10'],
    ['data/Group 3/46.csv', 'SE11'],
    ['data/Group 3/50.csv', 'SE12'],
    ['data/Group 3/54.csv', 'SE13'],
    ['data/Group 3/58.csv', 'SE14'],
    ['data/Group 3/62.csv', 'SE15'],
    ['data/Group 3/67.csv', 'SE16'],
    ['data/Group 3/71.csv', 'SE17'],
    ['data/Group 3/75.csv', 'SE18'],
    ['data/Group 3/79.csv', 'SE19'],
    ['data/Group 3/83.csv', 'SE20'],
    ['data/Group 4/7.csv', 'NE1'],
    ['data/Group 4/11.csv', 'NE2'],
    ['data/Group 4/15.csv', 'NE3'],
    ['data/Group 4/19.csv', 'NE4'],
    ['data/Group 4/23.csv', 'NE5'],
    ['data/Group 4/27.csv', 'NE6'],
    ['data/Group 4/31.csv', 'NE7'],
    ['data/Group 4/35.csv', 'NE8'],
    ['data/Group 4/39.csv', 'NE9'],
    ['data/Group 4/43.csv', 'NE10'],
    ['data/Group 4/47.csv', 'NE11'],
    ['data/Group 4/51.csv', 'NE12'],
    ['data/Group 4/55.csv', 'NE13'],
    ['data/Group 4/59.csv', 'NE14'],
    ['data/Group 4/63.csv', 'NE15'],
    ['data/Group 4/66.csv', 'NE16'],
    ['data/Group 4/70.csv', 'NE17'],
    ['data/Group 4/74.csv', 'NE18'],
    ['data/Group 4/78.csv', 'NE19'],
    ['data/Group 4/82.csv', 'NE20'],
]

config = 'config.csv'

output = []

print('converting ' , len(paths), ' files...')
for path in paths:
    convert(path, config)
print('done converting.')
print('sorting ', len(output), ' lines...')
sortedOutput = sorted(output, key=itemgetter(0))
print('done sorting.')
print('exporting to csv...')
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sortedOutput)
print('done exporting.')
