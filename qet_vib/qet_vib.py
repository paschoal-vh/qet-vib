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
    parser = argparse.ArgumentParser(
        description='QET-Vib: '\
        'A Quantum Espresso Toolbox for Vibrational Spectroscopy')

    parser.add_argument('--extract',action='append',
                        help='Call extraction module for q=(0 0 0) eigenvectors.'\
                        'Arguments are filename with the eigenvectors (defaults '\
                        'to eigen.out). The output directory (defaults to '\
                        './test_output) And ph.x output (defaults to ph.out)'\
                        'e.g.: --extract eigen.out;test_output;ph.out')
    parser.add_argument('--fdv',action='append',
                        help='Calculate mode participation of translations, '\
                        'librations and intramolecular motions. Needs as '\
                        'argument the mode number, the  system field from pw.x,'\
                        'read from pw.in (default) and the output directory '\
                        'used with --extract. '\
                        'e.g. --fdv 1;test_output --pwin pw.in')
    parser.add_argument('--pwin', action='pw.in',
                        help='Name of the pw.x input file used in for the ph.x '\
                        'calculations, defaults to pw.in')
    parser.add_argument('--raman_gen',action='append',
                        help='Generate Raman inputs for calculations with DFPT+'\
                        'Finite difference approach. Expects as arguments mode'\
                        'number, the directory from --extract, other parameters'\
                        'from --pwin and a normalization factor for the amount of'\
                        'deformation done to the reference structure in the'\
                        'direction of the eigenvector.'\
                        'e.g. --raman_gen 1;0.1 --pwin pw.in')
    parser.add_argument('--raman_calc',action='append',
                        help='Calculate Raman intensities from DFPT+finite '\
                        'difference method. Takes as arguments mode number and'\
                        'the name of the ph.x output (which defaults to ph.out)'\
                        'e.g. --raman_calc 1;ph.out')
#    parser.add_argument('--born_gen',action='append',
#                        help='Generate Born charge tensor and dielectric constant'\
#                        'inputs for calculations with the finite difference method.')
    args=parser.parse_args()


if __name__ == "__main__":
    main()
