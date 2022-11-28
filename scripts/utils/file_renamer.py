import os

path = os.path.join('data','RawOriginal')
files = os.listdir(path)
suffix = 'raw_'

for i,file in enumerate(files):
    os.rename(os.path.join(path,file), os.path.join(path,f"{suffix}{i}.jpg"))