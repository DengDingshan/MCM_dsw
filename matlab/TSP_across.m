function [child,wait_across]=TSP_across(initialnumber,initialmember_sort)
global citycount jiaochalv
% que ding jin xin jiao pei de ge ti

%display(initialnumber)
index_across=rand(1,initialnumber-1);%que ding index


wait_across=[]; %lun pan du
for i=1:initialnumber-1
    judgeindex=find(initialmember_sort(2:end,end-1)>=index_across(i));
    wait_across=[wait_across;initialmember_sort(judgeindex(1,1),1:end)];
end


%across
size_wait_across=size(wait_across);


randomnumber=zeros(1,2);
dadmom=[]; %que ding across sample
notdadmom=[];

for i=1:initialnumber-1
    index_across_judge=rand(1);
    if index_across_judge<=jiaochalv
        dadmom=[dadmom;wait_across(i,1:end)];
    else
        notdadmom=[notdadmom;wait_across(i,1:end)];
    end

end

% begin to across
dadmom=sortrows(dadmom,citycount+1);
[couplenumber,n]=size(dadmom);
if rem(couplenumber,2)~=0
    dadmom=dadmom(1:end-1,1:end);
    couplenumber=couplenumber-1;
    notdadmom=[notdadmom;dadmom(end,1:end)];
end
%display(couplenumber)
child=[];
for i=1:2:couplenumber-1
    child12=zeros(2,citycount+3);
    for j=1:5
        randomnumber(1)=randi(citycount,1);
        randomnumber(2)=randi(citycount,1);
        if randomnumber(1)~=randomnumber(2)
            if dadmom(i,randomnumber(1))<dadmom(i+1,randomnumber(2))
                dadmom(i,randomnumber(1):1:randomnumber(2))=dadmom(i,randomnumber(2):-1:randomnumber(1));
            elseif dadmom(i,randomnumber(1))>dadmom(i+1,randomnumber(2))
                dadmom(i,randomnumber(2):1:randomnumber(1))=dadmom(i,randomnumber(1):-1:randomnumber(2));
             
                if dadmom(i,randomnumber(2))<=dadmom(i+1,randomnumber(1))
                dadmom(i+1,randomnumber(1):1:randomnumber(2))=dadmom(i+1,randomnumber(2):-1:randomnumber(1));
                elseif dadmom(i,randomnumber(1))>dadmom(i+1,randomnumber(2))
                dadmom(i+1,randomnumber(2):1:randomnumber(1))=dadmom(i+1,randomnumber(1):-1:randomnumber(2));
                    
                end
            end
        end
    end
    child12=dadmom(i:i+1,1:end);
    child=[child;child12];
end
child=[child;notdadmom];
display(size(child))
end