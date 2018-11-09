fo = open("test.txt", "r");
# fo.write("Python is a great language.\nYeah its great!!\n");
str1 = fo.read(300)
print("read string is->>>> ", str1)
print("Name of the file", fo.name)

fo.close()
