word = input()
alphabet = list(range(97,123)) #아스키코드 숫자 범위(소문자)

for x in alphabet:
    print(word.find(chr(x)),end=" ")
