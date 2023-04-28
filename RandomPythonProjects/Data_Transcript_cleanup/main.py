with open("text.txt", "r") as handler:
    text = handler.readlines()

for line in text:
    try:
        currLine = line.split(":")
        #print(currLine)
        int(currLine[0])
        int(currLine[1])
        text.remove(line)
    except:
        currLine = line.split("\n")
        line = currLine[0]
print(text)
finishedText = " ".join(text)
tempText = finishedText.split("\n")
finishedText = " ".join(tempText)

print(finishedText)

with open("finishedText.txt", "w") as handler:
    handler.write(finishedText)