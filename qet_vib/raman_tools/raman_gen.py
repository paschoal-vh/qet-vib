def calculate_intensity(mode_number,sys_name='',filename='phG.out',amplitude=1):

    import numpy as np
    import re
    from os import mkdir, getcwd, path
    local=getcwd()
    system_name=str(sys_name)
    if len(sys_name)==0:
        minus_deform=local+"\\ms_"+"\mode_"+str(mode_number)
        plus_deform=local+"\\ps_"+"\mode_"+str(mode_number)
    else:
        minus_deform=local+"\\ms_"+system_name+"\mode_"+str(mode_number)
        plus_deform=local+"\\ps_"+system_name+"\mode_"+str(mode_number)
    filename=str(filename)
    c=0
    if path.isfile(plus_deform+'\\'+filename):
        c=c+1
    else:
        print('plus deform not found')
    if path.isfile(minus_deform+'\\'+filename):
        c=c+1
    else:
        print('minus deform not found')
    if (c!=2):
        print("not ok")
    data=[]
    p="Dielectric constant in cartesian axis"
    prop=re.compile(p)
    i=0
    with open(plus_deform+'\\'+filename,'r') as pf:
        for line in pf:
            i+=1
            data.append(line.split('\n'))
            for match in re.finditer(prop,line):
                dielectric_place=i
    exx_p=float(data[dielectric_place+1][0].split()[1])
    exy_p=float(data[dielectric_place+1][0].split()[2])
    exz_p=float(data[dielectric_place+1][0].split()[3])
    eyx_p=float(data[dielectric_place+2][0].split()[1])
    eyy_p=float(data[dielectric_place+2][0].split()[2])
    eyz_p=float(data[dielectric_place+2][0].split()[3])
    ezx_p=float(data[dielectric_place+3][0].split()[1])
    ezy_p=float(data[dielectric_place+3][0].split()[2])
    ezz_p=float(data[dielectric_place+3][0].split()[3])
    dielectric_p=np.array([[exx_p,exy_p,exz_p],[eyx_p,eyy_p,eyz_p],[ezx_p,ezy_p,ezz_p]])
    data=[]
    i=0
    with open(minus_deform+'\\'+filename,'r') as pf:
        for line in pf:
            i+=1
            data.append(line.split('\n'))
            for match in re.finditer(prop,line):
                dielectric_place=i
    exx_n=float(data[dielectric_place+1][0].split()[1])
    exy_n=float(data[dielectric_place+1][0].split()[2])
    exz_n=float(data[dielectric_place+1][0].split()[3])
    eyx_n=float(data[dielectric_place+2][0].split()[1])
    eyy_n=float(data[dielectric_place+2][0].split()[2])
    eyz_n=float(data[dielectric_place+2][0].split()[3])
    ezx_n=float(data[dielectric_place+3][0].split()[1])
    ezy_n=float(data[dielectric_place+3][0].split()[2])
    ezz_n=float(data[dielectric_place+3][0].split()[3])
    dielectric_n=np.array([[exx_n,exy_n,exz_n],[eyx_p,eyy_n,eyz_n],[ezx_n,ezy_n,ezz_n]])
    
    delta_dielectric=(dielectric_p-dielectric_n)/amplitude
    
    Ialpha=45.0*(1.0/3.0*(delta_dielectric[0][0]+delta_dielectric[1][1]+delta_dielectric[2][2]))**2
    
    Ibeta=7.0/2.0*((delta_dielectric[0][0]-delta_dielectric[1][1])**2+(delta_dielectric[0][0]-delta_dielectric[2][2])**2+
                   (delta_dielectric[1][1]-delta_dielectric[2][2])**2)+6.0*(delta_dielectric[0][1]**2+delta_dielectric[0][2]**2+delta_dielectric[1][2]**2)
    
    Ibackscattering=Ialpha+Ibeta
    
    return(Ialpha,Ibeta,Ibackscattering)
