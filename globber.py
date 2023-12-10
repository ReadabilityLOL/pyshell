import glob

def globber(globInput):
  globbing = ""
  for x in glob.glob(globInput):
    globbing += x + " "
  return globbing

if __name__ == "__main__":
  print(globber("*"))
