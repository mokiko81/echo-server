import socket
lobound = int(0)
hibound = int(65535)

while True:
    lower = input('Please input the lower bound of ports to check\n>>')
    lower = int(lower)
    if lower < lobound or lower > hibound:
        print('Number out of range, please try again.')
    else:
        break

while True:
    upper = input('Please input the upper bound of ports to check\n>>')
    upper = int(upper)
    if upper < lobound or upper > hibound:
        print('Number out of range, please try again.')
    else:
        break

for i in range(lower, upper):
    try:
        port = socket.getservbyport(i)
        print('Port {} belongs to {}'.format(i, port))
    except:
        pass