
def compare(a, b):
  a = str(a)
  b = str(b)
  if a[0] > b[0]:
    return 1 
  elif a[0] < b[0]:
    return -1 
  else:
    if len(a) > len(b):
      return compare(a, b + b[0])
    elif len(a) < len(b):
      return compare(a + a[0], b)
    else:

      return 0

def sort(nums):
  for i in range(len(nums) - 1):
    for j in range(len(nums) - i - 1):
      if compare(nums[j], nums[j+1]) == -1:
        nums[j], nums[j+1] = nums[j+1], nums[j]
  return nums

def max_number(nums):
  nums = sort(nums)
  result = ""
  for num in nums:
    result += str(num)
  print(result)

nums = [3, 30, 34, 5, 9]
max_number(nums)