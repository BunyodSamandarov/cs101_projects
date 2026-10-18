batteries = [25, 80, 95, 60]
amount = int(input("Enter a number charging amounnt: "))
new = int(input("Enter level of new device: "))


for i in range(len(batteries)):
    batteries[i] = batteries[i] + amount
    if batteries[i] > 100:
        batteries[i] = 100
    else:
        batteries[i] = batteries[i]

d = batteries.pop()
print(f"Disconnected device: {d}")
batteries.append(new)
print(f"Battery levels: {batteries[:]}")          
