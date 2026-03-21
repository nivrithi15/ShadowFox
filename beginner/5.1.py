import random
total_rolls=20
roll_list=[]

ones=0
sixes=0
two_sixes=0
prev_roll=0

for i in range(total_rolls):
    roll=random.randint(1,6)
    roll_list.append(roll)
    if roll==1:
        ones+=1
    elif roll==6:
        sixes+=1
        if prev_roll==6:
            two_sixes+=1
    prev_roll=roll
print("Rolls:",roll_list)
print("Number of ones:",ones)
print("Number of sixes:",sixes)
print("Number of times two sixes in a row:",two_sixes)

    
