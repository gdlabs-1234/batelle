
import os, os.path, sys

scaled_scores =  ['<1','<1','1','2','5','9','16','25','37','50','63','75','85','91','95','98','99','>99','>99']
n = 0
with open('scaled_scores.csv','w') as ofile:
    start_month = int(input('starting month: '))
    for month in range(start_month,61):
        if n == 99:
            break
        print(f'----- Month: {month} -----------')
        for scaled_score in range(len(scaled_scores)):
            n = int(input(f'M {month} SS {1+scaled_score}: '))
            if n < 0:
                continue
            elif n == 99:
                break
            #print(f'{(month + 0.01*n):0.2f}, {scaled_score+1}s, {scaled_scores[scaled_score]}')
            ofile.write(f'{month + 0.01*n}, {scaled_score+1}, {scaled_scores[scaled_score]}\n') 
                  
