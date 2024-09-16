with open("homefab_gerber.gbr", "w") as file1:
    with open("gerber.gbr", "r") as file2:
        while True:
            line = file2.readline()
            if line.strip() != "M02*":
                file1.write(line)
            else:
                break

    with open("dril.gbr", "r") as file3:
        while True:
            line = file3.readline()
            
            if line.strip() == "G04 APERTURE END LIST*":
                break
            else:
                continue
        
        file1.write("%TA.AperFunction,Conductor*%\n%ADD10C,0.800000*%\n%TD*%\nD10*\n%LPC*%\n")

        while True:
            line = file3.readline()
            if line.strip() == "":
                break 
            elif (line.strip())[0] == "X":
                file1.write(line)
    
    file1.write("M02*")