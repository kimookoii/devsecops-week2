# src/app.py
import os

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b

# Controlled "commands" implemented in Python (no subprocess)
def _cmd_ls(args):
    path = args or "."
    return "\n".join(os.listdir(path))

def _cmd_pwd(_args):
    return os.getcwd()

ALLOWED_COMMANDS = {
    "ls": _cmd_ls,
    "pwd": _cmd_pwd,
}

def run_command_safe(cmd_name, args=None):
    """
    Only allow pre-defined commands handled by Python functions.
    This avoids shell execution and prevents command injection.
    """
    if cmd_name not in ALLOWED_COMMANDS:
        raise ValueError("Perintah tidak diizinkan")

    return ALLOWED_COMMANDS[cmd_name](args)

if __name__ == "__main__":
    print(add(2,3))
    print(divide(10,2))
    print(run_command_safe("pwd"))
