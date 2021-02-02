import numpy as np
import random
genetic_population=np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])

for  i in range (1000):
    lens=len(genetic_population)####个体数
    len_chrom=len(genetic_population[0])###染色体长度
    #print(len_chrom)
    male1=random.randint(0,int((lens)*0.5)-1)
    male2=male1+1
    female1=random.randint(0,int((lens)*0.5)-1)
    female2=female1+1
    #i=1##0为第0个个体和第一个交换，1为第一个和第二个交换
    change_point_male =random.randint(0,len_chrom+1)
    change_point_female =random.randint(0,len_chrom+1)
    ##父本
    temp1 = []
    temp2 = []
    temp1.extend(genetic_population[male1][0: change_point_male])
    temp1.extend(genetic_population[male2][change_point_male:])
    temp2.extend(genetic_population[male2][0: change_point_male])
    temp2.extend(genetic_population[male1][change_point_male:])
    temp1=np.array(temp1)
    temp1=temp1.reshape(1,-1)
    temp2=np.array(temp2)
    temp2=temp2.reshape(1,-1)
    if random.random()>0.5:
        temp=temp1
    else:
        temp=temp2
    genetic_population = np.r_[genetic_population,temp]
    ###母本
    temp1 = []
    temp2 = []
    temp1.extend(genetic_population[male1][0: change_point_female])
    temp1.extend(genetic_population[male2][change_point_female:])
    temp2.extend(genetic_population[male2][0: change_point_female])
    temp2.extend(genetic_population[male1][change_point_female:])
    temp1=np.array(temp1)
    temp1=temp1.reshape(1,-1)
    temp2=np.array(temp2)
    temp2=temp2.reshape(1,-1)
    if random.random()>0.5:
        temp=temp1
    else:
        temp=temp2
    genetic_population = np.r_[genetic_population,temp]

print(genetic_population)
lens=len(genetic_population)
for i in range(int((lens)*0.5)-1):
    #print(genetic_population[i],genetic_population[i+1])
    list=[]
    for each in range(len_chrom):
        if genetic_population[i][each]==genetic_population[i+1][each] and genetic_population[i+1][each]==0:
            list.append('pur')
        if genetic_population[i][each]==genetic_population[i+1][each] and genetic_population[i+1][each]==1:
            list.append('out')
        if genetic_population[i][each]==0 and genetic_population[i+1][each]==1:
            list.append('mix')
        if genetic_population[i][each]==1 and genetic_population[i+1][each]==0:
            list.append('mix')
    print(list)
    del list
