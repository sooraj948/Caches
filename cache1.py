

import math


# No. of lines=Cache size/Block Size
# No of bits in index=log2(lines)
# offset bits=log2(block size)
# tag bits=32 - index bits - offset bits

size=int(input("Input size of cache in KB: "))
block=int(input("Input size of each block in B: "))
lines=size*1024//block #1024 B = 1KB
index_bits=int(math.log(lines,2))#log base 2
# print(index_bits)
offset_bits=int(math.log(block,2))

cache=[[0,0] for i in range(lines)]#valid bit and tag are the 2 parts of the inner list

def check(address):
    global cache,lines,index_bits,offset_bits

    #Address is made of tag,index,offset

    tag_bits=32-index_bits-offset_bits
    tag=address//(2**(index_bits+offset_bits))#tag is the part of 32 bit address before index and offset
    temp=address%(2**(index_bits+offset_bits))
    index = temp//2**offset_bits

    valid=cache[index][0]#checks if data is valid

    if (valid and tag==cache[index][1]):
        return 1#HIT


    cache[index][0]=1#make valid bit 1
    cache[index][1]=tag#update tag
    
    return 0#MISS

file=input("Enter name of trace file: ")

f=open("traces/"+file+".trace","r")
l=f.readlines()#gives list of lines of the file
f.close()

hit_count=0
total=0
for i in l:

    #https://www.tutorialspoint.com/How-to-convert-hex-string-into-int-in-Python
    address = int(i.split()[1],0)#gives only the address part here

    if (check(address)):#HIT
        hit_count+=1
        # print("HIT")
    # else:
    #     print("MISS")

    total+=1


hit_rate=hit_count/total#fraction of instructions which were hits(0<=hit_rate<=1)
miss_rate=1-hit_rate

print("HIT rate is:",hit_rate)
print("MISS rate is:",miss_rate)

# print(total)
        



        





