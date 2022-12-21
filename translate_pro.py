import sys
#selected pdbfile
pdbfile = sys.argv[1]

translate=[x/10 for x in range(1,6)]

with open(pdbfile,"r")as f:
    lines = f.readlines()

#make_replace_pdb
for t in translate:
    filename = pdbfile[:-4]+"_translate_"+str(t)+".pdb"
    with open(filename,"w") as f2:
        for line in lines:
            x = line.split()
            if str(x[0]) == 'ATOM':
                a = round(float(x[6])+t,3)
                b = round(float(x[7])+t,3)
                c = round(float(x[8])+t,3)

            if str(line[0:4]) == 'ATOM':
                newline = line.replace(line[30:38],'{:>8}'.format(a))
                newline = newline.replace(line[38:46],'{:>8}'.format(b))
                newline = newline.replace(line[46:54],'{:>8}'.format(c))

#write
            if str(line[0:4]) == 'ATOM':
                f2.write(str(newline))
            else:
                f2.write(str(line))


