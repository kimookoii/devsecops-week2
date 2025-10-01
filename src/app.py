# src/app.py

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b

# contoh fungsi berbahaya yang sempat kita tambahkan untuk uji Bandit
import subprocess
import shlex

def run_command(cmd):
    args = shlex.split(cmd)
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
