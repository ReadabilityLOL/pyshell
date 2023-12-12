from termcolor import colored, cprint
import os
import toml

home = os.path.expanduser("~")

#TODO: add more settings

if os.name == 'nt':
  os.system("color")

file_path = f"{home}/settings.toml"
default_path = f"{home}/default.toml"

def getValue(group, value):
  with open(file_path, 'r') as file:
    data = toml.load(file)
    try:
      groupData = data[group]
    except:
      groupData = ""

    if value not in groupData:
      with open(default_path, 'r') as file:
        data = toml.load(file)  
        groupData = data[group]
        return groupData[value]
    return groupData[value]

def colorShellText(command):
  try:
    return colored(command, getValue("shell", "basicColor"), attrs=getValue("shell", "basicColorAttrs"))
  except:
    return command

def colorOutput(command):
  try:
    return colored(command, getValue("output", "basicColor"), attrs=getValue("output", "basicColorAttrs"))
  except:
    return command

def permanintAlias(command1):
  try:
    with open(file_path, 'r') as file:
      data = toml.load(file)
    
      groupData = data["alias"]
      for i in groupData:
        command1 = command1.replace(i,groupData[i])
      return command1
  except Exception as e:
    return command1
