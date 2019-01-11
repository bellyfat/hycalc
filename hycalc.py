ver=0.1

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
from lib.get_linesize import *


#Main function. Parse inputs from command line and call the appropriate function.
def main():

    parser = argparse.ArgumentParser(description='A simple hydronics calculator. Specify the function, and the required inputs')

    #The outputs 
    parser.add_argument('--get-btuh', help='BTUs per hour (GPM, ΔT)', action='store_true')
    parser.add_argument('--get-btuh-out', help='BTUs per hour output (GPH, ΔT)', action='store_true')
    parser.add_argument('--get-btuh-in', help='BTUs per hour input (GPH, ΔT)', action='store_true')
    parser.add_argument('--get-deltat', help='Change in temperature (Btu/h, GPM, Efficiency)', action='store_true')
    parser.add_argument('--get-gph', help='gallons per hour (Btu/h, Efficiency, ΔT)', action='store_true')
    parser.add_argument('--get-gpm', help='gallons per minute (Btu/h, ΔT)', action='store_true')
    parser.add_argument('--get-rise', help='Temperature rise (Btu/h, GPH, ΔT)', action='store_true')
    parser.add_argument('--get-linesize', help='Optimal pipe size (GPM)', action='store_true')
    parser.add_argument('-v', '--version', help='Get version information', action='store_true')

    #The optional inputs
    parser.add_argument('-b', '--btuh', help='BTUs per hour', type=float)
    parser.add_argument('-t','--deltat', help='ΔT', type=float)
    parser.add_argument('-g','--gpm', help='Gallons per minute', type=float)
    parser.add_argument('--gph', help='Gallons per hour', type=float)
    parser.add_argument('-e','--eff', help='Efficiency (decimal <= 1.0)', type=float)
    
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
    if args.get_linesize:
        get_linesize(args.gpm)
    
    if args.version:
        print('\n-----hycalc release ' + str(ver) + '-----')
        print('-----By Kamin Horvath-----\n')
        print('Released under the GNU General Public License 3.0\n')


#Run the main function
if __name__== "__main__":
    main()