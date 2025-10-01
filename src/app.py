import subprocess
import shlex

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b

def run_command(cmd):
    # FIX: hindari shell=True, gunakan shlex.split untuk parsing
    args = shlex.split(cmd)
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout