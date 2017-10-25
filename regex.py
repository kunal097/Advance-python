import re
def main():
	line="I think I understand regular expressions"

	mathchResults = re.match('think' , line ,re.M|re.I)

	if mathchResults:
		print("Match found : "+ mathchResults.group())
	else:
		print("No match found : ")

	searchResults = re.search('think' , line ,re.M|re.I)
	
	if searchResults:
		print("Match found : "+ searchResults.group())
	else:
		print("No match found : ")	

if __name__ == '__main__':
			main()		
		