class Vertex(object):
	"""docstring for Vertex
	This class is a blueprint of every word in a dictionary.
	It has three datamembers: word, meaning and synonyms"""
	def __init__(self, word, meaning):
		self.word = word
		self.meaning = meaning
		self.synonyms = []

"""wordDict is a hashmap which is storing all the objects. Hashmap will give us O(1) time for lookup. 
We are storing in this form word:object(word,meaning,synonyms)"""
wordDict = {}

#This function is simply adding words
def addWord(word, meaning):
	wordDict[word] = Vertex(word, meaning)

#This function is adding synonyms in each others' synonyms list
def addSynonyms(word1, word2):
	v1 = wordDict[word1]
	v2 = wordDict[word2]

	v1.synonyms.append(word2)
	v2.synonyms.append(word1)

#Simple lookup in hashmap
def getMeaning(word):
	try:
		v = wordDict[word]
		return v.meaning
	except:
		return "Word doesn't exist."

#Function is getting synonyms of the given word by applying DFS on each word in synonym list.
""" Explaination: Assuming k<<n, this function would have worst case complexity of O(k) where k: number of synonyms and n: total number of words 
(atmost k edges in the graph). Although an O(1) lookup can be achieved by maintaining a complete synonym list for each word, my approach  
improves space complexity by avoiding maintaining a very huge dictionary. """
def getSynonyms(word):

	try:
		v = wordDict[word]
		st = [v]
		visited = set()
		while len(st)>0:
			cur = st.pop()
			if cur.word in visited:
				continue
			for i in cur.synonyms:
				st.append(wordDict[i])
			visited.add(cur.word)
		visited.remove(word)
		return list(visited)
	except:
		return ["Word doesn't exist."]

def driver(filePath):
	f = open(filePath)
	lines = f.readlines()

	for line in lines:
		line = line.rstrip()
		# print line
		cmd = line.split(':')
		if cmd[0]=='addWord':
			addWord(cmd[1], cmd[2])
		elif cmd[0]=='addSynonym':
			addSynonyms(cmd[1], cmd[2])
		elif cmd[0]=='lookupWord':
			print cmd[1],":",getMeaning(cmd[1])
		elif cmd[0]=='lookupSynonyms':
			res = getSynonyms(cmd[1])
			s =''
			for i in res:
				s+=i
				s+=','
			print cmd[1],':',s[:-1]
		else:
			print "Invalid Operation"

driver('testFile.txt')


