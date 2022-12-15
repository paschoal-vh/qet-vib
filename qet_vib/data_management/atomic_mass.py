def atomic_mass(element):

    """
    Compilation of common elements and their most abundant/stable isotopes. 
    """
    atomic_species={'H'  : [1,1.00782503223],
                    'D'  : [2,2.01410177812],
                    'T'  : [3,3.01604927790],
                    'He' : [4,4.00260325413],
                    'Li' : [7,7.01600343660],
                    'Be' : [9,9.01218306500],
                    'B'  : [11,11.00930536],
                    'C'  : [12,12.00000000],
                    'N'  : [14,14.003074004],
                    'O'  : [16,15.99491461957],
                    'F'  : [19,18.99840316273],
                    'Ne' : [20,19.9924401762],
                    'Na' : [23,22.9897692820],
                    'Mg' : [24,23.985041697],
                    'Al' : [27,26.98153853],
                    'Si' : [28,27.97692653465],
                    'P'  : [31,30.97376199842],
                    'S'  : [32,31.9720711744],
                    'Cl' : [35,34.968852682],
                    'Ar' : [40,39.9623831237],
                    'K'  : [39,38.9637064864],
                    'Ca' : [40,39.962590863],
                    'Sc' : [45,44.95590828],
                    'Ti' : [48,47.94794198],
                    'V'  : [51,50.94395704],
                    'Cr' : [52,51.94050623],
                    'Mn' : [55,54.93804391],
                    'Fe' : [56,55.93493633],
                    'Co' : [59,58.93319429],
                    'Ni' : [58,57.93534241],
                    'Cu' : [63,62.92959772],
                    'Zn' : [64,63.92914201],
                    'Ga' : [69,68.9255735],
                    'Ge' : [74,73.921177761],
                    'As' : [75,74.921594570],
                    'Se' : [80,79.9165218],
                    'Br' : [79,79.9040000],
                    'Kr' : [84,83.9114977282],
                    'Rb' : [85,84.9117897379],
                    'Sr' : [88,87.9056125],
                    'Y'  : [89,88.9058403],
                    'Zr' : [90,89.9046977],
                    'Nb' : [93,92.9063730],
                    'Mo' : [98,97.90540482],
                    'Ru' : [102,101.9043441],
                    'Rh' : [103,102.9054980],
                    'Ag' : [107,107.8682],
                    'In' : [115,114.903878776],
                    'Sn' : [120,119.90220163],
                    'Sb' : [121,120.9038120],
                    'I'  : [127,126.9044719],
                    'Cs' : [133,132.9054519610],
                    'Ba' : [138,137.90524700],
                    'Au' : [197,196.96656879],
                    'Pb' : [208,207.9766525] }
    mass=atomic_species[element][1]
    return(mass)
