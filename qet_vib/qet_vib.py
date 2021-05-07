"""
qet_vib.py
QET-Vib: A Quantum Espresso Toolbox for Vibrational Spectroscopy

Handles the primary functions
"""

import sys, argparse, numpy
from .data_management import atomic_mass, extract
from .eigenvector_tools import fdv
from .raman_tools import raman_gen, raman_calc
from .born_tools import born_gen, born_calc

def main():
    parser = argparse.ArgumentParser(
        description='QET-Vib: A Quantum Espresso Toolbox for Vibrational Spectroscopy')

    parser.add_argument('--extract', description='Call extraction module for q=(0 0 0) eigenvectors')
    parser.add_argument('--fdv', description='Calculate mode participation share of translations, librations and intramolecular motions')
    parser.add_argument('--raman_gen', description='Generate Raman inputs for calculations with the finite difference method')
    parser.add_argument('--raman_calc', description='Calculate Raman intensities for calculations with the finite difference method')
    parser.add_argument('--born_gen', description='Generate Born charge tensor and dielectric constant imputs for calculations with the finite difference method')

    

    args=parser.parse_args()
    

if __name__ == "__main__":
    main()
