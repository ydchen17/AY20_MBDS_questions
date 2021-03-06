def path_min_value(nrow_total, ncol_total):
    rightward_min = 1*(ncol_total-1)
    downward = nrow_total*(nrow_total-1)/2
    return rightward_min + downward + nrow_total


def pathfinding(nrow_total, ncol_total, value):
    delta = value - path_min_value(nrow_total, ncol_total)
    i = n = nrow_total - 1  # number of large and small rods
    path = ""
    while 1 <= i <= nrow_total - 1:
        path = "R"*int((delta//i))+path
        path = "D"+path
        n -= delta//i
        delta = delta % i
        i -= 1
    path = "R"*int(n)+path
    output_formatted = str(value)+" "+path+"\n"
    return output_formatted


output = open(
    '/Users/ydchen/Desktop/NTU-interview-questions/AY20_MBDS_questions/Question 1/output_question_1', 'a')
output.write(pathfinding(9, 9, 65))
output.write(pathfinding(9, 9, 72))
output.close()
