import subprocess
import glob
import globber
import re
import os
import sys
from settings.settings import colorShellText, colorOutput
import threading
import signal
import logging

"""
Tasks completed:
- add piping
- prevent Keyboard Interupt
- error handling
- add history command
- add globbing
- think of good name
- add history clear
- add !!
- add &&
- add '&' keyword
  - multiprocessing
"""

"""
TODO:
- add arrow keys
- add tui
- add zsh-like auto cd
 - optional
- add more settings
- capture error code
  - add command to show prev error code
- add running of files e.g. finnsh thing.finnsh
  -should be pretty easy
  -prob use argparse or sys.argv
- add shellscript that runs the whole thing
- add help command
  - should be pretty easy
"""

home = os.path.expanduser("~")
commandList = []

def runCommand(cmd):
  cmd = cmd.split() #split to get arguments
  cmd2 = []
  for x in cmd:
    cmd2.append(globber.globber(x))
  cmd = cmd2
  
  if "cd" in cmd: 
    if len(cmd) == 1 or "~" in cmd: 
      os.chdir(home) # change to home dir 
    else:
      os.chdir(cmd[1])

  elif cmd[0] == "history":
    with open(f"{home}/history.txt","r") as file:
      lines = file.read() 
    print(lines) #read and print all lines
    
  elif cmd[0] == "histclear":
    with open(f"{home}/history.txt","w") as file:
      file.write("\n") #write newline into file to clear
      
  elif "&" in " ".join(cmd) and not "&&" in " ".join(cmd):
    subprocess.Popen()
  else:
    commandList.append(cmd)
    cmd = " ".join(cmd)
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True)

    # Read and print output line by line
    for line in process.stdout:
      print(colorOutput(line), end='')

    _, error = process.communicate()
    if process.returncode != 0:
        print(f"finnsh: {error}")


def main():
  while True: #the loop
    try:
      cmd = input(f"{colorShellText(os.getcwd())}> ").strip()
      with open(f"{home}/shell/history.txt","r") as file:
        prevCommand = file.readlines()[-1]
      cmd = cmd.replace("!!",prevCommand)
      with open(f"{home}/shell/history.txt","a") as file:
        if cmd == "" or cmd == "history" or cmd == "histclear":
          pass
        else:
          file.write("\n"+cmd)
      if len(cmd) == 0:
        continue
      elif cmd == "exit":
        break
      runCommand(cmd)
    except KeyboardInterrupt: #handles keyboardinterrupt
      print() #adds newline
      
    except Exception as e:
      print(f"finnsh: {e}")  #prints error 
      #TODO: capture error code


if __name__ == "__main__":
  main()