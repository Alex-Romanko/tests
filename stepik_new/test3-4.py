'''      
Недавно мы считали для каждого слова количество его вхождений в строку. 
Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.
Напишите программу, которая считывает текст из файла 
(в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, 
сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое 
(можно использовать оператор < для строк).
Слова, написанные в разных регистрах, считаются одинаковыми.

abc a bCd bC AbC BC BCD bcd ABC
abc 3 

'''
a = 'XUbTY TY XTpYdY cU XpUUXZc Zp ZdYUZ bd bppdd cbc bppdd ZY YYZdZ XXUpd XUbTY YbZT T ZpacpTU ZdYUZ ZdYUZ ZpacpTU UTpXZYY pTUbZd TY TcpcTc pbTZbTc pUTcZTbb c caTZX cU UbpXdZY cbc XXUpd Z daYad acYa ZpacpTU XadZpUY UTpXZYY acXapYp Zd YUZ XXUpd ZY TY bTbUZYYpc cXbd bdcda UYTZTTc XUabYdXZZ ZppadZd bd pTccT cXbd XYUYaaTpT Y dUa    X UYTZTTc Yb bXcpUcbdd Ypp da da bUd TpbYbX cbUpY aUYaXdb X da XYdccbXa bUd     XZcXUU apdTTZYT d YbTY dc pTZbbb ccZd dYap YTYa pcccZp dYap apTadUc bYXpccU dYap bYXpccU U dXZbT dTadd UYaXTZ     apTadUc daXbYd daXbYd YZZ bYXpccU aTdbdXTY pcccZp Ubdd YbcZ aTdbdXTY YX dTb    XT  cTacc cTacc pUTTdUUd UpZ ZbdYXXb pdXUYdYcY ppadcUdc ZbdYXXb ZbdYXXb ppadcUdc     ZbdYXXb ZbdYXXb aTYUpTXZa p d dbbd pdXUYdYcY abbpZZ Taap Taap YbXaZ d XaZ X    bbbbpp cp aTYUpTXZa YY ZbdYXXb cTacc dZY pc cUTddYXp cUTddYXp dc T pbbcX pbbcX pbbcX dccbpU YZbZaXaYd YZbZaXaYd pbbcX bXdpUY d pbbcX bXdpUY Ucb     dZapda aTc bXdpUY Ucb pbbcX a bXdpUY TZcpbYbpT pUYXaZbd cYpUYZX YabY pbbcX     Ucb ZcXTTXY ZTU aZbYa bXdpUY a UZbbbUTcU TZcpbYbpT pcTUp Up a dccbpU TYU XXZ    UYZcT Ucb TaXd UpTXUTb Ucb pccdcXXcX XcZ dXY ad dXY ad pUYUbab pbcXbU U aYXUXYpYX cpX ad bpdXYY dUdYb dUdYb bpdXYY dUdYb dUdYb bTaT bbaUc X cZYZcpXaY acc YcUZXY Ub Y     YaUd UcX bUYUdbTp b dUdYb XXYXZp Xb ZcTddccU Zaaaac bbUpYUUX Ypbcp ZcTddccU     cpb cZZYYXXdX TZZ ab X UbdYcp cUcTaY Zaaaac TpX UXXbU bpdXYY XT YY bcp YTTU    UUTb ZZ'
a = sorted(a.upper().split())

list_a_unrep = set()
for i in a:
    list_a_unrep.add(i)

q=0
w=0
d = []
for j in list_a_unrep:
    q = a.count(j)
    d.append([str(q), j])

c = (max(d))
qwer = str(c[1]) + ' ' + str(c[0])
print (qwer)