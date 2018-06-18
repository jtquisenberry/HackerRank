#!/bin/python3

import sys


def get_zombie_cluster(zombies):
    #var_dump ($zombies)
    print(zombies)
    #print(zombies[1][3])
    #echo $zombies[1][3].PHP_EOL;
    zombie_count = len(zombies)

    print(zombie_count)
    zombie_cluster = []
    for i in range(0,zombie_count):
        zombie_cluster.append(None)
        for j in range(i,zombie_count):
            print(i)
            print(j)
            #print(zombies[i][j])
            if (zombies[i][j]==1):
                pass
                '''zombie_cluster[i][]=j'''
    '''
    #var_dump ($zombie_cluster);
    changed_cluster=1
    while (changed_cluster==1):
        changed_cluster=0
        for i in range(0,zombie_count):
            if (zombie_cluster[i]!=None):
                for k in range(i + 1, zombie_count):
                    for j in range(0,len(zombie_cluster[k])):
                        #echo $i."--".$k."--".$j.PHP_EOL;
                        if ((zombie_cluster[k][j] in zombie_cluster[i])):
                            # echo $k."--".$j."-- Element:".$zombie_cluster[$k][$j]." Found in ".$i.PHP_EOL;
                            zombie_cluster[i] = array_values(array_unique(array_merge(zombie_cluster[i],zombie_cluster[k])))
                            #// print_r(zombie_cluster)
                            zombie_cluster[k]=null
                            changed_cluster=1
                            #echo "Changed..".PHP_EOL;
                            #break 2;

    print_r(zombie_cluster);
    total_zombies=0;
    for i in range(0, zombie_count):
        if (zombie_cluster[i]!=None):
            total_zombies=total_zombies+1
    '''
    #return total_zombies

n=6;
zombies = ["0","0","0","0","0","0"]
zombies[0]="110001";  
zombies[1]="111000";
zombies[2]="011000";
zombies[3]="000110";
zombies[4]="000111";
zombies[5]="100011";
print(get_zombie_cluster(zombies))

#Code ends






'''

if __name__ == "__main__":
    n = int(input().strip())
    genes = input().strip().split(' ')
    health = list(map(int, input().strip().split(' ')))
    s = int(input().strip())
    for a0 in range(s):
        first, last, d = input().strip().split(' ')
        first, last, d = [int(first), int(last), str(d)]
'''