def overwritefile(input,file):
  with open(file,"w") as item:
    item.write(input)

def appendfile(input,file):
   with open(file,"a") as item:
    item.write(input)