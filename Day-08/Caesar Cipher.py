def calculate_love_score(name1,name2):
    count1 = 0
    count2 = 0
    for i in name1.lower():
        if i in "true":
            count1 +=1
        if i in "love":
            count2 +=1 
    for i in name2.lower():
        if i in "true":
            count1 +=1 
        if i in "love":
            count2 +=1
    print(str(count1)+str(count2))

calculate_love_score(name1="angela yu",name2="jack bauer")
