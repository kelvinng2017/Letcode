"""
給定一個整數數組 nums 和一個整數目標值 target，請你在該數組中找出 和為目標值 的那 兩個 整數，並返回它們的數組下標。

你可以假設每種輸入只會對應一個答案。但是，數組中同一個元素不能使用兩遍。

你可以按任意順序返回答案。
"""

nums = [2,7,11,5]
traget = 9

nums2 =[]
ans = []
input_act =True
while input_act:
    nums_index = input("請輸入")
    nums_index_int = int(nums_index)
    print(type(nums_index_int))
    nums2.append(nums_index_int)
    if(nums_index_int==0):
        input_act =False
print("nums=",nums2)
traget2 =int(input("輸入目標:"))
print(type(traget2))
print("traget=",traget2)

for num_index_i  in range(len(nums2)):
    print("num_index_i=",num_index_i)
    for num_index_j  in range(num_index_i+1,len(nums2)):
        print("num_index_j=",num_index_j)
        if nums2[num_index_i]+nums2[num_index_j]  == traget2:
            ans.append(num_index_i)
            ans.append(num_index_j)
            print("我在這裡")
            continue

print("ans_index=",ans)



