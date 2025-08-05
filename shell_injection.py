# # CWE-78: OS Command Injection

# import os

# def ping_host():
#     host = input("Enter host to ping: ")
    
#     # Shell Injection (Bandit & Semgrep)
#     os.system(f"ping -c 4 {host}")  

# ping_host()