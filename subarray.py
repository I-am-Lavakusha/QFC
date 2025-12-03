l1=[2,34,2,532,5,2343,52,-4,6,-5,45,-1]
sub_arr=l1[0]
cur_sum=0
for i in l1:
  if cur_sum<0:
    cur_sum=0
  cur_sum+=i
  sub_arr=max(cur_sum, sub_arr)
print(sub_arr)