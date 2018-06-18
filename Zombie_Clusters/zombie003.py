


def zombieCluster(zombies):

    N = int(zombies[0])
    print(N)
    '''
    int[][] M = new int [N][N];
    for(int i = 0; i<N; i++) {
        for (int j = 0 ; j<N; j++) {
            M[i][j] = Integer.parseInt(zombies[i + 1].charAt(j) + "");
        }
    }
    '''
    zombies = zombies[1:]
    print(zombies)
    M = [['']*N]*N
    #print(M)
    
    for i in range(0,N):
        for j in range(0,N):
            M[i][j] = zombies[i][j]
    
    
    print(M)
    
    visited = [False] * N
    visiting = [False] * N
    #boolean visited[] = new boolean[N];
    #boolean visiting[] = new boolean[N];
    
    #print(visited)
    #print(visiting)
    
    
    count = 0;
    for i in range(0,N):
        if(not visited[i]):
            visiting[i] = True
            DFS(M, N, visited, visiting, i)
            visited[i] = True
            count += 1
    
    return count

    

def DFS(M, N, visited, visiting, s):
    if( not visited[s] ): 
        visiting[s] = True
        for j in range(s+1,N):
        #for(int j = s+1; j < N; j++) {
            if(M[s][j] == 1 and not visited[j]):
                visiting[j] = True
                DFS(M, N, visited, visiting, j)
                visited[j] = True
            
strings = ["7",
            "1100001",
            "1110001",
            "0110001",
            "0001100",
            "0001100",
            "0000010",
            "0010001"]

count = zombieCluster(strings)
print(count)
