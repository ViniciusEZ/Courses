import subprocess

# Linux - ping -c 4

procs = subprocess.run(['ping', '127.0.0.1', '-c', '4'],
                       capture_output=True,
                       text=True)

print(procs.stdout)

