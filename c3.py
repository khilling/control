filename = input('tell me the name: ')
censorship = input('and the words for censorship: ').split()
file1 = open(filename, encoding = 'utf-8')
file2 = open('censored.txt', 'x', encoding = 'utf-8')
for line in file1:
    flag = True
    for item in censorship:
        if item in line.split():
            flag = False
            break
    if flag:
        file2.write(line)
print('censored.txt', ' - this is the right file', '\n', filename, ' is not useful anymore', sep = '')


file1.close()
file2.close()