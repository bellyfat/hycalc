def get_btuh_in(gph, deltat, eff):
    btuh_in = (gph*8.33*deltat)/eff
    print('Total BTU/h Input is: ' + str(btuh_in))