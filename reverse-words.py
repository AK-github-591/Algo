message=[ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

len=len(message)
l=[[] for _ in range(message.count(' ')+1)]
print(l)
temp=0
for i in range(0,len):

    if message[i] != ' ':
        l[temp].append(message[i])
    else:
        temp+=1


print("  ".join([' '.join(ele) for ele in l[::-1]]))