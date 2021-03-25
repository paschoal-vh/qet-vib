# QET-Vib: A Quantum Espresso Toolbox for Vibrational Spectroscopy

#### This repository is under development!  

The scripts called by qet_vib.py are meant to generate visualization of vibrational modes, inputs and Raman intensities using the Quantum espresso packge as   engine[1]. The module extract.py, vibrational eigenmodes (Q) obtained from dynmat.x output transforming them to XCrysDen[2] file format. From the extracted   eigenmodes coordinates raman_gen.py generates a series of pw.x and ph.x inputs to calculate the dielectric tensors from structures deformed along +Q and -Q.   
After the calculations, raman_calc.py assembles the dielectric tensors from ph.x calculations and outputs the intensities obtained within the far-from resonance   approximation,[3] assuming backsttering geometry.Finally, the modes composition, assuming contributions from translational, librational and intramolecular   contributions following the method proposed by Zhang et al.[4]  
  
The current status of the toolbox is summarized in Figure 1. Full arrows link functionalities available and dashed arrow functionalities under development.  


<img src="https://github.com/paschoal-vh/qet-vib/blob/main/docs/simplified_workflow.png" width="75%"></img>   
Figure 1: Functionalities of the code under development (dashed arrows) and already implemented (full arrows).

#### Currently available functionalities are:  

- extract.py: extracts vibrational eigenmodes and converts them to XCrysDen file format (.xsf) from dynmat.x eigen file.  
- raman_gen.py: generates pw.x and ph.x files for the calculation of Raman intensities.  
- raman_calc.py: calculates the Raman intensity and the contributions of the trace and out of trace elements of the dielectric tensor.  
- fdv.py: calculates modes composition assuming contributions from translational, librational and intramolecular contributions.
  
#### References:  
  
- 1-Giannozzi, P., Andreussi, O., Brumme, T., Bunau, O., Buongiorno Nardelli, M., Calandra, M., … Baroni, S. (2017). Advanced capabilities for materials modelling with Quantum ESPRESSO. Journal of Physics: Condensed Matter, 29(46), 465901. DOI:[10.1088/1361-648X/aa8f79](https://doi.org/10.1088/1361-648X/aa8f79)  
- 2-Kokalj, A. (1999). XCrySDen—a new program for displaying crystalline structures and electron densities. Journal of Molecular Graphics and Modelling, 17(3–4), 176–179. DOI:[10.1016/S1093-3263(99)00028-5](https://doi.org/10.1016/S1093-3263(99)00028-5)  
- 3-Skelton, J. M., Burton, L. A., Jackson, A. J., Oba, F., Parker, S. C., & Walsh, A. (2017). Lattice dynamics of the tin sulphides SnS2 , SnS and Sn2S3 : vibrational spectra and thermal transport. Physical Chemistry Chemical Physics, 19(19), 12452–12465. DOI:[10.1039/C7CP01680H](https://doi.org/10.1039/C7CP01680H)  
- 4-Zhang, F., Wang, H.-W., Tominaga, K., & Hayashi, M. (2016). Mixing of intermolecular and intramolecular vibrations in optical phonon modes: terahertz spectroscopy and solid-state density functional theory. Wiley Interdisciplinary Reviews: Computational Molecular Science, 6(4), 386–409. DOI:[10.1002/wcms.1256](https://doi.org/10.1002/wcms.1256)  


#### Copyright

Copyright (c) 2021, Vitor Paschoal


#### Acknowledgements
 
Project based on the [Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.5.  

Project developed with the support of FAPESP grant 2019/00207-0  
