import pdb

def subsets(arr):
    if len(arr) == 0:
        return [[]]
    first = arr[0]
    remaining = arr[1:]
    without_first = subsets(remaining)
    with_first = [ [first] + subset for subset in without_first]
    return without_first + with_first

print(subsets([1,2,3]))                                  

# 当n=5时
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

factorial(5)
# 1. 假设第一次进入factorial(5)函数，n=5，不等于1，所以执行else语句，返回5*factorial(4)的值
# 2. 假设第二次进入factorial(4)函数，n=4，不等于1，所以执行else语句，返回4*factorial(3)的值   
# 3. 假设第三次进入factorial(3)函数，n=3，不等于1，所以执行else语句，返回3*factorial(2)的值      
# 4. 假设第四次进入factorial(2)函数，n=2，不等于1，所以执行else语句，返回2*factorial(1)的值
# 5. 假设第五次进入factorial(1)函数，n=1，等于1，所以执行if语句，返回1