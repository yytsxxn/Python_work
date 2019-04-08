#1_abs()获取绝对值
print( abs(-2) )
print( abs(3+4j) )

#2_all()接受一个迭代器，如果迭代器的所有元素都为真，那么返回True，否则返回False
s1=["yyt","真可爱","222"]
print( all(s1) )
s2=["yyt","真可爱","222",0]
print( all(s2) )

#3_any()接受一个迭代器，如果迭代器里有一个元素为真，那么返回True,否则返回False
s3=[False,0]
print( any(s1) )
print( any(s2) )
print( any(s3) )

#4_ascii()返回一个可打印的对象字符串方式表示。
# 当遇到非ASCII码时，就会输出\x，\u或\U等字符来表示。
print(ascii(10),ascii(999999),ascii("a"),ascii("abc"),ascii("b\31"),ascii("0x\1000"))

#5_bin()返回一个整数 int 或者长整数 long int 的二进制表示。
print( bin(10) )

#6_oct()函数将一个整数转换成8进制字符串
print( oct(10) )

#7_hex()函数将一个整数转换成16进制字符串
print( hex(10) )

#8_ bool()函数测试一个对象是True还是False
print( bool(12345) )
print( bool(0) )

#9_bytes()函数将一个字符串转换成字节类型
s4="我 要 学  Python!"
print( bytes(s4,encoding="utf-8") )

#10_str()函数将字符类型/数值类型等转换为字符串类型
print( str(b"\xe6\x88\x91 \xe8\xa6\x81 \xe5\xad\xa6  Python!",encoding="utf-8"))

#11_callable(object)函数用于检查一个对象是否是可调用的。
# 如果返回True，object仍然可能调用失败；
# 但如果返回False，调用对象ojbect绝对不会成功。
print(callable(str()))
print( callable(max) )

#12_chr()函数用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
print( chr(0) )
print( chr(258) )
print( chr(90) )
print( chr(233) )

#13_ord()函数返回对应的 ASCII 数值，或者 Unicode 数值
print( ord("A") )
print( ord("a") )


