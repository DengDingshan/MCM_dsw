surface0 = open ("surface0.txt","r").read().split('\n')
for i in range (len(surface0)):
    surface0[i]=surface0[i].split(' ')
    for j in range (len(surface0[i])):
        surface0[i][j] = float(surface0[i][j])
print len(surface0)

z=[];
for i in range(512):
    for j in range(512):
        if i!=511:
            if surface0[i][j] > surface0[i+1][j]:
                if j!=511:
                    if surface0[i][j]>surface0[i][j+1]:
                        if i!=0:
                            if surface0[i][j]>surface0[i-1][j]:
                                if j!=0:
                                    if surface0[i][j]>surface0[i][j-1]:
                                        z.append(surface0[i][j]);
                                else:
                                    z.append(surface0[i][j]);
                        else:
                            if j!=0:
                                if surface0[i][j]>surface0[i][j-1]:
                                    z.append(surface0[i][j]);
                            else:
                                z.append(surface0[i][j]);
                else:
                    if i!=0:
                        if surface0[i][j]>surface0[i-1][j]:
                            if j!=0:
                                if surface0[i][j]>surface0[i][j-1]:
                                    z.append(surface0[i][j]);
                            else:
                                z.append(surface0[i][j]);
                    else:
                        if j!=0:
                            if surface0[i][j]>surface0[i][j-1]:
                                z.append(surface0[i][j]);
                        else:
                            z.append(surface0[i][j]);
        else:
            if j!=511:
                    if surface0[i][j]>surface0[i][j+1]:
                        if i!=0:
                            if surface0[i][j]>surface0[i-1][j]:
                                if j!=0:
                                    if surface0[i][j]>surface0[i][j-1]:
                                        z.append(surface0[i][j]);
                                else:
                                    z.append(surface0[i][j]);
                        else:
                            if j!=0:
                                if surface0[i][j]>surface0[i][j-1]:
                                    z.append(surface0[i][j]);
                                
                            else:
                                z.append(surface0[i][j]);
            else:
                    if i!=0:
                        if surface0[i][j]>surface0[i-1][j]:
                            if j!=0:
                                if surface0[i][j]>surface0[i][j-1]:
                                    z.append(surface0[i][j]);
                            else:
                                z.append(surface0[i][j]);
                    else:
                        if j!=0:
                            if surface0[i][j]>surface0[i][j-1]:
                                z.append(surface0[i][j]);
                        else:
                            z.append(surface0[i][j]);
print z