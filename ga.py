import random
import numpy as np

def cross(p1, p2):

    c1 = list()
    c2 = list()

    p = random.randint(0,100)
    mut = random.randint(0,10)

    sp1 = random.randint(0,9)
    sp2 = random.randint(0,9)

    if p < 20:
        c1 = p1
        c2 = p2
        
        if mut == 5:
            which = random.randint(0,2)
            num = random.randint(1,6)
            for i in range(num):
                if which == 1:
                    c1 = mutation(c1)
                else:
                    c2 = mutation(c2)





    else:

        if sp1 > sp2:
            swap = sp1
            sp1 = sp2
            sp2 = swap

        #print(sp1)
        #print(sp2)

        for i in range(sp1):
            c1.append(p1[i])
            c2.append(p2[i])
        for i in range(sp1,sp2):
            c1.append(p2[i])
            c2.append(p1[i])
        for i in range(sp2,9):
            c1.append(p1[i])
            c2.append(p2[i])

        if mut == 5:
            which = random.randint(0,2)
            num = random.randint(1,6)
            for i in range(num):
                if which == 1:
                    c1 = mutation(c1)
                else:
                    c2 = mutation(c2)


       

    #print c1
    #print c2
    return c1,c2


def mutation(c):
    element = random.randint(0,8)
    #print("mutation!!:",element)
    if element == 2 or element == 5 or element == 8:
        mut = random.randint(0,100)-50
        if c[element] + mut > 180:
            c[element] = c[element] + mut - 180
        elif c[element] + mut < 0:
            c[element] = c[element] + mut + 180
    else:
        mut = random.randint(0,200)-10
        if c[element] + mut > 255:
            c[element] = c[element] + mut - 255
        elif c[element] + mut < 0:
            c[element] = c[element] + mut + 255

    #print("mutation:",element, c[element])
    return c





def roulette_chose(chara):
    score_sum = 0
    for i in range(30):
        score_sum = score_sum + chara[i].score

    for i in range(30):
        chara[i].p = chara[i].score*1.0/score_sum * 100

    temp = random.randint(0,100)
    for i in range (30):
        temp = temp - chara[i].p
        if temp <= 0:
            return (chara[i])

    return chara[30]

def elite_chose(chara):
    score_list = list()
    for i in range(30):
        score_list.append(chara[i].score)

    elite = np.array(score_list)
    b = np.where(elite == elite.max())
    elite_num = random.choice(b[0])


    S = np.array(score_list)
    return elite_num, S.argsort()[2]


