def list():
    '''
    '''
    
    expenses_list = []
    expenses = open('DummyExpense.csv', 'r')
    
    #Skip header
    expenses.readline()
    for line in expenses.readlines():
        expenses_list.append([elem.rsplit("\r\n")[0] for elem in line.split(',')])
    expenses.close()
    
    
    ctracts_list = []
    ctracts = open('DummyCT.csv', 'r')
    
    #Skip header
    ctracts.readline()
    tract = []
    for line in ctracts.readlines():
        tract = line.split(',')
        tract = [tract[0]] + tract[4:-1]
        ctracts_list.append(tract)
    ctracts.close()
    
    
    pstation_list = []
    pstations = open('DummyPS.csv', 'r')
    
    #Skip header
    pstations.readline()
    for line in pstations.readlines():
        pstation_list.append([elem.rsplit("\r\n")[0] for elem in line.split(',')])
    pstations.close()
    
    
    links_list = []
    links = open('DummyLink.csv', 'r')
    
    #Skip header
    links.readline()
    for line in links.readlines():
        links_list.append([elem.rsplit("\r\n")[0] for elem in line.split(',')])
    links.close()
    
    return expenses_list, ctracts_list, pstation_list, links_list




if __name__ == '__main__':
