text = open("text.txt", "r")
read = text.read()
count_str = read.count("\n") + 1
print(read)
text = open("text.txt", "r")
read = text.read()
read = read.split()
print(f"Количество слов: {len(read)}")
print(f"Количество строк: {count_str}")
