import re

# 1. 문자 클래스
# \d = [0-9]
# 문자 : [a-z] [A-Z]  => [A-z]
# \w : [a-zA-Z0-9]
# \s whitespace : [ \t\n\r]
# . : 모든문자(\n만 제외)

# 2. 반복
# + : 1 이상 => [0-9]+ : 숫자가 1자리 이상
# * : 0 이상 [0-9]+ : 숫자가 없거나 1자리 이상
# ? : 0 또는 1 : [0-9]? : 숫자가 1자리 없거나 있거나
#
# {x} : x번 반복
# {x, y} : x~y번 반복
# {x, } : x번 이상 반복

# + => {1, } : [0-9]{1,}
# * => {0, } : [0-9]{0,}
# ? => {0,1} :: [0-9]{0,1}

# 3. 검색
# match() : 문자열의 처음부터 정규식과 매치(일지)하는지 확인한다.
# search() : 문자열 전체를 검사하여 정규식과 일치하는지 확인한다.
# findall() : 정규식과 매치되는 모든 문자열(substring)을 리스트로 반환한다.
# finditer() : 정규식과 매치되는 모든 문자열(substring)을 iterator 객체로 반환한다.


# 4. match
# 검색결과를 리턴하는 오브젝트
# 검색결과를 group 메쏘드로 볼 수 있음
# search, finditer로 검색시 사용가능
# group(0) : 검색된 전체
# group(x) : 패턴에서 지정한 그룹 번호
# 그룹지정은 ()로
# ex) "hello\s+(world)" => group(0) 는 전체, group(1)은 world


content = "hello jungil"
p = re.compile("hello\s+(\w+)")
m = p.search(content)
if m:
    print(m.group())
    print(m.group(1))


content = "first line \n second 2 line"
p = re.compile("\w+\s+line", re.MULTILINE)
results = p.findall(content)
print(results)