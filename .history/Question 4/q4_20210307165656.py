import pandas as pd
import numpy as np

# Remove auto-assigned col names
raw_image = pd.read_table("input_question_4", header=None)
nrow_total, ncol_total = raw_image.shape
print(raw_image)

# pixel value in pd


def pixel_value(x, y, pd):
    # return an array with (coord, value)
    return [tuple([x, y]), pd[y][x]]


pixel_set = []
for y in range(ncol_total):
    for x in range(nrow_total):
        if pixel_value(x, y, raw_image)[1] == 1:
            pixel_set += tuple([(x, y)])


i = 0
adjacency_set = []
while i < len(pixel_set):
    xy = pixel_set[i]
    x = xy[0]
    y = xy[1]
    adjacency_set_unconfirmed = [
        (x, y), (x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    adjacency_set_confirmed = []
    for pixel in adjacency_set_unconfirmed:
        if pixel in pixel_set:
            adjacency_set_confirmed.append(pixel)
    adjacency_set.append(adjacency_set_confirmed)
    i += 1
print(len(pixel_set), len(adjacency_set))


# all we need to do is to simplify the set to make sure all connected points are in the same set.
points_unvisited = pixel_set  # We make a list for all points
adjacency_set_untrimed = adjacency_set
adjacency_set_trimed = []
print(len(points_unvisited), len(
    adjacency_set_untrimed), len(adjacency_set_trimed))

for point in points_unvisited:
    # for each point, we want their adj_points to be removed and added to a new trimed adj_set
    adj_merged = set()
    for adj_set in adjacency_set_untrimed:  # we screen all adj_sets
        if point in adj_set:                # find the matched adj_set
            print(point, adj_set)
            for adj_point in adj_set:       # remove all adj_points
                print(adj_point)
                if adj_point in points_unvisited:
                    points_unvisited.remove(adj_point)
                # add each adj_point to new adj_points set
                adj_merged.add(adj_point)
        adjacency_set_untrimed.remove(adj_set)  # removed the trimed adj_set

    # for each point, we have a full list of adjacency_set_trimed until it finish emmuration
    adjacency_set_trimed.append(adj_merged)

    print(len(points_unvisited), len(
        adjacency_set_untrimed), len(adjacency_set_trimed))
