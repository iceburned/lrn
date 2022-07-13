dkt = {}                                         #contest pass and name
contest = {}                                     #dict with users and their contests
data = input()

while not data == "end of contests":             #contest and pass cicle
    k, v = data.split(":")
    dkt[k] = v
    data = input()
data1 = input()

while not data1 == "end of submissions":         #users and their contests cicle
    k1, password, name, points = data1.split("=>")
    points = int(points)
    if k1 in dkt.keys() and dkt[k1] == password:  #contest is valid (It is considered valid if you received it in the first type of input)
        if name not in contest:
            contest[name] = {}                    #add  person in contest dictionary
        if k1 not in contest[name]:
            contest[name].update({k1: points})    #add contest and points if none
        else:
            if contest[name][k1] <= points:       #add contest if poitns are bigger than present
                contest[name].update({k1: points})
    data1 = input()

total_points = 0
user = ""

for key in contest.keys():                        #whom is with most points
    if sum(contest[key].values()) > total_points:
        total_points = sum(contest[key].values())
        user = key
print(f"Best candidate is {user} with total {total_points} points.\nRanking:")


contest = dict(sorted(contest.items(), key=lambda x: x[0]))     #sort by key


for username, values in contest.items():
    print(username)
    values = dict(sorted(values.items(), key=lambda x: -x[1]))  #sort nested dict by value
    for con, po in values.items():
        print(f"#  {con} -> {po}")

"""
Part One Interview:success#
JS Fundamentals:fundExam
C# Fundamentals:fundPass
Algorithms:fun
end of contests
C# Fundamentals=>fundPass=>Tanya=>350
Algorithms=>fun=>Tanya=>380
Part One Interview=>success#=>Nikola=>120
Java Basics Exam=>wrong_pass=>Teo=>400
Part One Interview=>success#=>Tanya=>220
OOP Advanced=>password123=>Kay=>231
C# Fundamentals=>fundPass=>Tanya=>250
C# Fundamentals=>fundPass=>Nikola=>200
JS Fundamentals=>fundExam=>Tanya=>400
end of submissions
"""