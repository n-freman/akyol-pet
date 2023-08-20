import subprocess
from pprint import pprint as print

files = subprocess.check_output(
    "find . -name '*django.po*' | grep 'tm'",
    shell=True,
    text=True
).splitlines()

plural = '"Plural-Forms: nplurals=2; plural=(n != 1);\\n"\n'

for filename in files:
    print(filename)
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines[:30]):
            print(line)
            if "Plural" in line:
                lines[i] = plural
                print('replaced')
                break
        else:
            lines.insert(18, plural)
    with open(filename, 'w') as file:
        file.writelines(lines)
