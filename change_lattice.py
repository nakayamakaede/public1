import sys
#selected pdbfile
pdbfile = sys.argv[1]

#get lattice and plot
with open(pdbfile,"r") as f:
    lines = f.readlines()

ch = 0.02
filename = f'cl86_{ch}.pdb'

with open(filename,"w") as f2:
    for line in lines:
        x = line.split()
        if str(x[0]) == 'CRYST1':
            x1 = float(x[1])
            y1 = float(x[2])+float(x[2])*ch
            z1 = float(x[3])
            
            crline = line.replace(line[9:15],'{:.03f}'.format(x1))
            crline = crline.replace(line[18:24],'{:.03f}'.format(y1))
            crline = crline.replace(line[27:33],'{:.03f}'.format(z1))

            f2.write(crline)


        if str(x[0]) == 'ATOM':           
            x2 = round(float(x[6]),3)
            y2 = round(float(x[7])/(1+float(ch)),3)
            z2 = round(float(x[8]),3)
    
            newline = line.replace(line[30:38],'{:>8}'.format(x2))
            newline = newline.replace(line[38:46],'{:>8}'.format(y2))
            newline = newline.replace(line[46:54],'{:>8}'.format(z2))
        
            f2.write(newline)
                
        else:
            f2.write(line)
