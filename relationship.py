import json
import random
from math import sqrt,log
Data = {"nodes":[], "links":[]}
SponorUsers = []
MaxDis = 0;
# for check whether two users are in the same group
def TheSameGroup(user1, user2):
    global groups
    for i in range(GroupNum):
        if(user1 in groups[i]["members"] and user2 in groups[i]["members"]):
            return True
    return False
	
# evaluate two users' similarity
def evaluate(user1, user2): 
    intersection = list(set(user1).intersection(set(user2)))
    union = list(set(user1).union(set(user2)))
    x = (len(intersection) * 1.0+3) / sqrt(len(union))
    return 7*log(1.5+18*x)+x*2-11
# refresh the groups' center for new turn iteration
def CenterCheck(group):
    MinDis = 100000;
    id = -1;
    for user in group["members"]:
        distance = 0
        for another in group["members"]:
            distance += evaluate(SponorUsers[user], SponorUsers[another])
        if(distance < MinDis):
            id = user
    return id
with open("alluserlocal.json", encoding='gb18030') as f:
    for line in f.readlines():
        data = json.loads(line)
        if len(data['likevideo']) > 30 and len(data["likevideo"]) < 60:
            SponorUsers.append(data['likevideo'])
            # to make the graph more beautiful ,we need the users who collect plenty of animes
        if len(SponorUsers) > 50:
            break
GroupNum = 5
# like k-means we choose 5 users as the initial cluster center
random.shuffle(SponorUsers)
groups = []
for i in range(GroupNum):
    groups.append({"center": i, "members":[i]})
turns  = 400
centers = []# record the centers 
# iterate the centers and untill the centers are stable or it went through 400 cycles
while True :
    tmpCenters = []
    turns -= 1
    for i in range(len(SponorUsers)):
        IsCenter = False
		# if it is the center, continue
        for group in groups:
            if i == group["center"]:
                IsCenter = True
                break
        if IsCenter:
            continue
        value = []
		# check every user and let it enter a specific group
        for j in range(GroupNum):
            v = evaluate(SponorUsers[i], SponorUsers[groups[j]["center"]])
            value.append(v)
        minpos = value.index(min(value))
        groups[minpos]["members"].append(i)
    # refresh the center:
    print("______turn"+str(turns)+"________")
	# refresh the center
    for i in range(GroupNum):
        groups[i]["center"] = CenterCheck(groups[i])
        tmpCenters.append(groups[i]["center"])
        # clean the group
        if(turns > 0):
            groups[i]["members"] = [groups[i]["center"]]
            print(i, groups[i]["members"])
	# quit if centers are stable or it went through 400 cycles
    if(len(set(centers)^set(tmpCenters)) == 1 or turns <= 0):
        break;
    else:
        centers = tmpCenters
        
linksCheck = []
for i in range(GroupNum):
    for j in range(len(groups[i]["members"])):
        Data["nodes"].append({"id":str(groups[i]["members"][j]), "group":i})
# the part of the group is all right
for i in range(len(SponorUsers)):
    for j in range(len(SponorUsers)):
		# don't compare yourself to yourself
        if i == j:
            continue
        else:
            dis = evaluate(SponorUsers[i], SponorUsers[j])
            linksCheck.append(dis)
			# the same group must have link
            if TheSameGroup(i,j) or dis < 5:
                Data["links"].append({"source": str(i), "target": str(j), "value": dis})

fp = open('study.json', 'w')
#dump the result to json file
print(len(Data["links"]))
json.dump(Data, fp, indent=4)