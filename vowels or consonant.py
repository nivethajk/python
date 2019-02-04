str = input("Input a letter of the alphabet: ")
 if str in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'A', 'E'):
	print("%s is a vowel." % str)
elif str == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % str) 
