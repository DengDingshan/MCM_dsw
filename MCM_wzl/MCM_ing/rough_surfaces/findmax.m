z=[];
for i=1:512
    for j=1:512
        if i~=512
            if surface0(i,j)>surface0(i+1,j)
                if j~=512
                    if surface0(i,j)>surface0(i,j+1)
                        if i~=1
                            if surface0(i,j)>surface0(i-1,j)
                                if j~=1
                                    if surface0(i,j)>surface0(i,j-1)
                                        z=[z;surface0(i,j)];
                                    end
                                else
                                    z=[z;surface0(i,j)];
                                end
                            end
                        else
                            if j~=1
                                if surface0(i,j)>surface0(i,j-1)
                                    z=[z;surface0(i,j)];
                                end
                            else
                                z=[z;surface0(i,j)];
                            end
                    
                        end
                    end
                
                else
                    if i~=1
                        if surface0(i,j)>surface0(i-1,j)
                            if j~=1
                                if surface0(i,j)>surface0(i,j-1)
                                    z=[z;surface0(i,j)];
                                end
                            else
                                z=[z;surface0(i,j)];
                            end
                        end
                    else
                        if j~=1
                            if surface0(i,j)>surface0(i,j-1)
                                z=[z;surface0(i,j)];
                            end
                        else
                            z=[z;surface0(i,j)];
                        end
                    
                    end
                end
            end
        else
            if j~=512
                    if surface0(i,j)>surface0(i,j+1)
                        if i~=1
                            if surface0(i,j)>surface0(i-1,j)
                                if j~=1
                                    if surface0(i,j)>surface0(i,j-1)
                                        z=[z;surface0(i,j)];
                                    end
                                else
                                    z=[z;surface0(i,j)];
                                end
                            end
                        else
                            if j~=1
                                if surface0(i,j)>surface0(i,j-1)
                                    z=[z;surface0(i,j)];
                                end
                            else
                                z=[z;surface0(i,j)];
                            end
                    
                        end
                    end
                
                else
                    if i~=1
                        if surface0(i,j)>surface0(i-1,j)
                            if j~=1
                                if surface0(i,j)>surface0(i,j-1)
                                    z=[z;surface0(i,j)];
                                end
                            else
                                z=[z;surface0(i,j)];
                            end
                        end
                    else
                        if j~=1
                            if surface0(i,j)>surface0(i,j-1)
                                z=[z;surface0(i,j)];
                            end
                        else
                            z=[z;surface0(i,j)];
                        end
                    
                    end
            end
        end
    end
end
            
                        

                        