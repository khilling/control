def partofspeach(file, part, number = ''):                #я использовала словарь частотности
    file = open(file, encoding = 'utf-8')
    f = file.readlines()
    a = []
    for line in f:
        line = line.split('|')
        morpho = line[1].split()
        if morpho[0] == part and (number == '' or (number in morpho)):
            a.append((line[0], ' '.join(morpho)))
    file.close()
    return a


def vowelempty(s, parametr = 'all'):
    length = 0
    if parametr == 'all':
        for i in s:
            length += 1
        return s, length
    else:
        a = ''
        for i in s:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'y' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or i == 'Y':
                a += i
                length += 1
        return a, length
