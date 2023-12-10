from termcolor import colored, cprint
import os
import toml


#TODO: add toml group names

if os.name == 'nt':
  os.system("color")

file_path = "/home/runner/shell/settings/settings.toml"
default_path = "/home/runner/shell/settings/default.toml"

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
  return colored(command, getValue("shell", "basicColor"), attrs=getValue("shell", "basicColorAttrs"))

def colorOutput(command):
  return colored(command, getValue("output", "basicColor"), attrs=getValue("output", "basicColorAttrs"))