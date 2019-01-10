def get_deltat(btuh, gpm):
    deltat_output = btuh/(500*gpm)
    print('Total Delta T is: ' + str(deltat_output) + 'F')