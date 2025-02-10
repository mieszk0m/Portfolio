def key_gen(x):
    A = []
    s = []
    e = []
    t = []
    A.append([6*(x**3)+16*(x**2)+16*x+1,9*(x**3)+4*(x**2)+6*x+3])
    A.append([5*(x**3)+3*(x**2)+10*x+1,6*(x**3)+1*(x**2)+10*x+15])
    s.append(-1*(x**3)+-1*(x**2)+x)
    s.append(-1*(x**3)+x) 
    e.append(x**2)
    e.append(x**2 - 1) 
    
    return A,t,s
