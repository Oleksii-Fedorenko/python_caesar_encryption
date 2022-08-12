def shift(symb, num):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    symb_index = abc.find(symb.lower())
    if symb_index + num > 25:
        if symb.lower() == symb:
            return abc[symb_index + num - 26]
        else:
            return abc[symb_index + num - 26].upper()
    else:
        if symb.lower() == symb:
            return abc[symb_index + num]
        else:
            return abc[symb_index + num].upper()


def length(word):
    count = 0
    for char in word:
        if char.isalpha():
            count += 1
    return count


text = input().split()
new_word = ''
new_text = []
for word in text:
    new_word = ''
    word_len = length(word)
    for char in word:
        if char.isalpha():
            new_char = shift(char, word_len)
            new_word += new_char
        else:
            new_char = char
            new_word += new_char
    new_text.append(new_word)
print(*new_text, sep=' ')


#Gdb, qmgi. "Ciev" ku b tpzahrl!
#oa reqi ku Veznut!
#Vq dg, qt qrw vq dg, xlex ku wkh ycmabqwv

