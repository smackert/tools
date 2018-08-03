import hashlib
import io
import sys



if (len(sys.argv) != 2):
	print("Usage: appendnull.py <filename>")
	sys.exit(1)

f = sys.argv[1]

def readFile(file):
	try:
		data = io.open(file, "rb").read()
		return data
	except:
		print("Failed to read file.")
		sys.exit(1)

def appendNull(file):
	try:
		f = io.open(file, "ab")
		f.write(bytearray(1))
		f.close()
	except:
		print("Failed writing null byte.")
		sys.exit(1)

def getHash(file):
	try:
		data = readFile(file)
		# print(data)
		hashsum = hashlib.md5()
		hashsum.update(data)	
		return hashsum.hexdigest()
	except:
		print("Failed to get hash.")
		sys.exit(1)

oldHash = getHash(f)
appendNull(f)
newHash = getHash(f)

print("Old hash:", oldHash)
print("New hash:", newHash)