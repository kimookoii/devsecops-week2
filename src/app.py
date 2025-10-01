import subprocess
import shlex

def run_command(cmd):
    # Gunakan shlex.split agar input terpecah sesuai argumen, tidak raw string
    args = shlex.split(cmd)
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout