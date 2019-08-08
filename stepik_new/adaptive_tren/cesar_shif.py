shift_letter = int(input())
users_text = str(input().strip())
alphobet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
q = len(users_text)
users_text_list = []
for i in range(q):
    users_text_list.append(users_text[i])
output_message = []
q=0
for i in users_text_list:
    q = alphobet.index(i) +shift_letter
    while q >= 27:
        q = q - 27
    while q <= -27:
        q = q + 27
    output_message.append(alphobet[q])
result = ''
for i in output_message:
    result +=i
print ('Result: "' + result + '"')