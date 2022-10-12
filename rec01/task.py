from email import contentmanager
import os
from requests import get
import json
import csv
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class Task(object):

    def __init__(self):
        print('Downloading JSON file and printing entire file:')
        self.response = get(
            'http://db.cs.pitt.edu/courses/cs1656/data/hours.json',
            verify=False)
        print(self.response.content)

        print('Loading as JSON and iterating one line at a time:')
        self.hours = json.loads(self.response.content)
        print(self.hours)

        print('\nIterating over JSON:')
        for line in self.hours:
            print(line)

    def part4(self):
        csvOut = open("hours.csv", 'w', newline='')
        csvWrite = csv.writer(csvOut)
        count = 0

        for line in self.hours:
            count = count + 1
            keyNum = 0
            keys = []
            val = []

            for key in line:
                value = line[key]
                keys.append(key)
                val.append(value)
                keyNum = keyNum + 1

            if (count == 1):
                csvWrite.writerow(keys)
            csvWrite.writerow(val)

        csvOut.close()

    def part5(self):
        #write output to 'part5.txt'
        f = open('part5.txt', 'w')
        # csvFile = "hours.csv"

        if os.path.isfile(os.path.join(os.getcwd(), "hours.csv")):
            with open('hours.csv', newline='') as fi:
                contents = fi.read()
                print(contents)
                f.write(contents)
            fi.close()
        f.close()

    def part6(self):
        #write output to 'part6.txt'
        f = open('part6.txt', 'w')
        # csvFile = "hours.csv"

        if os.path.isfile(os.path.join(os.getcwd(), "hours.csv")):
            with open('hours.csv') as fi:
                csvReads = csv.reader(fi)
                for row in csvReads:
                    print(row)
                    f.write(str(row))
                f.close()
            f.close()

    def part7(self):
        #write output to 'part7.txt'
        f = open('part7.txt', 'w')
        # csvFile = "hours.csv"

        if os.path.isfile(os.path.join(os.getcwd(), "hours.csv")):
            with open('hours.csv') as fi:
                rows = csv.reader(fi)
                for row in rows:
                    for i in range(len(row)):
                        print(row[i])
                        f.write(row[i])
            fi.close()
        f.close()


if __name__ == '__main__':
    task = Task()
    task.part4()
    task.part5()
    task.part6()
    task.part7()
