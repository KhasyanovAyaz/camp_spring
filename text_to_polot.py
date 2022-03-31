from text_file_reading import read_with_split
import matplotlib.pyplot as plt

temp = read_with_split('txt.git2', '\n')
temp_int = []
days = []
i = 1
for elem in temp:
    temp_int.append(int(elem))
    days.append(i)
    i += 1
print(days)
plt.plot(days, temp_int)
plt.show()