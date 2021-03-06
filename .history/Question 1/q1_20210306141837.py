f = open('Question 1/test_output', 'r')
lines = f.read()
f.close()


def path2sum(path):
    index = 1
    finalsum = 0
    for i in str(path):
        if i == "R":
            finalsum += index
        else:
            finalsum += index
            index += 1
    return finalsum+index


print(path2sum(lines))
