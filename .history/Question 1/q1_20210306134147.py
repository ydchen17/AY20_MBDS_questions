def pathfinding (nrow_total, ncol_total, value):
    delta = value - path_min_value (nrow_total, ncol_total)
    i = n = nrow_total - 1 # number of large and small rods
    path=""
    while 1<=i<=nrow_total - 1:
        path="R"*int((delta//i))+path
        path="D"+path
        n-=delta//i
        delta = delta % i
        i-=1
    path="R"*int(n)+path
    output_formatted= str(value)+" "+path+"\n"
    return output_formatted


output = open('../output_question_1', 'a')
output.write(pathfinding(9, 9, 65)+"\n")
output.write(pathfinding(9, 9, 72))
output.close()

