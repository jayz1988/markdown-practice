import os
import subprocess

env = os.environ
newpath = r'C:\Users\USER\Desktop\test;'+env['PATH']
env['PATH'] = newpath  

r = subprocess.run('crolling.exe push1.tcl',shell=True, capture_output=True, text=True)    
# CompletedProcess returned
print(r.args)
print(r.returncode)
print(r.stderr)
print(r.stdout)