def palindrome(word):
	list_word=list(word)
	list_word_rev=list_word[:]
	list_word_rev.reverse()
	print(list_word, list_word_rev)
	return (list_word==list_word_rev)

word="level"
print(palindrome(word))
