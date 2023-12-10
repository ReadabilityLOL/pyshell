import glob

def globber(globInput):
  globbing = ""
  for x in glob.glob(globInput):
    globbing += x + " "
  if globbing:
    return globbing.strip()
  else: 
    return globInput

if __name__ == "__main__":
  print(globber("sdfjsdkljfskd"))
