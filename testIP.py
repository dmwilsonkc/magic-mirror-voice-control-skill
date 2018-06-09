import ipaddress


utterance = '192. 168. 3. 126'
utterance = utterance.replace(' ', '')

if utterance != '':
    try:
        ipaddress.ip_address(utterance)
        ip = '{"ipAddress": "' + utterance + '"}'
        print(ip)
        url = 'http://' + utterance + ':8080/remote'
        print(url)
    except:
        print('This is not a valid ip address')

print(utterance)
print(url)
