
# program to check the ipstatic

ipchk = '192.168.0.1'

# is a string tests as True
if ipchk:
    print('Looks like the IP address was set {}'.format(ipchk))


# alter your script so that the var ipchk is set by the user
ipchk = input('Apply an IP address')
if ipchk:
    print('Looks like the IP address was set to {}'.format(ipchk))


if ipchk == '192.168.70.1':
    print('Looks like the IP address of the Gateway was set: {}. This is not recommended' .format(ipchk))
elif ipchk:
    print('Looks like the IP address was set: {}'.format(ipchk))
else:
    print('You did not provide input')
