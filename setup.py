import subprocess

with open("commands.txt", "r") as f:
    commands = f.readlines()
    for command in commands:
        subprocess.run(command.split(" "))
