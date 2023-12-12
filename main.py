import subprocess
import globber
import re
import os
import getpass
import sys
from settings.settings import *
import threading
import signal
import logging
from shlex import split

"""
Tasks completed:
- add piping
- prevent Keyboard Interupt
- error handling
- add history command
- add globbing
- add aliases
- think of good name
- add history clear
- add !!
- add &&
- fix bug where empty history.txt causes error
  - possibly try-except 
"""

"""
TODO:
- add the memes
  - add special argument that does this
  - reverse sl and ls
  - all text is cowsay
  - all text is lolcat
- add arrow keys *important*
- add '&' keyword (hard)
  - multiprocessing
- add tui (optional)
- add zsh-like auto cd (optional) 
- add more settings
- capture error code
  - add command to show prev error code
- add running of files e.g. finnsh thing.finnsh
  -should be pretty easy
  -prob use argparse or sys.argv
- add shellscript that runs the whole thing
  - takes argument(s)
- comment code *important*
- add help command
  - should be pretty easy
- add >, >>, 2>, etc commands *important*
- add EOF keyword
- add / at end of line to wait for newline
- add () keywords
- add modularity
- add configuratibility
- add nushell-like output 
  - see nushell website
- add echo builtin for speed
- add printf as well
- add 'test' builtin
- add 'kill' builtin
- the above are external, but should be built internally for safety
"""

home = os.path.expanduser("~")
commandList = []
aliases = dict()

def runCommand(cmd):
  cmd = split(cmd)  #split to get arguments
  cmd2 = []
  for x in cmd:
    cmd2.append(globber.globber(x))
  cmd = cmd2

  try:
    if cmd[0] == "history":
      with open(f"{home}/history.txt", "r") as file:
        lines = file.read()
      print(lines)  #read and print all lines
  except:
    print("History File Empty")

  if "cd" in cmd:
    if len(cmd) == 1 or "~" in cmd:
      os.chdir(home)  # change to home di
    else:
      os.chdir(cmd[1])
    
  elif cmd[0] == "histclear":
    with open(f"{home}/history.txt", "w") as file:
      file.truncate(0) #clear file

  elif "&" in " ".join(cmd) and "&&" not in " ".join(cmd): #this won't work long term
    fullCommand = " ".join(cmd)
    fullCommand = fullCommand.split("&")
    t1 = threading.Thread(target=runCommand(fullCommand[0]), args=(10, ))
    t1.start()
  elif "alias" in "".join(cmd) and "=" in "".join(cmd): #also wont work long term, maybe regex later
    aliased = "".join(cmd).replace("alias","").split("=")[0] #very ugly code
    alias = "".join(cmd).replace("alias","").split("=")[1]

    aliases[aliased] = alias
    
  else:
    commandList.append(cmd)
    cmd = " ".join(cmd)
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               bufsize=1,
                               universal_newlines=True)

    # Read and print output line by line
    for line in process.stdout:
      print(colorOutput(line), end='')

    _, error = process.communicate()
    if process.returncode != 0:
      print(f"finnsh: {error}")


def main():
  while True:  #the loop
    try:
      command1 = input(
          f"{colorShellText(getpass.getuser())}@{colorShellText(os.getcwd())}> "
      ).strip()
      command1 = permanintAlias(command1)
      for aliased,alias in aliases.items():
        command1 = command1.replace(aliased,alias) #should work
      try:
        with open(f"{home}/history", "r") as file:
          prevCommand = file.readlines()[-1]
      except:
        prevCommand = "\n"
      command1 = command1.replace("!!", prevCommand)
      with open(f"{home}/history.txt", "a") as file:
        if command1 == "" or command1 == "history" or command1 == "histclear":
          pass
        else:
          file.write("\n" + command1)
      commandsplit1 = command1.split("&&")
      for cmd in commandsplit1:
        if len(cmd) == 0:
          continue
        elif cmd == "exit":
          break
        else:
          runCommand(cmd)
    except KeyboardInterrupt:  #handles keyboardinterrupt
      print()  #adds newline
  
    except Exception as e:
      print(f"finnsh: {e}")  #prints error
        #TODO: capture error code
  

if __name__ == "__main__":
  main()
