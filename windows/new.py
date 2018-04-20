import os

print("Wechat Audio Converter")
print("Convert Wechat audio from amr(silk) format to pcm format.")
print("Author : MSRA team of Tongji University")

file_in = input("Input the name of Wechat audio:")
file_out = input("Input the name of output audio:")
file_in = file_in.strip('"')

fs_in = open(file_in,"rb")
path = os.path.split(__file__)
print(path)
os.chdir(path[0])
fs_out = open('temp.amr',"wb")

if not fs_in.read(1) == b'#':
    fs_in.seek(1,0)

fs_out.write(fs_in.read())
fs_out.close()

if os.path.exists("silk2wav.exe"):
    print("waiting...")
else:
    print("decoder not exist!")
    print(os.path.abspath(__file__))
    exit(1)

os.system(".\silk2wav.exe "+"temp.amr "+file_out)

os.remove("temp.amr")

print("input:  " + file_in)
print("output: " + file_out)
print("Convertion finished!")
