# Huffman-Compression
A simple implementation of Huffman algorithm to compress text.
This implementation is obsolete since it has to store a lookup table that takes up some extra space which significantly reduces the efficiency of the algorithm, hence even if the compressed text file seems to have a size equal to 60% of the original, in reality, the compressed file + lookup file can be upto 90% or more of the original file size, rendering compression almost useless. 
None the less, building this was a fun learning experience and a satisfying one too.
