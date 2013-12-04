from ElectionSimulation.Models.PStation import *
from ElectionSimulation.Models.CTract import *
from ElectionSimulation.Models.Expenses import *
from ElectionSimulation.Models.Link import *

def list_data():
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

def insert_data():
    expenses_list, ctracts_list, pstation_list, links_list = list_data()
    for row in expenses_list:
        p = Expenses(cand_num = row[0], expense = row[1], expense_ceiling = row[2])
        p.save()

    for row in ctracts_list:
        p = CTract(ctuid = row[0], age_1 = row[1], age_2 = row[2], age_3 = row[3], age_4 = row[4], age_5 = row[5], age_6 = row[6], age_7 = row[7], age_8 = row[8], age_9 = row[9], age_10 = row[10])
        p.save()

    for row in pstation_list:
        p = PStation(pd_num = row[0], tot_votes = row[1], cand_num = row[2], votes = row[3])
        p.save()

    for row in links_list:
        p = Link(pd_num = row[0], ctuid = row[1])
        p.save()

