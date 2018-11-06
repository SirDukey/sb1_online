import paramiko

client = paramiko.client.SSHClient()
client.load_system_host_keys()

try:
    client.connect('hostname', port=, username='', password='')
    try:
        stdin, stdout, stderr = client.exec_command('cat sysadmin/online.txt', timeout=5)
        if stdout:
            x = stdout.read()
            x = x.decode('ascii')
            if x == 'online\n':
                print(0)
        elif stderr:
            print(1)

    except:
        '''cant read online.txt file'''
        print(2)

    finally:
        client.close()
except:
    '''cant connect'''
    print(3)
