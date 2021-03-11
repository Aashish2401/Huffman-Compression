import array
import os
import pickle

#Class whose objects are used to represent nodes on the huffman tree
class nodes:
    char = ''
    bit = ''
    code = ''
    freq = 0
    id_no = 0
    point = 0
    def __init__(self):
        prev = self

file = input("Enter your text filename: ")
file = file.replace(".txt",'')
for r,d,f in os.walk("D:\\"):
    for files in f:
         if files == file + ".txt":
              path = os.path.join(r,files)

path = path.replace(file + ".txt",'')
f = open(path + file + '.txt',mode = 'r')
content = f.read()

unique = list((set(content)))   #Set of all unique characters present in the text file
freq = [0] * len(unique)

#Loop to calculate the frequency of occurence of every character in the text file
for i in range(len(unique)):
    for j in range(len(content)):
        if unique[i] == content[j]:
            freq[i] += 1

bits = {}
bits_to_char = {}
n = []            
u_char = ['0']*len(freq)
u_freq = [0]*len(freq)
temp_char = ['0']*len(freq)
temp_freq = [0]*len(freq)
id_no = [i for i in range(len(unique))]

#Sorting and saving the character and frequencies in 2 lists for future use
ind = 0
for i in range(len(unique)):
    temp = freq.index(min(freq))
    u_char[ind] = unique[temp]
    u_freq[ind] = freq[temp]
    temp_char[ind] = unique[temp]
    temp_freq[ind] = freq[temp]
    del freq[temp]
    del unique[temp]
    ind += 1

#Huffman tree construction
index = 0
while len(temp_freq) >= 2:
    #Find the character with minimum frequency
    minc1 = temp_char[temp_freq.index(min(temp_freq))]
    minf1 = min(temp_freq)
    min_id1 = id_no[temp_freq.index(min(temp_freq))]
    id_no.append(id_no[-1] + 1)
    #Delete it from the list
    del(temp_char[temp_freq.index(min(temp_freq))])
    del(id_no[temp_freq.index(min(temp_freq))])
    del(temp_freq[temp_freq.index(min(temp_freq))])
    #Add this character and its details to a node
    n.append(nodes())
    n[index].char = minc1
    n[index].freq = minf1
    n[index].bit = '0'
    n[index].id_no = min_id1
    n[index].point = id_no[-1]
    #Find the character with second minimum frequency
    index = index + 1
    minc2 = temp_char[temp_freq.index(min(temp_freq))]
    minf2 = min(temp_freq)
    min_id2 = id_no[temp_freq.index(min(temp_freq))]
    #Delete it from the list
    del(id_no[temp_freq.index(min(temp_freq))])
    del(temp_char[temp_freq.index(min(temp_freq))])
    del(temp_freq[temp_freq.index(min(temp_freq))])
    #Add this character and its details to a node
    n.append(nodes())
    n[index].char = minc2
    n[index].freq = minf2
    n[index].bit = '1'
    n[index].id_no = min_id2
    n[index].point = id_no[-1]
    #Creating a parent node for the 2 nodes whose frequency is the sum of the 2 frequencies
    temp_freq.append(minf1 + minf2)
    temp_char.append(str(minf1 + minf2))
    index = index + 1

n.append(nodes())
n[index].char = temp_char[0]
n[index].freq = temp_freq[0]
n[index].bit = ''
n[index].id_no = id_no[0]
n[index].point = None

#Assigning the pointers to the parent nodes
for i in n:
    for j in n:
        if i.point == None:
            i.prev = None
            break
        if i.point == j.id_no:
            i.prev = j
            break

#Formation of the binary code for each character from the huffman tree
for i in n:
    c = i
    while c.prev != None:
        i.code = i.code + c.bit
        c = c.prev
    i.code = i.code[::-1]

#Forming dictionaries with characters and their corresponding binary codes
for i in n:
    for j in range(len(u_char)):
        if i.char == u_char[j]:
            bits_to_char[i.code] = i.char
            bits[i.char] = i.code

f = open(path + 'bits_to_char.pkl', 'wb')
pickle.dump(bits_to_char,f)     #Saving a lookup table for decoding the compressed file.
f.close()
    
compressed = ''
#Encoding
for i in content:
    compressed = compressed + bits[i]

#Adjusting the length of the encoded string to be a multiple of 8
if len(compressed) % 8 != 0:
    compressed = compressed + ('0' * (8 - (len(compressed) % 8)))

#Creating a string of bytes
data = array.array('B')
i = 0
while i <= (len(compressed) - 8):
    data.append(int(compressed[i:i+8], 2))
    i = i + 8

#Writing the bytes to a binary file
f = open(path + file+'_comp.aash', 'wb')
data.tofile(f)
f.close()

print("\n\n\nCompression completed!!\n\nFile stored as " + file + "_comp.aash\n\n\n")
input()