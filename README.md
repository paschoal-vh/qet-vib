QET-Vib
==============================
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/paschoal-vh/qet_vib/workflows/CI/badge.svg)](https://github.com/paschoal-vh/qet_vib/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/paschoal-vh/QET-Vib/branch/master/graph/badge.svg)](https://codecov.io/gh/paschoal-vh/QET-Vib/branch/master)


QET-Vib: A Quantum Espresso Toolbox for Vibrational Spectroscopy

This repository is under development! Currently available functionalities are

Full arrows link functionalities available (Figure 1).


<img src="https://github.com/paschoal-vh/qet-vib/blob/main/docs/simplified_workflow.png" width="50%"></img> 
=======

The scripts called by QET-Vib_main.py are meant to generate visualization of vibrational modes, inputs and Raman intensities.  The module extract.py, vibrational eigenmodes (Q) obtained from dynmat.x output transforming them to XCrysDen file format. From the extracted eigenmodes coordinates raman_gen.py generates a series of pw.x and ph.x inputs to calculate the dielectric tensors from structures deformed along +Q and -Q. After the calculations, raman_calc.py assembles the dielectric tensors from ph.x calculations and outputs the intensities obtained within the far-from resonance approximation,[1] assuming backsttering geometry.

Reference:

1-Skelton, et al., Lattice dynamics of the tin sulphides SnS2, SnS and Sn2S3: vibrational spectra and thermal transport. Phys. Chem. Chem. Phys., 2017, 19, 12452-12465. DOI: 10.1039/C7CP01680H. And references within. 

### Copyright

Copyright (c) 2021, Vitor Paschoal


#### Acknowledgements
 
Project based on the [Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.5.

Project developed with the support of FAPESP grant 2019/00207-0
