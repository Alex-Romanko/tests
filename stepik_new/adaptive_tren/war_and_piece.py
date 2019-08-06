war_string =str(input())
wars_string = war_string.upper().split( )
set_wars = set(wars_string)
n = 0
val = ''
list_war = []
for i in set_wars:
    val = i
    n = wars_string.count(i)
    list_war.append(str(val + ' ' + str(n)))
for i in list_war:
    print(i)


