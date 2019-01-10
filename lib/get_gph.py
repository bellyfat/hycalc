def get_gph(btuh, eff, deltat):
    gph_output = (btuh*eff)/(deltat*8.33)
    print('Total Gallons/Hour is: ' + str(gph_output))