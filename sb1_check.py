try:
    with open('/root/sysadmin/online.txt', 'r') as f:
        try:
            res = f.read()
            if res == 'online\n':
                print(0)
        except:
            print(1)

except:
    '''cant read online.txt file'''
    print(2)
