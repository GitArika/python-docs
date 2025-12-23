# For Loops (Looping)

# Print from 1 to 5

for num in range (1,6): 
  print(num)


print('')
word = 'Home'

for letter in word:
  print(f'{letter} is in the word {word}')

# Send email with buy details [Max 3 attempts] 

buy_data = 'Your course in value of $23.99 is confirmed'

for send_email in range(3):
  print(buy_data)
  break

for x in range(5):
  print(x)
  for y in range(5):
    print(f"Inner {y}")

word  = 'Amazing'
formated_word = ''

for letter in word:
  formated_word += f" {letter}"

print(formated_word.strip())

