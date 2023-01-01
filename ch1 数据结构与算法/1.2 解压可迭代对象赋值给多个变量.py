# 问题
# 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 那么怎样才能从这个可迭代对象中解压出 N 个元素出来？

# 解决方案
# Python 的星号表达式可以用来解决这个问题。比如，你在学习一门课程，在学期末的时候， 你想统计下家庭作业的平均成绩，
# 但是排除掉第一个和最后一个分数。如果只有四个分数，你可能就直接去简单的手动赋值， 但如果有 24 个呢？这时候星号表达式就派上用场了：
from numpy import mean

def drop_first_last(grads):
    first, *middles, last = grads
    return mean(middles)

# 另外一种情况，假设你现在有一些用户的记录列表，每条记录包含一个名字、邮件，接着就是不确定数量的电话号码。 你可以像下面这样分解这些记录：
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

# 值得注意的是，星号表达式在迭代元素为可变长元组的序列时是很有用的。 比如，下面是一个带有标签的元组序列：
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)


# 星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

# 如果你够聪明的话，还能用这种分割语法去巧妙的实现递归算法。比如：
def sum(items):
    head, *tail = items
    # print(head, tail)
    # print(sum(tail) if tail else head)
    # head + sum(tail)最好加上括号，以免引起歧义，误以为if。。。else只针对sum(tail)
    return (head + sum(tail)) if tail else head


if __name__ == "__main__":
    grads = [1, 2, 3, 4, 5]
    avg_grads = drop_first_last(grads)
    print(avg_grads)
    print(phone_numbers)

    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)

    items = [1, 10, 7, 4, 5, 9]
    print(sum(items))
    items2 = [1]
    print(sum(items2))
