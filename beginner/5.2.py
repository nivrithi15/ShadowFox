total=0
target=100
set=10

for i in range(0,target,set):
    print("Current total:",total)
    total+=set
    if total>=target:
        print("Congratulations!YOU HAVE REACHED THE TARGET!")
        break
    tired=input("Are you tired? (yes/no): ")
    if tired.lower()=="yes" or tired.lower()=="y":
        skip=input("Do you want to skip the rest of the sets? (yes/no): ")
        if skip.lower()=="yes" or skip.lower()=="y":
            print("Stopped the sets. Final total:",total)
            break


   
        
    