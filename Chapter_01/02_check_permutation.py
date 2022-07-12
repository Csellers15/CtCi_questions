def checkPermutation(str1, str2):
	if len(str1) != len(str2):
		return False
	
	counter = [0] * 256

	for c in str1:
		counter[ord(c)] += 1
	
	for c in str2: 
		if counter[ord(c)] == 0: 
			return False 
		counter[ord(c)] -= 1
	
	return True

def main(): 
	test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

	for str1, str2, expected in test_cases: 
		result = checkPermutation(str1, str2)

	if result == expected:
		print("Counter Pass")
	else: 
		print("Counter Fail on" + str1 + " "  + str2 + " expected " + str(expected) + " got " + str(result))

if __name__ == "__main__":
	main() 
