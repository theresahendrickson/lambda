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
  
#Creating a HashTable of length 8 as a list
HashTable = [[] for _ in range(8)]
  
# Hashing Function using DJB2 to return key for every value.
def Hashing(strValue):
	hash = 5381;
	for i in strValue:
		hash = ((hash << 5) + hash) + ord(i)
	return hash % len(HashTable)


# put function to add values to the hash table
def put(Hashtable, value):
	hash_key = Hashing(value)
	Hashtable[hash_key].append(value)

# get function to fine value in the hash table
def get(Hashtable, value):
	hash_key = Hashing(value)
	if value in Hashtable[hash_key]:
		print('Value ' + value + ' found in HashTable at hashkey ' + str(hash_key))
		return hash_key
	else:
		return -1
		


# deleEntry function to remove values from the hash table
def deleEntry(Hashtable, value):
	hash_key = get(Hashtable, value)
	if (hash_key == -1):
		print('Unable to delete ' + value)
		return -1
	
	Hashtable[hash_key].remove(value)
	print('Value ' + value + ' removed from HashTable')
  
# Driver Code
put(HashTable, 'Globe')
put(HashTable, 'Flagstaff')
put(HashTable, 'Queen Creek')
put(HashTable, 'Goodyear')
put(HashTable, 'Mesa')
put(HashTable, 'Tonto Basin')
put(HashTable, 'Mammoth')
put(HashTable, 'Sedona')
put(HashTable, 'Tombstone')
put(HashTable, 'Sun Valley')
put(HashTable, 'Thatcher')
put(HashTable, 'San Manuel')
put(HashTable, 'Yuma')
put(HashTable, 'Sells')
put(HashTable, 'Tucson')
put(HashTable, 'Snowflake')
display(HashTable)

deleEntry(HashTable, 'Globe')
display(HashTable)

deleEntry(HashTable, 'Sun Valley')
display(HashTable)

deleEntry(HashTable, 'Clayton')
display(HashTable)

