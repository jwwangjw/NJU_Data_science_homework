s=input()
swap=input()
swapp=[]
i=2
while i<len(swap):
    swapp.append(swap[i:i+3])
    i+=6
for i in range(len(swapp)):
    for j in range(len(swapp)):
        choice=swapp[i]
        place=choice.split(",")
        placel=int(place[0])
        placer=int(place[1])
        if s[placel:placel+1]>s[placer:placer+1]:
            s=s[0:placel]+s[placer:placer+1]+s[placel+1:placer]+s[placel:placel+1]+s[placer+1:]
        choice=swapp[j]
        place=choice.split(",")
        placel=int(place[0])
        placer=int(place[1])
        if s[placel:placel+1]>s[placer:placer+1]:
            s=s[0:placel]+s[placer:placer+1]+s[placel+1:placer]+s[placel:placel+1]+s[placer+1:]
print(s)
