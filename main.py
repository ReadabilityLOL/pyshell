import subprocess
import glob
import globber
import os
import sys
from settings.settings import colorShellText, colorOutput
import signal
import logging

"""
Tasks completed:
- add piping
- prevent Keyboard Interupt
- error handling
- add history command
- add globbing
- think of  a good name
"""

"""
TODO:
- add arrow keys
- add !!
- add tui
- add zsh-like auto cd
- add '&' keyword
- add more settings
- capture error codes
- add running of files
"""

home = os.path.expanduser("~")

commandList = []

def main():
  while True: #the loop
    try:
      cmd = input(f"{colorShellText(os.getcwd())}> ").strip()
      with open("history.txt","a") as file:
        file.write(cmd+"\n")
      cmd = cmd.split() #split to get arguments
      cmd2 = []
      for x in cmd:
        cmd2.append(globber.globber(x))
      cmd = cmd2
      
      if len(cmd) == 0:
        continue
      elif "cd" in cmd: 
        if len(cmd) == 1 or "~" in cmd: 
          os.chdir(home) 
        else:
          os.chdir(cmd[1])
          
      elif cmd[0] == "history":
        with open("history.txt","r") as file:
          lines = file.read()
        print(lines)
        
      elif cmd[0] == "exit":
        break
        
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
              
    except KeyboardInterrupt: #handles keyboardinterrupt
      print() #adds newline
      
    except Exception as e:
      print(f"finnsh: {e}")  #prints error 
      #TODO: capture error code


if __name__ == "__main__":
  main()