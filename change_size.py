import sys
#selected pdbfile
pdbfile = sys.argv[1]

#make_replace_pdb
def pdb_replace(lines,a,b,c):
    for line in lines:
        if str(line[0:6]) == 'CRYST1':
            newline = line.replace(line[9:15],'{:.03f}'.format(a))
            newline = newline.replace(line[18:24],'{:.03f}'.format(b))
            newline = newline.replace(line[27:33],'{:.03f}'.format(c))
    
    filename = pdbfile[:-4]+"_"+str(a)+"_"+str(b)+"_"+str(c)+".pdb" 
    with open(filename,"w") as f:
        for line in lines:
            if str(line[0:6]) == 'CRYST1':
                f.write(newline)
            else:
                f.write(line)
    return filename
            
with open (pdbfile,'r') as f2:
    lines = f2.readlines()

#get a,b,c    
for line in lines:
    x = line.split()
    if str(x[0]) == 'CRYST1':
        a = float(x[1])
        b = float(x[2])
        c = float(x[3])

#3% change
for i in range(1,5):
    for j in range(1,6):
        if i == 1:
            a2 = a + a*0.03*j
            pdb_replace(lines,a2,b,c)        
        elif i == 2:
            b2 = b + b*0.03*j
            pdb_replace(lines,a,b2,c)
        elif i == 3:
            c2 = c + c*0.03*j
            pdb_replace(lines,a,b,c2)
        elif i == 4:
            a2 = a + a*0.03*j
            b2 = b + b*0.03*j
            c2 = c + c*0.03*j
            pdb_replace(lines,a2,b2,c2)
        else:
            print('error')  
