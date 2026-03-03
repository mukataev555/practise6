f = open("demofile.txt", "r")

print(f.read())

print("\t")
with open("demofile.txt") as f:
  print(f.read())  #Using with statement

f = open("demofile.txt")
print(f.readline())
f.close()

with open("demofile.txt", "r") as f:
  print(f.read(5))

with open("demofile.txt") as f:
  print(f.readline())

with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())

print ("\t")
with open("demofile.txt") as f:
  for x in f:
    print(x)


