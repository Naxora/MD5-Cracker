#!/usr/bin/python 
# Author Naxora <https://github.com/Naxora>

import hashlib
import optparse	

def main():
	parser = optparse.OptionParser("usage %prog "+"-f <pwd_file> "+"-x <md5_hash>")
	parser.add_option('-f', dest='pname', type='string', help='specify password file')
	parser.add_option('-x', dest='x', type='string', help='specify md5 hash string')
    	(options, args) = parser.parse_args()
	if (options.pname == None) | (options.x == None):
        	print parser.usage
        	exit(0)
    	else:
        	pname = options.pname
		x = options.x
		
	with open(pname, "r") as myfile:
		for line in myfile:
			m = hashlib.md5()
			m.update(line.rstrip())
			m.hexdigest()
			print "[+]Check: "+ x + " ---> " + hashlib.md5(line.rstrip()).hexdigest()

			if hashlib.md5(line.rstrip()).hexdigest() == x:
				print "---------------------------------------------->"
				print "[*] Found Passwd: " + line
				break
	print "---------------------------------------------->"
	print "[-] Not found password"

if __name__ == '__main__':
	main()



