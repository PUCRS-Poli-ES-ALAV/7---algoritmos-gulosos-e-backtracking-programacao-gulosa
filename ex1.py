
#coins = [100, 25, 10, 5, 1]
coins = [1, 0.25, 0.10, 0.05, 0.01]
def change(x):
    x = x
    change = []
    for coin in coins:
        count = 0
        if x <= 0: return change
        print(coin)
        while x >= coin: #and x > 0:
            print(f"{x} - {coin} = {x-coin}") 
            x =  x - coin
            count += 1
        print(x)
        change.append((count, coin))
    
    return change


print(change(2.40))
