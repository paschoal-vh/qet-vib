def fdv(mode_number,system,mode_place):

    import numpy as np
    import re
    from os import mkdir, getcwd, path
    from ..data_management import atomic_mass
    
    
    local=getcwd()
    mode_name='conf_'+str(mode_number)
    filename=local+'\\'+mode_place+'\conf_'+str(mode_number)+'.xsf'
    data=[]
    with open(filename) as f:
        for line in f:
            data.append(line.split())
  
    primvec=np.array([[np.float(data[3][0]),np.float(data[3][1]),np.float(data[3][2])],
                      [np.float(data[4][0]),np.float(data[4][1]),np.float(data[4][2])],
                      [np.float(data[5][0]),np.float(data[5][1]),np.float(data[5][2])]])
    posx=[] 
    dsx=[] 
    posy=[]
    dsy=[] 
    posz=[]
    dsz=[]
    atomlist=[]
    mass=[]
    for ii in range(int(system['nat'])):
            atomlist.append(data[7+ii][0])
            mass.append(np.float(atomic_mass(atomlist[ii])))
            posx.append(np.float(data[8+ii][1]))
            posy.append(np.float(data[8+ii][2]))
            posz.append(np.float(data[8+ii][3]))
            dsx.append(np.float(data[8+ii][4]))
            dsy.append(np.float(data[8+ii][5]))
            dsz.append(np.float(data[8+ii][6]))
    M=np.sum(mass)
    ds_x=np.array(dsx)
    ds_y=np.array(dsy)
    ds_z=np.array(dsz)
    ##translational part
    d_trans_X=np.multiply(mass,ds_x)/M
    d_trans_Y=np.multiply(mass,ds_y)/M
    d_trans_Z=np.multiply(mass,ds_z)/M
    ##calculate translation contribution relative to librational and intramolecular
    d_lib_intra_X=np.array(dsx)-d_trans_X
    d_lib_intra_Y=np.array(dsy)-d_trans_Y
    d_lib_intra_Z=np.array(dsz)-d_trans_Z
    ##librational part
    ##first: shift the center of mass
    CM_x=np.sum(np.multiply(mass,posx))/M
    CM_y=np.sum(np.multiply(mass,posy))/M
    CM_z=np.sum(np.multiply(mass,posz))/M
    pos_shift_x=np.array(posx)-CM_x
    pos_shift_y=np.array(posy)-CM_y
    pos_shift_z=np.array(posz)-CM_z
    ##second: define the inertia tensor (I)
    ### trace elements
    Ixx=np.sum(np.multiply(mass,(pos_shift_y**2+pos_shift_z**2)))
    Iyy=np.sum(np.multiply(mass,(pos_shift_x**2+pos_shift_z**2)))
    Izz=np.sum(np.multiply(mass,(pos_shift_x**2+pos_shift_y**2)))
    ### off-trace elements
    Ixy=-1*np.sum(np.multiply(mass,(np.multiply(pos_shift_x,pos_shift_y))))
    Ixz=-1*np.sum(np.multiply(mass,(np.multiply(pos_shift_x,pos_shift_z))))
    Iyz=-1*np.sum(np.multiply(mass,(np.multiply(pos_shift_y,pos_shift_z))))
    Iyx=Ixy
    Izx=Ixz
    Izy=Iyz
    I=np.array([[Ixx,Ixy,Ixz],[Iyx,Iyy,Iyz],[Izx,Izy,Izz]])
    ##third: diagnolize I
    eigenvalues_I, eigenvector_I=np.linalg.eig(I)
    ### new system of coordinates
    primvec_shift=np.array([[primvec[0,0]-CM_x,primvec[0,1]-CM_y,primvec[0,2]-CM_z],
                           [primvec[1,0]-CM_x,primvec[1,1]-CM_y,primvec[1,2]-CM_z],
                           [primvec[2,0]-CM_x,primvec[2,1]-CM_y,primvec[2,2]-CM_z]])
    transform_matrix_A=np.dot(np.transpose(primvec_shift),eigenvector_I).T 
    pos_p=[]
    ds_p=[]
    pos_p_cross_ds_p=[]
    for jj in range(int(system['nat'])):
        pos_p.append(np.matmul(transform_matrix_A,np.array([pos_shift_x[jj],pos_shift_y[jj],pos_shift_z[jj]])))
        ds_p.append(np.matmul(transform_matrix_A,np.array([dsx[jj],dsy[jj],dsz[jj]])))
        pos_p_cross_ds_p.append(np.cross(pos_p[jj],ds_p[jj]))
    ##fourth: calculate the libration angle 
    pos_cross_p=np.array(pos_p_cross_ds_p)
    mass_pos_p_cross_ds_x=np.multiply(mass, pos_cross_p[:,0])
    mass_pos_p_cross_ds_y=np.multiply(mass, pos_cross_p[:,1])
    mass_pos_p_cross_ds_z=np.multiply(mass, pos_cross_p[:,2])
    theta_x=np.sum(mass_pos_p_cross_ds_x)*((eigenvalues_I[0])**-1)
    theta_y=np.sum(mass_pos_p_cross_ds_y)*((eigenvalues_I[1])**-1)
    theta_z=np.sum(mass_pos_p_cross_ds_z)*((eigenvalues_I[2])**-1)
    ###calculate the displacement due to a mode
    rotation_matrix_x=np.array([[1,0,0],[0,np.cos(theta_x),-1*np.sin(theta_x)],[0,np.sin(theta_x),np.cos(theta_x)]])
    rotation_matrix_y=np.array([[np.cos(theta_y),0,np.sin(theta_y)],[0,1,0],[-1*np.sin(theta_y),0,np.cos(theta_y)]])
    rotation_matrix_z=np.array([[np.cos(theta_z),-1*np.sin(theta_z),0],[np.sin(theta_z),np.cos(theta_z),0],[0,0,1]])
    Id=np.identity(3)
    delta_lib_x=[]
    delta_lib_y=[]
    delta_lib_z=[]
    for ll in range (int(system['nat'])):
        delta_lib_x.append(np.matmul((rotation_matrix_x-Id),np.array(pos_p)[ll,:]))
        delta_lib_y.append(np.matmul((rotation_matrix_y-Id),np.array(pos_p)[ll,:]))
        delta_lib_z.append(np.matmul((rotation_matrix_z-Id),np.array(pos_p)[ll,:]))
    ##fifth: put the displacements back in the normal axis
    delta_lib_X=[]
    delta_lib_Y=[]
    delta_lib_Z=[]
    transform_matrix_AT=np.linalg.inv(transform_matrix_A)
    for kk in range (int(system['nat'])):
        delta_lib_X.append(np.matmul(transform_matrix_AT,delta_lib_x[kk]))
        delta_lib_Y.append(np.matmul(transform_matrix_AT,delta_lib_y[kk]))
        delta_lib_Z.append(np.matmul(transform_matrix_AT,delta_lib_z[kk]))
    ##intramolecular contributions
    d_lib_Xy=np.array(delta_lib_X)[:,1]
    d_lib_Xz=np.array(delta_lib_X)[:,2]
    d_lib_Yx=np.array(delta_lib_Y)[:,0]
    d_lib_Yz=np.array(delta_lib_Y)[:,2]
    d_lib_Zx=np.array(delta_lib_Z)[:,0]
    d_lib_Zy=np.array(delta_lib_Z)[:,1]
    d_intra_X=ds_x-(d_lib_Yx+d_lib_Zx+d_trans_X)
    d_intra_Y=ds_y-(d_lib_Xy+d_lib_Zy+d_trans_Y)
    d_intra_Z=ds_z-(d_lib_Xz+d_lib_Yz+d_trans_Z)
    ##amplitude of the displacements
    inv_atom=1/(int(system['nat']))
    D_trans_X=(inv_atom*np.sum(np.matmul(mass,d_trans_X**2)))**(1/2)
    D_lib_X=(inv_atom*np.sum(np.matmul(mass,(d_lib_Yx**2+d_lib_Zx**2))))**(1/2)
    D_intra_X=(inv_atom*np.sum(np.matmul(mass,d_intra_X**2)))**(1/2)
    D_trans_Y=(inv_atom*np.sum(np.matmul(mass,d_trans_Y**2)))**(1/2)
    D_lib_Y=(inv_atom*np.sum(np.matmul(mass,(d_lib_Xy**2+d_lib_Zy**2))))**(1/2)
    D_intra_Y=(inv_atom*np.sum(np.matmul(mass,d_intra_Y**2)))**(1/2)
    D_trans_Z=(inv_atom*np.sum(np.matmul(mass,d_trans_Z**2)))**(1/2)
    D_lib_Z=(inv_atom*np.sum(np.matmul(mass,(d_lib_Xz**2+d_lib_Yz**2))))**(1/2)
    D_intra_Z=(inv_atom*np.sum(np.matmul(mass,d_intra_Z**2)))**(1/2)
    Norm_D=D_trans_X+D_lib_X+D_intra_X+D_trans_Y+D_lib_Y+D_intra_Y+D_trans_Z+D_lib_Z+D_intra_Z
    D_lib_total=(D_lib_X+D_lib_Y+D_lib_Z)/Norm_D
    D_intra_total=(D_intra_X+D_intra_Y+D_intra_Z)/Norm_D
    D_trans_total=(D_trans_X+D_trans_Y+D_trans_Z)/Norm_D
    return(D_trans_total,D_intra_total,D_lib_total)
    
