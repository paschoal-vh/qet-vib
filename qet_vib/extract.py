def extract(filename='eigen.out',output_dir):
    import numpy as np
    from os import mkdir, getcwd, path
    """"
    This function will create XCrysDen files, with the xsf extension and writes them 
    to a directory provided by the user. This function should be called in the folder 
    containing the outputs of pw.x and ph.x.
    Aside from the extracted files, this function will generate a numpy array (primvec) 
    with the lattice vectors and three dictionaries: control, system and atomic_species.
    
    control has the following information:
    
    -calculation type, prefix type, pseudo pontential directory and output directory
    
    system has the following information:
    
    -number of atoms, number of types, kinetic-energy cutoff, charge density cutoff, convergence threshold,
    mixing beta, number of iterations used, mixing mode
    
    atomic_species has the following information:
    
    -element type, mass, pseudo potential file name
    
    """
    
    # define some constants
    local=getcwd()
    bohr2angstron=0.529177
    
    # create local directory for extracted eigenmodes
    mkdir(local+"\\"+str(output_dir))
    filename=str(filename) #"default" file name, eigen.out
    
    #begin file reading
    data=[]
    p1="q =       0.0000      0.0000      0.0000"
    prop1=re.compile(p1)
    p2="**************************************************************************"
    prop2=re.compile(p2)
    i=0
    separator_place=[]
    with open(filename,'r') as file:
        for line in file:
            i+=1
            data.append(line.split('\n'))
            for match in re.finditer(prop1,line):
                q0_place=i
            for match in re.finditer(prop2,line):
                separator_place.append(i)
    
    gamma_eigen_begin=separator_place[separator_place.index(q0_place+1)]
    gamma_eigen_end=separator_place[gamma_eigen_begin+1]
    
    
    with open(filename) as f:
        for line in f:
            data.append(line.split())
    n_conf=np.int(data[0][1])
    primvec=np.array([[np.float(data[3][0]),np.float(data[3][1]),np.float(data[3][2])],
                      [np.float(data[4][0]),np.float(data[4][1]),np.float(data[4][2])],
                      [np.float(data[5][0]),np.float(data[5][1]),np.float(data[5][2])]])
    n_particles=np.int(data[7][0])
    ii=6
    filelocation=local+'\\'+str(output_dir)
    for conf_n in range(n_conf):
        file=open(filelocation+'\conf_'+str(conf_n+1)+'.xsf','w')
        file.write('CRYSTAL\n')
        file.write('PRIMVEC\n')
        file.write('    ''%.9f' '    ' '%.9f' '    ' '%.9f''\n' % (primvec[0][0],primvec[0][1],primvec[0][2]))
        file.write('    ''%.9f' '    ' '%.9f' '    ' '%.9f''\n' % (primvec[1][0],primvec[1][1],primvec[1][2]))
        file.write('    ''%.9f' '    ' '%.9f' '    ' '%.9f''\n' % (primvec[2][0],primvec[2][1],primvec[2][2]))
        file.write('PRIMCOORD'' ''%d''\n' % (conf_n+1))
        file.write('    ''%d''    ''1''\n' % n_particles)
        for jj in range(ii+2,ii+n_particles+2,1):
            file.write(str(data[jj]).strip('[]').replace('\'','').replace(',','')+'\n')
        file.close()
        ii=ii+2+n_particles
        
    return(control, system, atomic species, primvec)
