days = int(input("Enter days"))
empty = []
for i in range(1, days+1):
    
    height = int(input("Enter heights: "))
    empty.append(height)
    print(f"Day {i}: {height} cm")
    
print(f"First height: {empty[0]} cm")
print(f"Last height: {empty[-1]} cm")
print(f"Change: {empty[-1] - empty[0]} cm")
