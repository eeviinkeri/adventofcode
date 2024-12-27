import pandas

data = pandas.read_csv('data/input1.txt', sep='   ', header=None, engine='python')

location_id_list_left = sorted(data[0].to_list())
location_id_list_right = sorted(data[1].to_list())

list_len = len(location_id_list_left)

sum = 0
for i in range(0, list_len):
    diff = abs(location_id_list_left[i] - location_id_list_right[i])
    sum = sum + diff

print(f"Answer to part 1 is: {sum}")

similarity_score = 0
for i in range(0, list_len):
    left_num = location_id_list_left[i]
    count_in_right = location_id_list_right.count(left_num)
    similarity_score = similarity_score + left_num * count_in_right

print(f"Answer to part 2 is: {similarity_score}")
