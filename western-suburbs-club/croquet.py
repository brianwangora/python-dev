
# each entry in inputList represents a member and contains their [age, handicap]
inputList = [[35,25],[62,0],[56,12],[58,-3],[72,5],[45,2],[35,-5],[67,4]]

for i in inputList:
    if i[0] >= 55 and i[1] < 7 and i[1] >= -2:
        print("Senior")
    elif i[0] < 55 and i[1] >= 7 and i[1] <= 26:
        print("open")
    elif i[0] < 55 and i[1] < 7 and i[1] >= -2:
        print("open")
    elif i[0] >= 55 and i[1] >= 7 and i[1] <= 26:
        print("open")
    else: 
        print("Wrong handicap information entered")
   