#https://www.hackerrank.com/challenges/little-chammys-huge-donation
import sys
squaredRange = [x*x for x in range(1, 1000)]

def compute(input_value):
        current_value = int(input_value)
        personCompleteCounter = 0

        for e in squaredRange:
                if current_value >= e and current_value != 0:
                        current_value -= e
                        personCompleteCounter += 1
                else:
                        sys.stdout.write("%s" %  personCompleteCounter + '\n')
                        return
firstLine = True
for line in sys.stdin:
        if firstLine:
            firstLine = False
        else:
            compute(line)
