

def accum(s, n=0, ret=''):
    for letter in s:
        ret += (letter + letter*n).title()
        if n+1 != len(s): ret += '-'
        n+=1
    print(ret)
    return ret

accum("abcd") # -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") # -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") # -> "C-Ww-Aaa-Tttt"
accum("ZpglnRxqenU")
