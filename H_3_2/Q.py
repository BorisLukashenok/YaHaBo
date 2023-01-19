string = input()
friendship = dict()

while string != '': 
    secondname = string.split(' ')
    if secondname[0] not in friendship.keys():
        friendship[secondname[0]] = {secondname[1]}
    else:
        friendship[secondname[0]].add(secondname[1])
    if secondname[1] not in friendship.keys():
        friendship[secondname[1]] = {secondname[0]}
    else:
        friendship[secondname[1]].add(secondname[0])
    string = input()

friend_result = {key: set() for key in friendship.keys()}
for i in friendship.keys():
    for j in friendship[i]:
        temp = friendship[j].copy()
        temp.discard(i)
        temp.difference_update(friendship[i])
        friend_result[i] = friend_result[i].union(temp)
        
sort_res = sorted(friend_result.items(), key=lambda secondname: secondname[0])
for i in sort_res:
    print(f"{i[0]}: {', '.join(sorted(i[1]))}")