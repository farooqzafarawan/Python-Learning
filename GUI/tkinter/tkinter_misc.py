import subprocess
from subprocess import Popen

try:
    output = subprocess.run(["powershell", "date"], universal_newlines=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(output)
    
except FileNotFoundError as e:
    print(e)
