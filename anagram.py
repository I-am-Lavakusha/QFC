from collections import Counter
def is_anagram(s1, s2):
  if len(s1)!=len(s2):
    return False
  counts, countt={}, {}
  for i in range(len(s1)):
    counts[s1[i]]=1+counts.get(s1[i], 0)
    counts[s2[i]]=1+countt.get(s2[i], 0)

  for c in counts:
    if counts[c]!=countt.get(c, 0):
      return False
  return True
  # return Counter(s1)==Counter(s2)

s1=input("enter the string1")
s2=input("enter the string2")
print(is_anagram(s1, s2))