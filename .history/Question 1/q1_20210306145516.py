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


output = open('Question 1/output_question_q3', 'a')
output.write(pathfinding(90000, 1000000, 87127231192))
output.close()

