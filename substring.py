'''
To find small string inside a larger string
worst case would be still O(m*n) but only if hash map is very bad
else it would be linear.

'''

long_str = "Hello, world this is a long string"
sub_str  = "world"
hash_sub_str = 0

hash_sum = [0]*len(long_str)
hash_val = [0]*len(long_str)

for i in range(0, len(sub_str)):
    hash_sub_str+= ord(sub_str[i])
print(hash_sub_str)

for index,val in enumerate(long_str):
    hash_val[index] = ord(val)

for i in range(0, len(sub_str)):
    hash_sum[0] += hash_val[i]
    if(hash_sum[0] == hash_sub_str):
        print(0)
print(hash_sum)
for i in range(1, (len(long_str) - len(sub_str) ) ):
        hash_sum[i] = hash_sum[i-1] - hash_val[i-1] + hash_val[i+ len(sub_str)-1]
        if(hash_sum[i] == hash_sub_str):
            print(i)
            # Have to check again since there might be duplicate hash values
            # Two identical strings will have same hash values, vice versa not true.
            break
print(hash_sum)
