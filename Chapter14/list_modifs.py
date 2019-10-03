directory = ["melkor", "oupss", "néluge", "joy", "klem"]
print (id(directory))
directory.append("rulior")
directory.append("mohe")

print (directory)
print (id(directory))

directory_sorted = sorted(directory)
print (directory_sorted)
print (directory_sorted[0])
print (directory_sorted[1])
