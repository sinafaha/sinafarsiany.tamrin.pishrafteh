n = int(input("Please enter the number of exams"))
scores_guide = {"A":5, "B":4, "C":3, "D":2, "E":1}
all_units = 0
total = 0
for i in range(n):
    x = str(input("Please enter the weight & score:\n"))
    score = int(x.split(" ")[0]) * scores_guide[x.split(" ")[1].upper()]
    all_units += int(x.split(" ")[0])
    total += score
print(all_units)
avg = total//all_units +1
avg_in_letter = ""
print(scores_guide.items())
for i in scores_guide:
    if scores_guide[i] == avg:
        avg_in_letter = i
        break
print("The average is: {}".format(avg_in_letter))
