import subprocess

def process(lang, str):
    langList = ["el", "ru", "ja", "hi", "fa", "uk", "th", "sr", "ps",
                "mk", "ko", "he", "bg", "hy", "ar"]

    if (lang in langList):
        uconv = subprocess.Popen("uconv -x Latin-%s" % lang, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        uconv.stdin.write(str)
        result = uconv.communicate()
        result = result[0]
#        uconv.terminate()
    else:
        result = str
        
    return result
