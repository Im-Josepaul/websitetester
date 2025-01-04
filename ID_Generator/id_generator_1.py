#This program helps in generating the id's of 1st years for the Project
#into an array, so it's much easy to use later.

initial = 12110000
id = []


# Id's of CE Department
for i in range(1,26):
    id_CE = initial + 1000 + i
    id.append(id_CE)


# Id's of CSE-A Department
for i in range(1,63):
    id_CSA = initial + 2000 + i
    id.append(id_CSA)
    

# # Id's of CSE-B Department
for i in range(64,126):
    id_CSB = initial + 2000 + i
    id.append(id_CSB)
    

# Id's of EEE Department
for i in range(1,26):
    id_EEE = initial + 3000 + i
    id.append(id_EEE)
    

# # Id's of EC Department
for i in range(1,37):
    id_EC = initial + 4000 + i
    id.append(id_EC)


# # Id's of ME Department
for i in range(2,36):
    id_ME = initial + 5000 + i
    id.append(id_ME)


# Id's of MR Department
for i in range(1,27):
    id_MR = initial + 6000 + i
    id.append(id_MR)
    

# Id's of AD Department
for i in range(1,54):
    id_AD = initial + 7000 + i
    id.append(id_AD)


# Id's of RA Department
for i in range(1,17):
    id_RA = initial + 8000 + i
    id.append(id_RA)
    
# value = id[292]

print("Total number of id's available:")
print(len(id))
for j in range(len(id)):
    print(id[j])
