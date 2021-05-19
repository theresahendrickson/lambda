import unittest
import HashChain

#Creating a HashTable of length 8 as a list
HashTable = [[] for _ in range(8)]

class TestHashChain(unittest.TestCase):

	def test_put(self):
		self.assertEqual(HashChain.put(HashTable, 'Mesa'), 0)
		self.assertEqual(HashChain.put(HashTable, 'Globe'),0)
		self.assertEqual(HashChain.put(HashTable, 'Flagstaff'),0)
		self.assertEqual(HashChain.put(HashTable, 'Queen Creek'),0)

		#print('HashTable result after test_put')
		#self.assertEqual(HashChain.display(HashTable),None)
		for i in HashTable:
			i.clear()


	def test_get(self):
		self.assertEqual(HashChain.put(HashTable, 'Mesa'), 0)
		self.assertEqual(HashChain.put(HashTable, 'Globe'),0)
		self.assertEqual(HashChain.put(HashTable, 'Flagstaff'),0)
		self.assertEqual(HashChain.put(HashTable, 'Queen Creek'),0)
		self.assertEqual(HashChain.put(HashTable, 'Goodyear'),0)
		self.assertEqual(HashChain.put(HashTable, 'Mesa'),0)
		self.assertEqual(HashChain.put(HashTable, 'Tonto Basin'),0)
		self.assertEqual(HashChain.put(HashTable, 'Mammoth'),0)
		self.assertEqual(HashChain.put(HashTable, 'Sedona'),0)
		self.assertEqual(HashChain.put(HashTable, 'Sun Valley'),0)
		self.assertEqual(HashChain.put(HashTable, 'Thatcher'),0)
		self.assertEqual(HashChain.put(HashTable, 'San Manuel'),0)
		self.assertEqual(HashChain.put(HashTable, 'Yuma'),0)
		self.assertEqual(HashChain.put(HashTable, 'Sells'),0)
		self.assertEqual(HashChain.put(HashTable, 'Tucson'),0)
		self.assertEqual(HashChain.put(HashTable, 'Snowflake'),0)
		self.assertEqual(HashChain.get(HashTable,'Globe'), 0)
		self.assertEqual(HashChain.get(HashTable,'Sun Valley'),0)
		self.assertEqual(HashChain.get(HashTable,'Clayton'),-1)
		
		#print('HashTable result after test_get')
		#self.assertEqual(HashChain.display(HashTable), None)
		for i in HashTable:
			i.clear()

	def test_delete(self):

		self.assertEqual(HashChain.put(HashTable, 'Mesa'), 0)
		self.assertEqual(HashChain.put(HashTable, 'Globe'),0)
		self.assertEqual(HashChain.put(HashTable, 'Flagstaff'),0)
		self.assertEqual(HashChain.put(HashTable, 'Queen Creek'),0)
		self.assertEqual(HashChain.put(HashTable, 'Goodyear'),0)
		self.assertEqual(HashChain.put(HashTable, 'Mesa'),0)
		self.assertEqual(HashChain.put(HashTable, 'Tonto Basin'),0)
		self.assertEqual(HashChain.put(HashTable, 'Mammoth'),0)
		self.assertEqual(HashChain.put(HashTable, 'Sedona'),0)
		self.assertEqual(HashChain.put(HashTable, 'Sun Valley'),0)
		self.assertEqual(HashChain.put(HashTable, 'Thatcher'),0)
		self.assertEqual(HashChain.put(HashTable, 'San Manuel'),0)
		self.assertEqual(HashChain.put(HashTable, 'Yuma'),0)
		self.assertEqual(HashChain.put(HashTable, 'Sells'),0)
		self.assertEqual(HashChain.put(HashTable, 'Tucson'),0)
		self.assertEqual(HashChain.put(HashTable, 'Snowflake'),0)

		self.assertEqual(HashChain.deleEntry(HashTable,'Globe'), 0)
		self.assertEqual(HashChain.deleEntry(HashTable,'Sun Valley'),0)
		self.assertEqual(HashChain.deleEntry(HashTable,'Clayton'),-1)

		#print('HashTable result after test_get')
		#self.assertEqual(HashChain.display(HashTable), None)

		for i in HashTable:
			i.clear()



if __name__ == '__main__' :
	unittest.main()