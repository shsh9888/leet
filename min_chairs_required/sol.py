
def min_chairs(S, E):
    if len(S) is 0 or len(E) is 0:
        return 0
    ##the maximum timestamp where a person leaves
    max_time = max(E)

    arrives = {}

    ##stores  how many chairs neeeded at each timestamp. index is the timestamp here
    time_array = [0]*(max_time+1)

    ##Filling the leave time stamps (-1s) at each point where person leaves
    for time in E:
        time_array[time]  = time_array[time] -1

    ##Arrival count dictionary
    for arrival_time in S:
        if arrival_time in arrives:
            arrives[arrival_time] += 1
        else:
            arrives[arrival_time] = 1


    ## Go through each time stamp and see if someone is arriving at that point. lev
    for index,time in enumerate(time_array):
        if index is 0:
            continue

        number_ppl_arriving = 0
        if index in arrives:
            number_ppl_arriving = arrives[index]
        # print(number_ppl_arriving)
        time_array[index]  = time_array[index-1] + time_array[index] + number_ppl_arriving

    # print(time_array)
    return max(time_array)


print(min_chairs([1,2,6,5,3],[5,5,7,6,8]),3) ##randome
print(min_chairs([1,2,6,5,3],[8,8,8,8,8]),5) ##everyone leaves late
print(min_chairs([1,2,6,5,3],[1,2,6,5,3]),0) ##  same time as arrive
print(min_chairs([1,2,6,5,3],[1,3,6,5,3]),1) ##  2nd person waits for one time stamp
print(min_chairs([],[]),0) ##  2nd person waits for one time


print(min_chairs([1,2,6,5,3],[2,3,7,6,4]),1) ##  leave at the next time stamp