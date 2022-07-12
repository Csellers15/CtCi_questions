def isUniqueCharacter(str):
	if len(str) > 128: 
		return False
	
	char_set = [False] * 128
	for char in str:
		val = ord(char)
		if char_set[val]:
			return False
		char_set[val] = True
	
	return True

def isUniqueCharacterUsingDictionary(str):
	character_counts = {}

	for char in str: 
		if char in character_counts: 
			return False
		character_counts[char] = 1
	
	return True

def main():
	test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]

	for test, expected in test_cases: 
		result = isUniqueCharacter(test)

	if result == expected:
		print("Array Pass")
	else: 
		print("Array Fail")

	for test, expected in test_cases: 
		result = isUniqueCharacterUsingDictionary(test)

	if result == expected:
		print("Dictionary Pass")
	else: 
		print("Dictionary Fail")


if __name__ == "__main__":
	main()
