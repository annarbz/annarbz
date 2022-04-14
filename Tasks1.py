#!/usr/bin/env python
# coding: utf-8

# # Задание 1

# Даны две строки: `s1` и `s2` с одинаковым размером.
# 
# Проверьте, может ли некоторая перестановка строки `s1` “победить” некоторую перестановку строки `s2` или наоборот.
# 
# Строка x может “победить” строку y (обе имеют размер n), если `x[i] >= y[i]` (в алфавитном порядке) для всех i от 0 до n-1.
# 

# ## Ввод

# `abc`
# `xya`

# ## Вывод

# `True`
# 
# ### Исполняемый код записать в ячейку ниже:

# In[4]:


def check(str1, str2):
    s = 0
    for i in range(len(str1)):
        s += ord(str1[i]) - ord(str2[i])
    if s >= 0:
        return True
    else:
        return False
        
str1 = input()
str2 = input()
print(check(str1,str2) or check(str2,str1))


# # Задание 2

# Дана строка `s`, вернуть самую длинную полиндромную подстроку в `s`.

# ## Ввод

# `babad`

# ## Вывод

# `aba` или `bab`

# ## Исполняемый код записывать в ячейку ниже

# In[12]:


string = input()

def invert(string):
    return str(string) == "".join(reversed(string))

if invert(string):
    print(string)
else:
    i=1
    while (i <len(string))and (not invert(string[i:]) and not invert(string[:len(string)-i])):
        i += 1
    if invert(string[i:]):
        print(string[i-1:])
    else:
        print(string[:len(string)-i])


# # Задание 3

# Вернуть количество отдельных непустых подстрок текста, которые могут быть записаны как конкатенация некоторой строки с самой собой (т.е. она может быть записана, как `a + a`, где `a` - некоторая строка).

# ## Ввод

# `aabb`

# ## Вывод

# 2

# ## Исполняемый код записывать в ячейку ниже

# In[ ]:




