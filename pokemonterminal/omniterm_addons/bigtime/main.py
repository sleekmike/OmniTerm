import sys
import subprocess

def main():
    subprocess.run(
        # Location of Micro's Binary + adding command args to construct the command to run
        f'bigtime {' '.join(sys.argv[1:])}', 
        shell=True
    )