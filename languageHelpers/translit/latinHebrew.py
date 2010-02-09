import subprocess

def ltoh(str):
    uconv = subprocess.Popen("uconv -x Latin-he_IL", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    uconv.stdin.write(str)
    cyrillic = uconv.communicate()
    return cyrillic[0]
