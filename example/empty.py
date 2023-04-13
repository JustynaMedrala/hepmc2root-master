# opening and creating new .txt file
with open("evrecel_hepmc.dat", 'r') as r, open('el.dat', 'w') as o:
    for line in r:
        #strip() function
        if line.strip():
            o.write(line)
