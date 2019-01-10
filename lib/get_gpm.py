def get_gpm(btuh, deltat):
    gpm_output = btuh/(500*deltat)
    print('Total Gallons/Min is: ' + str(gpm_output))