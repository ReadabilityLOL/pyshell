import glob

def globber(globInput):
  globbing = ""
  for x in glob.glob(globInput):
    globbing += x + " "
  if globbing:
    return globbing.strip()
  else: 
    return globInput