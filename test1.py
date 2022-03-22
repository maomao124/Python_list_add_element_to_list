"""
 * Project name(项目名称)：Python_list列表添加元素
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/22 
 * Time(创建时间)： 10:35
 * Version(版本): 1.0
 * Description(描述)： 
 """

if __name__ == '__main__':
    # 使用+进行连接
    language = ["Python", "C++", "Java"]
    birthday = ["1991", "1998", "1995"]
    info = language + birthday
    print("language =", language)
    print("birthday =", birthday)
    print("info =", info)
    # Python append()方法添加元素
    language.append("C")
    print(language)
    # 追加元组，整个元组被当成一个元素
    t = ('JavaScript', 'C#', 'Go')
    language.append(t)
    print(language)
    # 追加列表，整个列表也被当成一个元素
    language.append(['Ruby', 'SQL'])
    print(language)
    # append() 方法传递列表或者元组时，此方法会将它们视为一个整体，作为一个元素添加到列表中，从而形成包含列表和元组的新列表。

    # Python extend()方法添加元素
    # extend() 和 append() 的不同之处在于：extend() 不会把列表或者元祖视为一个整体，而是把它们包含的元素逐个添加到列表中。
    language.extend("java")
    print(language)
    i = ["java", "C"]
    language.extend(i)
    print(language)
    # 追加元组，元祖被拆分成多个元素
    t = ('JavaScript', 'C#', 'Go')
    language.extend(t)
    print(language)

    # Python insert()方法插入元素
    # listName.insert(index , obj)
    # 其中，index 表示指定位置的索引值。insert() 会将 obj 插入到 listname 列表第 index 个元素的位置。
    l = ['Python', 'C++', 'Java']
    # 插入元素
    l.insert(2, 'C')
    print(l)
    # 插入元组，整个元祖被当成一个元素
    t = ('C#', 'Go')
    l.insert(2, t)
    print(l)
    # 插入列表，整个列表被当成一个元素
    l.insert(3, ['Ruby', 'SQL'])
    print(l)
    # 插入字符串，整个字符串被当成一个元素
    l.insert(0, "hello")
    print(l)

    input()
