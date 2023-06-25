"""
mult_table 
Author:25423
Date:2023/6/25
"""
i=1
while i<=9:
    j=1
    while j<=i:
        print('%d*%d=%d'%(i,j,i*j),end='\t')
        j+=1
    print('\n')
    i+=1
