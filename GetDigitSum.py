import math

months = [31,29,31,30,31,30,31,31,30,31,30,31]

def convert(n):
  if n == 1:
    return 1
  n = float(n)
  ret = 0
  exp = math.ceil(math.log10(n))
  exp = int(exp)
  for i in range(1,exp+1):
    ret = ret + (n % pow(10,i))/pow(10,i-1)
    n = n - (n % pow(10,i))
  return ret

sum = 0

for i in range(1,12):
  for day in range(1,months[i]):
    sum += convert(i) + convert(day) + convert(2016)

print(sum)

#convert function finds the sum of the digits of a number (convert(2016) returns 9)
