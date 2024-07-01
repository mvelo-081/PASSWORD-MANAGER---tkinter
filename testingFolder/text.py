def fetchAccountPass():
    username = "MVELOKHUMALO"
    account = "NETFLIX"
    with open(f'listOfClientsAccount\\{username}.txt', 'r') as ff:
        for line in ff:
            if line.startswith(f'{account}'):
                parts = line.split(':')
                StoredPassword = parts[-1]
                
    def dencrypterFun( StoredPassword): # dencrypter -->
        dencrypterPass = ''
        for char in StoredPassword:
            dencrypterPass += chr(ord(char) % 33 - 33)
        return dencrypterPass
    
    print(StoredPassword)


fetchAccountPass()