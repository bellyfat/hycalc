def get_rise(btuh, eff, gph):
    rise_output = (btuh*eff)/(gph*8.33)
    print('Total Rise is: ' + str(rise_output) + 'F')