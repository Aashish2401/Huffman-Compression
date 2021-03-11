import pickle 
import os

uncompressed = ''
compressed = ''
bi = ''

#Load the lookup table into a dictionary
for r,d,f in os.walk("D:\\"):
    for files in f:
         if files == 'bits_to_char.pkl':
              path = os.path.join(r,files)
path = path.replace('bits_to_char.pkl', '')
with open(path + 'bits_to_char.pkl', 'rb') as f: 
    data = pickle.load(f)
    
bits_to_char = data

#Reading the compressed file
file = input("Enter the name of the compressed file(.aash):")
file = file.replace(".aash",'')
with open(path + file + '.aash', 'rb') as f: 
    data = f.read()

#Primitive way to remove padding zeros
for i in range(len(data)):
    bi = bin(data[i]).replace("0b", "")
    extra = 8 - len(bi)
    zer = '0' * extra
    compressed = compressed + zer + bi

#Extracting text using the lookup dictionary
while len(compressed) != 0:
    prev_len = len(compressed)
    for i in bits_to_char:
        if compressed[0:len(i)] == i:
            uncompressed = uncompressed + bits_to_char[i]
            compressed = compressed.replace(i,'',1)
    if prev_len == len(compressed):
        break

#Writing to a new file
f = open(path + file + '_uncomp.txt','wt')
f.write(uncompressed)
f.close()

print("\n\n\nFile extraction completed!!\n\nFile stored as " + file + "_uncomp.txt\n\n\n")
input()