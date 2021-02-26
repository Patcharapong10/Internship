
print("Internship")
x = int(input("Enter you number : "))

word = []
for i in range(x) :
    letterinit = ''
    letter = input('Input your word : ')
    letter_ = letter.split(' ')
    for n in letter_:
        if(n[0].isupper):
            letterinit += n[0]
    word.append(letterinit)

word.sort(key=lambda item: (-len(item), item))
#word.sort(reverse=True)
for j in word:
    print(i)
    #print(letter)
print(word)
#print("Hello : " + letter)