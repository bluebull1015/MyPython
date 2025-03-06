import re
addressList = [
    "('강원원주시웅비2길8');",
    "('강원도철원군서면와수로181번길7-16');",
    "('강원평창군봉평면태기로68');",
    "('강원강릉시강변로410번길36');"
]

regex = "\d\S*\'"
pattern = re.compile(regex)

for address in addressList:
    myMatch = pattern.search(address)
    # print(myMatch.group().rstrip("'"))
    print(myMatch.group().replace("'",""))
#end for