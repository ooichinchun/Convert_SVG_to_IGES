import re

svg_file = open('map.svg',mode='rU')

## Filter 1 : RGB (96.862745%,93.72549%,71.764706%)
## Filter 2 : RGB (85.098039%,81.568627%,78.823529%)

f1 = '(96.862745%,93.72549%,71.764706%)'
f2 = '(85.098039%,81.568627%,78.823529%)'

bld_num_pts_seqList = []
bld_vertex_seqList = []


counter = 0

for L1 in svg_file:
    L1stripped = L1.strip()
    
    if 'style="fill-rule:evenodd;' in L1stripped:
        
        if f1 or f2 in L1stripped:
            
            counter += 1
            y = re.findall('d="(.*Z)',L1stripped)
            for yy in y:
                yyy = yy.split(' ')
                num_vertex = (len(yyy)-1)/3
                bld_num_pts_seqList.append(num_vertex)
                   
                for yyyy in range(num_vertex):
                    new_pt = yyy[yyyy*3+1]+','+yyy[yyyy*3+2]+',0.'
                    bld_vertex_seqList.append(new_pt)


svg_file.close()

for n1 in range(len(bld_num_pts_seqList)):
    print bld_num_pts_seqList[n1]

out_File = open('sur_bld_template.igs',mode='rU')

content = out_File.read()

with open('sur_bld.igs','w') as f:
    f.write(content)
    d_counter = 0
    for n1 in range(len(bld_vertex_seqList)):
        d_counter += 1
        if d_counter<10:
            d_str = '  ' + str(d_counter)
        elif d_counter<100:
            d_str = ' ' + str(d_counter)
        else:
            d_str = str(d_counter)
            
        if n1<9:
            n_str = '  ' + str(n1+1) 
        elif n1<99:
            n_str = ' ' + str(n1+1)
        else:
            n_str = str(n1+1)


        f.write('     116     ' + n_str + '       0       1       0       0       0       000000001D    '+d_str+'\n')
        f.write('     116       1       0       1       0       0       0vertex.')
        if n1<9:
            n_str = str(n1+1) + '  ' 
        elif n1<99:
            n_str = str(n1+1) + ' '
        else:
            n_str = str(n1+1)
        f.write(n_str)
    
        d_counter += 1
        if d_counter<10:
            d_str = '  ' + str(d_counter)
        elif d_counter<100:
            d_str = ' ' + str(d_counter)
        else:
            d_str = str(d_counter)
        f.write('     0D    '+d_str+'\n')
        
    for n1 in range(len(bld_vertex_seqList)):
        front_string = '116,'+bld_vertex_seqList[n1] + ';'
        blank_rep = ' ' * (72-len(front_string)-3)
        n1_double = n1*2 + 1

        if n1_double<10:
            n_str_2 = '  ' + str(n1_double) 
        elif n1_double<100:
            n_str_2 = ' ' + str(n1_double)
        else:
            n_str_2 = str(n1_double)

        if n1<9:
            n_str = '  ' + str(n1+1) 
        elif n1<99:
            n_str = ' ' + str(n1+1)
        else:
            n_str = str(n1+1)
            
        f.write(front_string+blank_rep+n_str_2 + 'P    ' +n_str+ '\n')

    f.write('S      1G      3D    '+d_str+'P    '+n_str+' '*40+'T      1')
    
out_File.close()
f.close()
