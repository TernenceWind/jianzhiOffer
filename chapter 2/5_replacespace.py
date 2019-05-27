# coding = utf-8
# 替换空格

string = 'We are happy.'
rep_o = ' '
rep_d = '%20'


# 1 内置的replace函数
print(string.replace(rep_o, rep_d))


# 2 join
print(rep_d.join(string.split(rep_o)))


