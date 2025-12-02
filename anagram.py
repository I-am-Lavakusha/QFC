from collections import Counter
def is_anagram(s1, s2):
  if len(s1)!=len(s2):
    return False
  s1=list(s1)
  s2=list(s2)
  for i in s1:
    if i in s2:
      s2.remove(i)
  if not s2:
    return True
  else:
    return False

  # return sorted(s1)==sorted(s2)

  # if len(s1)!=len(s2):
  #   return False
  # counts, countt={}, {}
  # for i in range(len(s1)):
  #   counts[s1[i]]=1+counts.get(s1[i], 0)
  #   counts[s2[i]]=1+countt.get(s2[i], 0)

  # for c in counts:
  #   if counts[c]!=countt.get(c, 0):
  #     return False
  # return True

  # return Counter(s1)==Counter(s2)

s1=input("enter the string1: ")
s2=input("enter the string2: ")
print(is_anagram(s1, s2))