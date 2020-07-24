
print('The IP of the server is?')
server = input('Enter in ip address ')
port1 = int(input('The server start port is? '))
port2 = int(input('The server end port is? '))
while port1 <= port2:
    print('server  {} : {}'.format(server, port1))
    port1 += 1  # increase port1 by 1
