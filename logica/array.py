'''
Dado um array de inteiros nums e um inteiro target,
retorne os índices de dois números que somados sejam iguais ao target.
Você pode assumir que existirá exatamente uma solução possível e que você não pode usar o mesmo elemento duas vezes.
Você pode retornar a resposta em qualquer ordem.
Ex 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Como nums[0] + nums[1] == 9, retornamos [0, 1].

Ex 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Ex 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''

nums = [2,7,11,15]
target = 9

for x in range(len(nums)):
  for y in range(len(nums)):
    if x != y and nums[x] + nums[y] == target:
      print(x, y)