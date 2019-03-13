
# 1) Open Python shell in the same location like the script
# 2) >>> import prepare_jobs
# 3) >>> data = prepare_jobs.rewrite()
# 4) Access M by 'prepare_jobs.M'

import numpy as np

def rewrite():
    f = open('shops.dat', 'r')
    d = f.readlines()
    
    cities = ['Z', 'D', 'B', 'N']
    
    k = []
    
    cnt = 0
    
    for i in d:
        if(len(i.split('&')) > 1): 
            l = []
    
            # Insert the city label using a cyclic counter
            l.append(cities[cnt // 4])
    
            # Return a new list with sales Q1, Q2, Q3
            l = l + i.split('&')[0:4]
    
            # Append sales Q4 (split trailing slashes)
            l.append(i.split('&')[4].split('\\')[0])
    
            # Prepare writeable list
            k.append(l)
    
            # Cycle city counter
            cnt += 1
    
    output = open('output.dat', 'w')
    output.write('City Sport Q1 Q2 Q3 Q4\n')
    for i in k:
        output.write(" ".join(i) + '\n')
    output.close()
    
    filehandle = open('output.dat', 'r')
    data = filehandle.readlines()
    for i in data:
        print(i, end='')
    
    return data

data = rewrite()
M = []

# Skip header line
for i in data[1:]:
    l = []
    l = i.split(' ')[2:5]
    l.append(i.split(' ')[5].split('\n')[0])
    M.append(l)

M = np.array(M)

print(M)
print(type(M))

Z = M[0:4]
D = M[4:8]
B = M[8:12]
N = M[12:16]

def convert_to_float(B):
    print("Converting...")
    return np.array([list(map(lambda x: float(x), Bi)) for Bi in B])

Z = convert_to_float(Z)
D = convert_to_float(D)
B = convert_to_float(B)
N = convert_to_float(N)



# Z = np.array([list(map(lambda x: float(x), Bi)) for Bi in Z])


