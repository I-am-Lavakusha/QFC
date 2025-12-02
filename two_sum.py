l1=[2,4,24,5,2,423,5]
target=28
search={}
for i, val in enumerate(l1):
  diff=target-val
  if diff in search:
    print([search[diff], i])
    break
  search[val]=i