# write your code here
for x in range(1, 11):
    f = open(f"file{x}.txt", "w")
    f.write(f"{x}")
    f.close()
