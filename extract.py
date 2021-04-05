def extract(filename='eigen.out',output_dir='test_output',phx_output='ph.out'):
    import numpy as np
    import re
    from os import mkdir, getcwd, path
    """"
    This function will create XCrysDen files, with the xsf extension and writes them 
    to a directory provided by the user. This function should be called in the folder 
    containing the outputs of dynmat.x.    
    """
    
    # define some constants
    local=getcwd()
    bohr2angstrom=0.529177
    
    # create local directory for extracted eigenmodes
    mkdir(local+"\\"+str(output_dir)) #default output_dir='test_output'
    filename=str(filename) #"default" file name= eigen.out
    
    #begin file reading
    data=[]
    p1="q =       0.0000      0.0000      0.0000"
    prop1=re.compile(p1)
    p2="[**************************************************************************]"
    prop2=re.compile(p2)
    p3="freq"
    prop3=re.compile(p3)
    i=0
    separator_place=[]
    freq_place=[]
    with open(filename,'r') as file:
        for line in file:
            i+=1
            data.append(line.split('\n'))
            for match in re.finditer(prop1,line): ##find where the gamma point frequencies are
                q0_place=i
            for match in re.finditer(prop2,line):  ##find where the separators are
                separator_place.append(i)
            for match in re.finditer(prop3,line):  ##find where the frequencies are
                freq_place.append(i)

                
    separator_place_unique=np.unique(separator_place)
    i,=np.where(separator_place_unique==q0_place+1)
    gamma_eigen_begin=separator_place_unique[i[0]]
    gamma_eigen_end=separator_place_unique[i[0]+1]  
    eigenmodes_temp=data[gamma_eigen_begin:gamma_eigen_end-1]
    freq_list=[]
    for i in range(len(freq_place)):
        freq_list.append(eigenmodes_temp.pop(freq_place[i]-1-gamma_eigen_begin-i)) ##separate frequencies from eigenmodes

    modes=[]
    for i in range(len(eigenmodes_temp)):
        modes.append(eigenmodes_temp[i][0].split())

    frequencies=[]
    
    n_conf=len(freq_list)
    for i in range(n_conf):
        frequencies.append(np.float(freq_list[i][0].rstrip().replace("("," ").replace(")"," ").split()[6]))
    ## separate the eigenmodes in their x,y,z components 

    eigenmode_x=[]
    eigenmode_y=[]
    eigenmode_z=[]
    
    for i in range(len(modes)):
        eigenmode_x.append(np.float(modes[i][1].strip())*bohr2angstrom)
        eigenmode_y.append(np.float(modes[i][3].strip())*bohr2angstrom)
        eigenmode_z.append(np.float(modes[i][5].strip())*bohr2angstrom)
    
    ##begin extracting information from phx_output
    del data, modes, p1, p2, p3, prop1, prop2, prop3, freq_list
    
    filename=str(phx_output)
    
    #begin file reading
    
    data=[]
    p1="number of atoms/cell"
    prop1=re.compile(p1)
    p2="celldm"
    prop2=re.compile(p2)
    p3="crystal axes"
    prop3=re.compile(p3)
    p4="Atoms inside the unit cell"
    prop4=re.compile(p4)
    i=0
    celldm_place=[]
    with open(filename,'r') as file:
        for line in file:
            i+=1
            data.append(line.split('\n'))
            for match in re.finditer(prop1,line): ##find where the number of atoms is
                Nat_place=i-1
            for match in re.finditer(prop2,line): ##find where the a dimension of the crystal is
                celldm_place.append(i-1)
            for match in re.finditer(prop3,line):  ##find where the cartesian crystal axes are
                crystal_dim_place=i-1
            for match in re.finditer(prop4,line):  ##find where the frequencies are
                crystal_place=i+3
    Natoms=np.int(data[Nat_place][0].split('=')[1])
    Alattice=np.float(data[celldm_place[0]][0].lstrip().split()[1])*bohr2angstrom
    
    a1=np.array([np.float(data[crystal_dim_place+1][0].lstrip().rstrip().split()[3]),
                 np.float(data[crystal_dim_place+1][0].lstrip().rstrip().split()[4]),
                 np.float(data[crystal_dim_place+1][0].lstrip().rstrip().split()[5])])
    
    a2=np.array([np.float(data[crystal_dim_place+2][0].lstrip().rstrip().split()[3]),
                 np.float(data[crystal_dim_place+2][0].lstrip().rstrip().split()[4]),
                 np.float(data[crystal_dim_place+2][0].lstrip().rstrip().split()[5])])
    
    a3=np.array([np.float(data[crystal_dim_place+3][0].lstrip().rstrip().split()[3]),
                 np.float(data[crystal_dim_place+3][0].lstrip().rstrip().split()[4]),
                 np.float(data[crystal_dim_place+3][0].lstrip().rstrip().split()[5])])
    
    Cell_volume=np.abs(np.dot(np.cross(a1,a2),a3))*Alattice**3
    primvec=np.array([a1,a2,a3])*Alattice
    
    atomlist=[]
    crystal_pos=[]
    
    for i in range(1,Natoms+1):
        atomlist.append(data[crystal_place+i][0].lstrip().split()[1])
        crystal_pos.append([np.float(data[crystal_place+i][0].lstrip().split()[7])*Alattice,
                            np.float(data[crystal_place+i][0].lstrip().split()[8])*Alattice,
                            np.float(data[crystal_place+i][0].lstrip().split()[9])*Alattice])
    
    
    filelocation=local+'\\'+str(output_dir)
    ii=0
    for conf_n in range(n_conf):
        file=open(filelocation+'\conf_'+str(conf_n+1)+'.xsf','w')
        file.write(f'freq= {frequencies[conf_n]} cell volume= {Cell_volume} \n')
        file.write(f'CRYSTAL\n')
        file.write(f'PRIMVEC\n')
        file.write(f'  {primvec[0][0]:>15.9f} {primvec[0][1]:>15.9f} {primvec[0][2]:>15.9f} \n')
        file.write(f'  {primvec[1][0]:>15.9f} {primvec[1][1]:>15.9f} {primvec[1][2]:>15.9f} \n')
        file.write(f'  {primvec[2][0]:>15.9f} {primvec[2][1]:>15.9f} {primvec[2][2]:>15.9f} \n')
        file.write(f'PRIMCOORD {conf_n+1} \n')
        file.write(f'  {Natoms}  1\n')
        for jj in range(Natoms):
            file.write(f' {atomlist[jj]}  {crystal_pos[jj][0]:>15.9f}  {crystal_pos[jj][1]:>15.9f}  {crystal_pos[jj][2]:>15.9f}  {eigenmode_x[ii]:>15.9f}  {eigenmode_y[ii]:>15.9f}  {eigenmode_z[ii]:>15.9f} \n')
            ii+=1
        file.close()

    return()
