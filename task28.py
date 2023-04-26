# Дана строка (возможно, пустая), состоящая
# из букв A-Z: 
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB
# BBBBBBBBBBBBBBBBBBBBBBBB

# Нужно написать функцию RLE,
# которая на выходе даст строку вида:

# A4B3C2XYZD4E3F3A6B28

# И сгенерирует ошибку, если на вход пришла
# невалидная строка.

# Пояснения: Если символ встречается 1 раз,
# он остается без изменений; Если символ
# повторяется более 1 раза, к нему
# добавляется количество повторений.

def RLE(string: str) -> str: 
    
    out_string: str = str()
    count = 1
    current_str = str()
    for el in (string + " "): 
        if current_str != "":
            if current_str == el:
                count += 1
            else:
                if count != 1:
                    out_string += current_str + str(count)
                    count = 1
                    current_str = el
                else: 
                    out_string += current_str
                    count = 1
                    current_str = el
        else:
            current_str = el
    return out_string
    
print(RLE("AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"))