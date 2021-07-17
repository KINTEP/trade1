#Important codes for analysis

#This function solves differential equation given initail conditions and a transformation matrix

def predict(matx, init, num = 100):
    x_vals = [init[0]]
    y_vals = [init[1]]
    for i in range(num):
        arr1 = np.array([x_vals[-1], y_vals[-1]])
        res1 = matx @ arr1
        x_vals.append(res1[0])
        y_vals.append(res1[1])
    
    return x_vals, y_vals


#This function obtains all the turning points from a sequence

def turning_points(sequence):
    upt = []
    dwn = []
    N = len(sequence)
    
    for i in range(1, N-1):
        t = sequence[i]
        t0 = sequence[i-1]
        t1 = sequence[i+1]
        if t0 <= t and t1 < t:
            upt.append(i)
        if t0 >= t and t1 > t:
            dwn.append(i)
    
    add = upt + dwn
    add = sorted(add)
            
    n1 = len(add)

    nan = list(sequence[:add[0]])
    normal = normalize(nan)[1:]
    
    for i in range(n1-1):
        f = add[i]
        s = add[i+1]
        ls = sequence[f:s+1]
        norm = normalize(ls)
        normal += list(norm[1:])
        nan += list(ls[1:])
        
    T = list(sequence[add[-1]:])
    T1 = list(sequence[add[-1]:])
    nan += T
    normal += normalize(T1)
    
    return normal