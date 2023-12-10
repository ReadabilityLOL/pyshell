import subprocess
#import tensorflow
import glob
import os
import sys
from settings.settings import colorShellText, colorOutput
import signal
import logging

"""
Tasks completed:
- add piping
- prevent Keyboard Interupt
"""

"""
TODO:
- add up and down arrows
- add !!
"""

home = os.path.expanduser("~")

commandList = []

def main():
  while True: #the loop
    try:
      cmd = input(f"{colorShellText(os.getcwd())}> ")
      cmd = cmd.split() #split to get arguments 
      if "cd" in cmd: 
        if len(cmd) == 1 or "~" in cmd: 
          os.chdir(home) 
        else:
          os.chdir(cmd[1])
      elif len(cmd) == 0:
        continue
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
            print(f"Error executing command: {cmd}")
            if error:
                print(f"Error message: {error}")
    except KeyboardInterrupt: #handles keyboardinterrupt
      pass
    except Exception as e: #TODO: think of a good name
      print(f"<insert cool shell name here>: {e}")  #prints error 
      #TODO: capture error code


if __name__ == "__main__":
  main()