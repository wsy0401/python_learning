# --*-- coding: utf-8 --*--

######这里做的是fast integer数据的编码操作
def fast_uint_encoder(data_decoded):
    divident = data_decoded #被除数
    divisor = 0x80 #除数
    Quotient =divident // divisor
    Remainder = divident%divisor
    fast_encode_integer=[]
    result = ""
    while Quotient > 0:
        Quotient = divident // divisor
        Remainder = divident % divisor
        fast_encode_integer.insert(0,Remainder)
        divident = Quotient
    if  divident > 0  and fast_encode_integer[0] > 0x40 :
        fast_encode_integer.insert(0,0)
#这里尝试过hex(fast_encode_integer[i]),会多出来0x
#str(fast_encode_integer[i]),只是将整形数变成一个str(如32转为'32'，正确的是把32转成16进制的值20,再变成'20')
#format可以实现这个功能，前提需要填那个str'{:02x}'
    for i in range(len(fast_encode_integer)) :
        if i == (len(fast_encode_integer) - 1):
            result = result + '{:02x}'.format(fast_encode_integer[i]+0x80)
        else :
            result = result + '{:02x}'.format(fast_encode_integer[i])
    return result

#这里做的是fast integer数据的解码操作
def fast_uint_decoder(data_encoded):
    fast_data=data_encoded
    result = 0
    #int(x,base)用于把一个字符或者数字转为整形,这里的base是指x是什么进制的值
    for i in range(0,len(fast_data)-1,2):
        if i == len(fast_data) - 2 :
            temp = int(fast_data[i:i+2],16) - 0x80
        else: 
            temp = int(fast_data[i:i+2],16)
        result = result * 0x80 + temp
#    print("%d" % (result - 1))
    return result
