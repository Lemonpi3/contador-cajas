import os

path = "./data/RawOriginal"
files = os.listdir(path)
suffix = 'raw_'

for i,file in enumerate(files):
    os.rename(f"{path}/{file}",f"{path}/{suffix}{i}.jpg")