"""
qet_vib.py
QET-Vib: A Quantum Espresso Toolbox for Vibrational Spectroscopy

Handles the primary functions
"""

import sys, argparse, numpy
from data_management import atomic_mass, extract, pwin
from eigenvector_tools import fdv
from raman_tools import raman_gen, raman_calc
#from born_tools import born_gen, born_calc


def main():
   global_parser = argparse.ArgumentParser(description='QET-Vib: A Quantum Espresso Toolbox for Vibrational Spectroscopy')
   subparsers=global_parser.add_subparsers(title="Subroutines")
   extract_parser=subparsers.add_parser('--extract', help='Call extraction module for q=(0 0 0) eigenvectors.'\
                                        'Arguments are filename with the eigenvectors (defaults '\
                                        'to eigen.out). The output directory (defaults to '\
                                        './test_output) And ph.x output (defaults to ph.out)'\
                                        'e.g.: --extract eigen.out test_output ph.out')
   extract_parser.add_argument(dest='extract',nargs='*',action='append')
   extract_parser.set_defaults(func=extract)
   fdv_parser=subparsers.add_parser('--fdv', help='Calculate mode participation of translations, '\
                                    'librations and intramolecular motions. Needs as '\
                                    'argument the mode number, the  system field from pw.x,'\
                                    'read from pw.in (default) and the output directory '\
                                    'used with --extract. '\
                                    'e.g.: --fdv 1 test_output --pwin pw.in')
   fdv_parser.add_argument(dest='fdv',nargs='*',action='append')
   fdv_parser.set_defaults(func=fdv)
   pwin_parser=subparsers.add_parser('--pwin',help='Name of the pw.x input file used in for the ph.x '\
                                     'calculations, defaults to pw.in')
   pwin_parser.add_argument(dest='pwin',nargs='*', action='append')
   pwin_parser.set_defaults(func=fdv)
   ramangen_parser=subparsers.add_parser('--raman_gen',help='Generate Raman inputs for calculations with DFPT+'\
                        'Finite difference approach. Expects as arguments mode'\
                        'number, the directory from --extract, other parameters'\
                        'from --pwin and a normalization factor for the amount of'\
                        'deformation done to the reference structure in the'\
                        'direction of the eigenvector.'\
                        'e.g.: --raman_gen 1 0.1 --pwin pw.in')
   ramangen_parser.add_argument(dest='ramangen',nargs='*',action='append')
   ramangen_parser.set_defaults(func=raman_gen)
   ramancalc_parser=subparsers.add_parser('--raman_calc',help='Calculate Raman intensities from DFPT+finite '\
                                                                     'difference method. Takes as arguments mode number and'\
                                                                     'the name of the ph.x output (which defaults to ph.out)'\
                                                                     'e.g.: --raman_calc 1 ph.out')
   ramancalc_parser.add_argument(dest='ramancalc',nargs='*',action='append')
   ramancalc_parser.set_defaults(func=raman_calc)
   args=global_parser.parse_args()
#    parser.add_argument('--born_gen',action='append'
#                        help='Generate Born charge tensor and dielectric constant'\
#                        'inputs for calculations with the finite difference method.')


if __name__ == "__main__":
    main()
