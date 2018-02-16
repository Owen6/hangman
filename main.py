import random

with open('sowpods.txt') as f:
	words = list(f)

word = (random.choice(words).strip())
blanks = []
for j in range(len(word)):
	blanks.append('_')

#print(word)
x = 0
y = 0
guessedRight = []
guessedWrong = []
while x < len(word):
	print ''.join(map(str, blanks))
	guess = (raw_input('Guess a Letter ')).upper()
	for i in range(0, len(word)):
		if guess == word[i] and not i in guessedRight:
			guessedRight.append(guess)
			x = x + 1
			blanks[i] = guess
			
		elif not guess in guessedWrong and guess != word[i]:
			guessedWrong.append(guess)
print(guessedWrong)
print(guessedRight)
for j in range(0,len(guessedRight)):
	for k in range(0,len(guessedWrong)):
		if guessedWrong[k] == guessedRight[j]:
			del guessedWrong[k]
		else:
			y = y


	if y == 1:
		print('o')
	elif y == 2:
		print(' o ')
		print('-|-')
	elif y == 3:
		print(' o ')
		print('-|-')
		print(" /\\")
print(word)
print(guessedWrong)