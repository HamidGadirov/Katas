def solution(c):
    letter = ord(c[0])
    digit = int(c[1])
    moves = [(2, 1), (1, 2), (-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, -2), (2, -1)]
    A = ord('a')
    print(A)
    H = ord('h')
    print(H)
    possible = 0
    for i in moves:
        if A <= i[0] + letter <= H and 1 <= i[1] + digit <= 8:
            print(i[0] + letter, i[1] + digit)
            possible += 1
        else:
            print("no", i[0] + letter, i[1] + digit)
    return possible
    
    # x,y = ord(c[0])-96, int(c[1])
    # return sum([1<=(x+i)<=8 and 1<=(y+j)<=8 for i in [-2,-1,1,2] for j in [-2,-1,1,2]])//2
    
    # r = 0
    # c = [ord(cell[0])-96,int(cell[1])]
    
    # m = [[1,2],[2,1],[1,-2],[-2,1],[-1,2],[2,-1],[-1,-2],[-2,-1]]
    
    # for i in m:
    #     if 0<c[0]+i[0]<9 and 0<c[1]+i[1]<9:
    #         r +=1
    # return r
            
        
    

