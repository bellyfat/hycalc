def get_linesize(gpm):

    import math

    #Initialize the output array
    linesize_output = []

    #Setting the ranges for each size
    range050 = [0, 3]
    range075 = [0, 9]
    range100 = [3, 10]
    range125 = [7, 17]
    range150 = [10, 26]
    range200 = [20, 50]
    range250 = [30, 80]
    range300 = [60, 150]
    range400 = [120, 300]
    range500 = [220, 550]
    range600 = [350, 800]
    range800 = [700, 1800]
    range1000 = [1000, 2700]
    range1200 = [2000, 3800]


    #Compare input gpm for known ranges for sizes 0.5" to 12", and if matching, add that size to the output array
    if gpm <= range050[1]:
        linesize_output.append(0.5)
    if gpm <= range075[1]:
        linesize_output.append(0.75)
    if range100[0] <= gpm <= range100[1]:
        linesize_output.append(1.0)
    if range125[0] <= gpm <= range125[1]:
        linesize_output.append(1.25)
    if range150[0] <= gpm <= range150[1]:
        linesize_output.append(1.5)
    if range200[0] <= gpm <= range200[1]:
        linesize_output.append(2.0)
    if range250[0] <= gpm <= range250[1]:
        linesize_output.append(2.5)
    if range300[0] <= gpm <= range300[1]:
        linesize_output.append(3.0)
    if range400[0] <= gpm <= range400[1]:
        linesize_output.append(4.0)
    if range500[0] <= gpm <= range500[1]:
        linesize_output.append(5.0)
    if range600[0] <= gpm <= range600[1]:
        linesize_output.append(6.0)
    if range800[0] <= gpm <= range800[1]:
        linesize_output.append(8.0)
    if range1000[0] <= gpm <= range1000[1]:
        linesize_output.append(10.0)
    if range1200[0] <= gpm <= range1200[1]:
        linesize_output.append(12.0)

    #For sizes above 12", we will calculate the velocity and add sizes that are below the set maximum velocity
    if gpm > range1200[1]:

        max_v = 13     #The maximum allowable velocity in ft/s

        d = math.sqrt((0.4084*gpm)/max_v)
        d = math.ceil(d)    #Round up to a whole number

        if d % 2 != 0 and d != 0:   #We check if d is an odd number and if so, add one to get a valid pipe size
            d = d + 1

        linesize_output.append(d)

    #Print the valid output sizes
    print('Valid line sizes for ' + str(gpm) + ' gpm are:\n')

    for size in linesize_output:
        print(str(size) + '"')
    