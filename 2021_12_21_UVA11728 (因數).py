
# 新技巧!!!! 取得因數
def get_divisors(n):
    divisors = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
        i += 1
    return sorted(divisors)



n = 12
divisors = get_divisors(n)
print("Divisors of", n, "=", divisors)
print("Sum of divisors:", sum(divisors))