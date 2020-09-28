students={"Chem2":0, "Chem8":0, "Chem10":0}
students["Chem2"]=373
students["Chem8"]=273
students["Chem10"]=301
students["Chem2"]+=5
students["Chem10"]-=14
for i in students:
    print("%6s: %5d"%(i, students[i]))
