def urlify(str, length):
	"Replace spaces with %20 and remove trailing spaces"

	# Convert to a list since strings are immutable in python 
	char_list = list(str)
	new_index = len(char_list)

	for i in reversed(range(length)):
		if char_list[i]== " ":
			char_list[new_index - 3: new_index] = "%20"
			new_index -= 3
		else: 
			char_list[new_index - 1] = char_list[i]
			new_index -= 1

	return "".join(char_list[new_index:])


def main(): 
	test_cases = {
        ("much ado about nothing      ", 22): "much%20ado%20about%20nothing",
        ("Mr John Smith       ", 13): "Mr%20John%20Smith",
        (" a b    ", 4): "%20a%20b",
        (" a b       ", 5): "%20a%20b%20",
    }

	for args, result in test_cases: 
		value = urlify(*args)

		if(value == result): 
			print("urlify passed")
		else: 
			print("urlify failed")

if __name__ == "__main__":
	main()
