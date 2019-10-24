def numberOfConnections(gridOfNodes):
    # Write your code here
       # Write your code here
    count=0
    c_list=[]
    suml=[]
    if len(gridOfNodes)>=1 or len(gridOfNodes)>=500:
            for g in gridOfNodes:
                if len(g)>=1 or len(g)>=500 and ( g == 0 or g ==1):

                    for i,val in enumerate(g,1):
                        if val == 1  :
                            count +=1
                        if i == len(g):
                                c_list.append(count)
                                count =0
            for m,val in enumerate(c_list):
                    if m+1 < len(c_list):
                        total =c_list[m] * c_list[m+1]
                        if total ==0 and m+2 < len(c_list):
                            total = c_list[m] * c_list[m+2]
                        suml.append(total)
            print (sum(suml))
        
        



numberOfConnections([[1,0,1,1],[0,1,1,0],[0,0,0,0],[1,0,0,0]])
