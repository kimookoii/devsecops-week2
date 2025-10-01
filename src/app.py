# src/app.py

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b

# contoh fungsi berbahaya yang sempat kita tambahkan untuk uji Bandit
import subprocess

def run_command_safe(cmd: str):
    # hanya izinkan command tertentu (whitelist)
    allowed_cmds = ["ls", "pwd", "whoami"]
    if cmd not in allowed_cmds:
        raise ValueError("Perintah tidak diizinkan")

    result = subprocess.run([cmd], capture_output=True, text=True, check=True)
    return result.stdout