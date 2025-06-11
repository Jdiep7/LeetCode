import re
s = "Was it a car or a cat I saa?"

lowercase_text = s.lower()
cleanString = re.sub('[^A-Za-z0-9]+', '', lowercase_text)
palindrome = list(cleanString)
n = len(palindrome)
print(palindrome)
for i in range(n // 2):
    print(n //2)
    if palindrome[i] != palindrome[n-1-i]:
        print(False)
        break
