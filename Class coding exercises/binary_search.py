import random


def binary_search(data, target, low, high):
  mid_temporal = len(data) - 1
  pasos = 0

  while mid_temporal > 0:#low <= high: #pasos < (len(data) - 1) // 2:
    pasos += 1
    mid_temporal //= 2
    mid = (low + high) // 2

    if target == data[mid]:
      print(pasos)
      return True
    elif target < data[mid]:
      high = mid - 1
    else:
      low = mid + 1
  
  print(pasos)
  return False

#def binary_search(data, target, low, high):
#  if low > high:
#   return False
#
#  mid = (low + high) // 2
#
#  if target == data[mid]:
#   return True
#  elif target < data[mid]:
#   return binary_search(data, target, low, mid - 1)
#  else:
#    return binary_search(data, target, mid + 1, high)


if __name__== '__main__':
  data = [random.randint(0, 100) for i in range(100)]

  data.sort()

  print(data)

  target = int(input('What number would you like to find'))
  found = binary_search(data, target, 0, len(data) - 1)

  print(found)
