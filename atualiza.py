import os
print("gera")
os.system("python setup.py sdist bdist_wheel")
print("upgrade repo")
os.system("python setup.py sdist bdist_wheel upload")
print("git")
os.chdir("dist/")
os.system("git add *")
