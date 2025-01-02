## Finding the Nearest Divisible number

val = int(input())
divisor = int(input())

def num(v,div):
  lower = (v//div)*div
  upper = ((v//div)+1)*div
  if (v-lower) >= (upper-v):
    return upper
  else:
    return lower


print(num(val,divisor))
