import string
import random

st = input("Enter string:")
words = st.split(" ")
coding = input("1.for Coding 2.for Decoding: ")
coding = True if (coding == "1") else False
num = 3
if (coding):
  nword = []

  for word in words:
    if (len(word) >= 3):
      r1 = ''.join(random.choices(string.ascii_lowercase, k=num))
      r2 = ''.join(random.choices(string.ascii_uppercase, k=num))
      stnew = r1 + word[1:] + word[0] + r2
      nword.append(stnew)

    else:
      nword.append(word[::-1])
  print(" ".join(nword))
else:
  nword = []
  for word in words:
    if (len(word) >= 3):
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      nword.append(stnew)
    else:
      nword.append(word[::-1])
  print(" ".join(nword))
