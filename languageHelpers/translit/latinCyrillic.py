import subprocess

def ltoc(str):
    uconv = subprocess.Popen("uconv -x Latin-Cyrillic", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    uconv.stdin.write(str)
    cyrillic = uconv.communicate()
    uconv.terminate()
    return cyrillic[0]
