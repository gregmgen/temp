import unittest

d = ["1,10000,40", "1,10002,45", "1,11015,50", "2,10005,42", "2,11051,45", "2,12064,42", "2,13161,42"]


def average_temp(interval, data):
    time = map(lambda s: int(s.split(',')[1]), data)
    temp = map(lambda s: int(s.split(',')[2]), data)
    time, temp = zip(*sorted(zip(time, temp)))
    blocks = []
    temp_blocks = []
    cur_block = 0
    cur_base_time = time[0];
    blocks.append([])
    temp_blocks.append([])
    blocks[0].append(time[0])
    temp_blocks[0].append(temp[0])
    i = 1
    while i < len(time):
        if time[i] >= cur_base_time + (interval - 1):
            while time[i] > cur_base_time + interval * 2:
                blocks.append([])
                temp_blocks.append([])
                cur_base_time += interval
                cur_block += 1
            blocks.append([])
            temp_blocks.append([])
            cur_base_time += interval
            cur_block += 1
        blocks[cur_block].append(time[i])
        temp_blocks[cur_block].append(temp[i])
        i += 1

    brackets = []
    avg = []

    j = 0
    start = blocks[0][0]
    while j < len(blocks):
        brackets.append(str(start + interval * j) + " - " + str(start + (interval * (j + 1)) - 1))
        j += 1

    for b in temp_blocks:
        total = 0
        for n in b:
            total += n
        if len(b) == 0:
            avg.append(0)
        else:
            avg.append(total / len(b))

    k = 0
    while k < len(brackets):
        t = "N/A" if avg[k] == 0 else "{0:.2f}".format(avg[k])
        print(brackets[k] + ": " + t)
        k += 1


average_temp(1000, d)
