def generate_Raman(n_conf,extract_directory,system_name,control,system,electron,k_points,a=1):
    import numpy as np
    from os import mkdir, getcwd, path
    local=getcwd()
    filename=local+'\\'+str(extract_directory)+'\conf_'+str(n_conf)+'.xsf'
    data=[]
    with open(filename) as f:
        for line in f:
            data.append(line.split())
    primvec=np.array([[float(data[2][0]),float(data[2][1]),float(data[2][2])],
                      [float(data[3][0]),float(data[3][1]),float(data[3][2])],
                      [float(data[4][0]),float(data[4][1]),float(data[4][2])]])
    posx=[] 
    dsx=[] 
    posy=[]
    dsy=[] 
    posz=[]
    dsz=[]
    atomlist=[]
    for ii in range(int(system['nat'])):
            atomlist.append(data[7+ii][0])
            posx.append(float(data[7+ii][1]))
            posy.append(float(data[7+ii][2]))
            posz.append(float(data[7+ii][3]))
            dsx.append(float(data[7+ii][4])*(2*hart*atomic_species[atomlist[ii]][0]))
            dsy.append(float(data[7+ii][5])*(2*hart*atomic_species[atomlist[ii]][0]))
            dsz.append(float(data[7+ii][6])*(2*hart*atomic_species[atomlist[ii]][0]))
    norm_displacement=np.linalg.norm(dsx)**2+np.linalg.norm(dsy)**2+np.linalg.norm(dsz)**2
    system_name=str(system_name)
    appendix='\ms_'+system_name+'\mode_'+str(n_conf)
    mkdir(local+appendix)
    filelocation=local+appendix
    file=open(filelocation+'\pw.in','w')
    file.write('&CONTROL\n')
    file.write('    '+'calculation'+'='+'\''+control['calculation_type']+'\''+','+'\n')
    file.write('    '+'prefix'+'='+'\''+control['prefix_type']+'\''+','+'\n')
    file.write('    '+'pseudo_dir'+'='+'\''+control['pseudo_dir']+'\''+','+'\n')
    file.write('    '+'outdir'+'='+'\''+control['outdir']+appendix.replace("\\" , '/')+'\''+','+'\n')
    file.write('/\n')
    file.write('\n')
    file.write('&SYSTEM\n')
    file.write('    '+'ibrav'+'='+str(system['ibrav'])+','+'\n')
    file.write('    '+'nat'+'='+str(system['nat'])+','+'\n')
    file.write('    '+'ntyp'+'='+str(system['ntyp'])+','+'\n')
    file.write('    '+'ecutwfc'+'='+str(system['ecutwfc'])+','+'\n')
    file.write('    '+'ecutrho'+'='+str(system['ecutrho'])+','+'\n')
    file.write('    '+'vdw_corr'+'='+'\''+str(system['vdw_corr'])+'\''+','+'\n')
    file.write('/\n')
    file.write('\n')
    file.write('&ELECTRONS\n')
    file.write('    '+'conv_thr'+'='+str(electron['conv_thr']).replace('e','d')+'\n')
    file.write('/\n')
    file.write('\n')
    file.write('ATOMIC_SPECIES\n')
    atomtypes=np.unique(atomlist)
    for ii in range(len(atomtypes)):
        file.write(atomtypes[ii]+'    '+str(atomic_species[atomtypes[ii]][0])+'    '+atomic_species[atomtypes[ii]][1].strip('\'')+'\n')
    file.write('\n')
    file.write('CELL_PARAMETERS angstrom\n')
    file.write('    ''%.9f' '    ' '%.9f' '    ' '%.9f''\n' % (primvec[0][0],primvec[0][1],primvec[0][2]))
    file.write('    ''%.9f' '    ' '%.9f' '    ' '%.9f''\n' % (primvec[1][0],primvec[1][1],primvec[1][2]))
    file.write('    ''%.9f' '    ' '%.9f' '    ' '%.9f''\n' % (primvec[2][0],primvec[2][1],primvec[2][2]))
    file.write('\n')
    file.write('ATOMIC_POSITIONS angstrom\n')
    for jj in range(int(system['nat'])):
        file.write(atomlist[jj]+'   ' '%.9f' '   ' '%.9f' '   ' '%.9f\n'%(posx[jj]-a*dsx[jj]/norm_displacement**(1/2),posy[jj]-a*dsy[jj]/norm_displacement**(1/2),posz[jj]-a*dsz[jj]/norm_displacement**(1/2)))
    file.write('\n')
    file.write('K_POINTS automatic\n')
    file.write('%d'' ' '%d' ' ' '%d' ' ' '%d' ' ' '%d' ' ' '%d' % (k_points[0],k_points[1],k_points[2],k_points[3],k_points[4],k_points[5]))
    file.close()
    appendix='\ps_'+str(system_name)+'\mode_'+str(n_conf)
    mkdir(local+appendix)
    filelocation=local+appendix
    file=open(filelocation+'\pw.choline.in','w')
    file.write('&CONTROL\n')
    file.write('    '+'calculation'+'='+'\''+control['calculation_type']+'\''+','+'\n')
    file.write('    '+'prefix'+'='+'\''+control['prefix_type']+'\''+','+'\n')
    file.write('    '+'pseudo_dir'+'='+'\''+control['pseudo_dir']+'\''+','+'\n')
    file.write('    '+'outdir'+'='+'\''+control['outdir']+appendix.replace("\\" , '/')+'\''+','+'\n')
    file.write('/\n')
    file.write('\n')
    file.write('&SYSTEM\n')
    file.write('    '+'ibrav'+'='+str(system['ibrav'])+','+'\n')
    file.write('    '+'nat'+'='+str(system['nat'])+','+'\n')
    file.write('    '+'ntyp'+'='+str(system['ntyp'])+','+'\n')
    file.write('    '+'ecutwfc'+'='+str(system['ecutwfc'])+','+'\n')
    file.write('    '+'ecutrho'+'='+str(system['ecutrho'])+','+'\n')
    file.write('    '+'vdw_corr'+'='+'\''+str(system['vdw_corr'])+'\''+','+'\n')
    file.write('/\n')
    file.write('\n')
    file.write('&ELECTRONS\n')
    file.write('    '+'conv_thr'+'='+str(electron['conv_thr']).replace('e','d')+'\n')
    file.write('/\n')
    file.write('\n')
    file.write('ATOMIC_SPECIES\n')
    atomtypes=np.unique(atomlist)
    for ii in range(len(atomtypes)):
        file.write(atomtypes[ii]+'    '+str(atomic_species[atomtypes[ii]][0])+'    '+atomic_species[atomtypes[ii]][1].strip('\'')+'\n')
    file.write('\n')
    file.write('CELL_PARAMETERS angstrom\n')
    file.write('    ''%.9f' '    ' '%.9f' '    ' '%.9f''\n' % (primvec[0][0],primvec[0][1],primvec[0][2]))
    file.write('    ''%.9f' '    ' '%.9f' '    ' '%.9f''\n' % (primvec[1][0],primvec[1][1],primvec[1][2]))
    file.write('    ''%.9f' '    ' '%.9f' '    ' '%.9f''\n' % (primvec[2][0],primvec[2][1],primvec[2][2]))
    file.write('\n')
    file.write('ATOMIC_POSITIONS angstrom\n')
    for jj in range(int(system['nat'])):
        file.write(atomlist[jj]+'   ' '%.9f' '   ' '%.9f' '   ' '%.9f\n'%(posx[jj]+a*dsx[jj]/norm_displacement**(1/2),posy[jj]+a*dsy[jj]/norm_displacement**(1/2),posz[jj]+a*dsz[jj]/norm_displacement**(1/2)))
    file.write('\n')
    file.write('K_POINTS automatic\n')
    file.write('%d'' ' '%d' ' ' '%d' ' ' '%d' ' ' '%d' ' ' '%d' % (k_points[0],k_points[1],k_points[2],k_points[3],k_points[4],k_points[5]))
    file.close()
