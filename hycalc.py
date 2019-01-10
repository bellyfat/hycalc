#Import libraries
import sys, argparse

#Importing functions from lib
from lib.get_btuh import *
from lib.get_btuh_in import *
from lib.get_btuh_out import *
from lib.get_deltat import *
from lib.get_gph import *
from lib.get_gpm import *
from lib.get_rise import *



def main():

    parser = argparse.ArgumentParser(description='A simple hydronics calculator')

    #The outputs 
    parser.add_argument('--get-btuh', help='BTUs per hour', action='store_true')
    parser.add_argument('--get-btuh-out', help='BTUs per hour output', action='store_true')
    parser.add_argument('--get-btuh-in', help='BTUs per hour input', action='store_true')
    parser.add_argument('--get-deltat', help='Change in temperature (F)', action='store_true')
    parser.add_argument('--get-gph', help='gallons per hour (GPH)', action='store_true')
    parser.add_argument('--get-gpm', help='gallons per minute (GPM)', action='store_true')
    parser.add_argument('--get-rise', help='Temperature rise', action='store_true')

    #The optional inputs
    parser.add_argument('--btuh', type=float)
    parser.add_argument('--deltat', type=float)
    parser.add_argument('--gpm', type=float)
    parser.add_argument('--gph', type=float)
    parser.add_argument('--eff', type=float)
    
    args = parser.parse_args()
    
    #Calling a function based on the chosen output and passing along the inputs
    if args.get_btuh:
        get_btuh(args.gpm, args.deltat)
    if args.get_btuh_in:
        get_btuh_in(args.gph, args.deltat, args.eff)
    if args.get_btuh_out:
        get_btuh_out(args.gph, args.deltat)
    if args.get_deltat:
        get_deltat(args.btuh, args.gpm)
    if args.get_gph:
        get_gph(args.btuh, args.eff, args.deltat)
    if args.get_gpm:
        get_gpm(args.btuh, args.deltat)
    if args.get_rise:
        get_rise(args.btuh, args.eff, args.gph)



  
if __name__== "__main__":
    main()