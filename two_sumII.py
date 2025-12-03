l1=[10,23,24,34,45,56,67,76]
target=90
s=0
e=len(l1)-1
while s<e:
  cur_sum=l1[s]+l1[e]
  if cur_sum>target:
    e-=1
  elif cur_sum<target:
    s+=1
  else:
    print(s+1, e+1)
    break
  