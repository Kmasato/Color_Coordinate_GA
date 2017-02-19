def hue_eval(hue1, hue2):
        dhue = abs(hue1-hue2)*1.0/1.8
        score = 0

        if dhue < 1:
            score = score + 1
        elif 1 <= dhue and dhue < 7:
            score = 0
        elif 7 <= dhue and dhue < 12:
            score = 0.8
        elif 12 <= dhue and dhue < 16:
            score = 0.2
        elif 16 <= dhue and dhue < 24:
            score = 0
        elif 24 <= dhue and dhue < 28:
            score = 0.2
        elif 28 <= dhue and dhue < 33:
            score = 0.65
        elif 33 <= dhue and dhue < 39:
            score = 0.85
        elif 39 <= dhue and dhue <= 45:
            score = 0.65
        elif 45 <= dhue and dhue <= 50:
            score = 0.85

        return score

def sat_val_eval(sat1,sat2,val1,val2):
        dsat = abs(sat1-sat2)*1.0/85
        dval = abs(val1-val2)*1.0/32

        score = 0

        if 0<= dsat and dsat < 0.5:
            if 0<= dval and dval <0.5:
                score = 0.9
            elif 0.5<= dval and dval < 2:
                score =  0
            elif 2 <= dval and dval <3:
                score =  0.3
            elif 3 <= dval and dval < 3.5:
                score = 0.7
            elif 3.5 <= dval and dval < 4.5:
                score = 1.0
            elif 4.5 <= dval and dval < 5:
                score = 0.7
            elif 5 <= dval and dval < 7:
                score = 0
            elif 7 <= dval and dval <= 8:
                score = 0.8


        elif 0.5 <= dsat and dsat < 1.0:
            if 0 < dval and dval < 2:
                score = 0.8
            elif 2 <= dval and dval < 4:
                score = 1.0
            elif 4 <= dval and dval < 5:
                score = 0.5
            elif 5 <= dval and dval < 6:
                score = 0
            elif 6 <= dval and dval < 7:
                score = 0.2
            elif 7 <= dval and dval < 8:
                score = 0.8

        elif 1 <= dsat and dsat < 1.5: 
            if 0 < dval and dval < 1:
                score = 0.8
            elif 1 <= dval and dval < 2:
                score = 0.65
            elif 2 <= dval and dval < 3:
                score = 0.4
            elif 3 <= dval and dval < 4:
                score = 0.2
            elif 4 <= dval and dval < 6:
                score = 0
            elif 6 <= dval and dval < 8:
                score = 1.0

        elif 1.5 <= dsat and dsat < 2.0: 
            if 0 < dval and dval < 4:
                score = 0
            elif 4 <= dval and dval < 5:
                score = 0.2
            elif 5 <= dval and dval < 6:
                score = 0.8
            elif 6 <= dval and dval < 8:
                score = 1.0

        elif 2.0 <= dsat and dsat < 2.5: 
            if 0 < dval and dval < 2:
                score = 0.0
            elif 2 <= dval and dval < 3:
                score = 0.3
            elif 3 <= dval and dval < 4:
                score = 0.65
            elif 4 <= dval and dval < 5:
                score = 0.85
            elif 5 <= dval and dval < 8:
                score = 1.0

        elif 2.5 <= dsat and dsat <= 3:
            if 0 < dval and dval < 3:
                score = 0.85
            elif 3 <= dval and dval < 8:
                score = 1.0
        
        return score

def judge(child):
    score_list = list()
    for i in range(30):
        score_list.append(child[i].score)
    
    max_score = max(score_list)
    
    if max_score >= 3.65:
        return True
    else:
        return False
