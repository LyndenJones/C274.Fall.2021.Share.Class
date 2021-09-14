# Part 2
theCount = 0
word = input("Word: ")
targetWords = ['outside', 'today', 'weather', 'raining', 'nice', 'rain', 'snow', 'day', 'winter', 'cold', 'warm', 'snowing', 'out', 'hope', 'boots', 'sunny', 'windy', 'coming', 'perfect', 'need', 'sun']
if word in targetWords:
    theCount = theCount + 1
print("Total count %s" % (theCount))
