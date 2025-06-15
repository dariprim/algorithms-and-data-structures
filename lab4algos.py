g=(("a","b",6),("a","h",2),("b","c",9),("b","g",5),("b","h",1), ("c","d",12), ("c","f",8),("c","g",3), ("d","e",4),("d","f",3),("e","f",8),  ("f","g",4), ("h","g",7))
 
 
def get_vlist(g):
    vlist=[]
    for triple in g:
        vlist.append(triple[0])
        vlist.append(triple[1])
    vls=set(vlist)    
    return list(zip(vls,range(1,len(vls)+1))) # [("a",1),("b",2),...]
 
def get_ncomp(p,vlist):
    for pair in vlist:
        if p == pair[0]:
            return pair[1]
 
def krusk(g):
    
    vlist=get_vlist(g)
    sort_graph=sorted(list(g),key=lambda x: x[2])
 
    while True:
        
        if len(sort_graph)==0:
            break
        
        curr_edge=sort_graph[0]    # берем первое (самое короткое) ребро
        sort_graph=sort_graph[1:]  # удаляем его из графа
 
        p1=curr_edge[0]            # первая вершина ребра
        p2=curr_edge[1]            # вторая 
         
        n1=get_ncomp(p1,vlist)
        n2=get_ncomp(p2,vlist)
 
        if n1 != n2:
            print(curr_edge)
            # у всех вершин с n2 ставим n1
            t=[]
            for pair in vlist:
                if pair[1]==n2:
                    t.append((pair[0],n1))
                else:
                    t.append(pair)
            vlist=t
    
    print("OK")    
            
krusk(g)


def get_vlist(graph):
    res=[]
    for triple in graph:
        res.append(triple[0])
        res.append(triple[1])
    return list(set(res))    
 
 
def prim(graph):
    
    vlst=get_vlist(graph)
    skel=[vlst[0]]
    vlst=vlst[1:]
    
    while len(vlst) > 0:
        
        # Ищем ребро минимального веса, одна вершина которой в skel, 
        # а другая в vlst
        
        tmp=sorted([triple for triple in graph 
                     if (triple[0] in skel and triple[1] in vlst) or 
                        (triple[0] in vlst and triple[1] in skel)], 
                        key=lambda x: x[2])[0]
        
        print(tmp)
        
        
        if tmp[0] in vlst:
            v=tmp[0]
        else:
            v=tmp[1]
 
        skel.append(v)
        vlst=[q for q in vlst if q != v]
 
 
prim(g)