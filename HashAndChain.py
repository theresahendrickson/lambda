# Function to display the hashTable
def display(hashTable):
    
    print()
    print('PRINTING HASHTABLE::')
    print()
    #outer loop to print first entry for each hash_key
    for i in range(len(hashTable)):
        print(i, end = " ")
        
        #inner loop to print through collision list
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
             
        print()
  

  
# Hashing Function using DJB2 to return key for every value.
def Hashing(Hashtable, strValue):
	hash = 5381;
	for i in strValue:
		hash = ((hash << 5) + hash) + ord(i)
	return hash % len(Hashtable)


# put function to add values to the hash table
def put(Hashtable, value):
	hash_key = Hashing(Hashtable,value)
	Hashtable[hash_key].append(value)
	return 0

# get function to fine value in the hash table
def get(Hashtable, value):
	hash_key = Hashing(Hashtable,value)
	if value in Hashtable[hash_key]:
		return 0
	else:
		return -1
		

# deleEntry function to remove values from the hash table
def deleEntry(Hashtable, value):
	hash_key = Hashing(Hashtable, value)
	if value in Hashtable[hash_key]:
		Hashtable[hash_key].remove(value)
		return 0
	else:
		return -1
	
	
 
