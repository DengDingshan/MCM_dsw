function [best,initialmember_sort]=TSP_fitness(initialnumber,initialmember)
global yb citycount 
fitness=zeros(initialnumber,1);
d=zeros(citycount,citycount);
for i=1:citycount   %calculate distance
    for j=1:citycount
        d(i,j)=(((yb(i,2)-yb(j,2))^2)+((yb(i,3)-yb(j,3))^2))^(1/2);
    end
end


for i=1:initialnumber
    d_part=0;
    for j=1:citycount-1
        d_part=d_part+d(initialmember(i,j),initialmember(i,j+1));
    end
    fitness(i,1)=d_part+d(initialmember(i,citycount),initialmember(i,1));
end
initialmember(1:end,citycount+3)=fitness;
fitness=1-fitness;
%Evaluation function
fitnesstotal=sum(fitness);
fitness_proportion=(fitness)./fitnesstotal;
initialmember(1:end,citycount+1)=fitness_proportion; %shi ying gai lv

initialmember_sort=sortrows(initialmember,citycount+1);


best=initialmember_sort(1,1:end);




initialmember_sort(end,1:end)=best;
initialmember_sort(2:end,1:end)=sortrows(initialmember_sort(2:end,1:end),citycount+1);

%Evaluation function(except best)
fitnesstotal2=sum(initialmember_sort(2:end,end-2));
fitness_proportion2=initialmember_sort(2:end,end-2)./fitnesstotal2;
initialmember_sort(2:end,citycount+1)=fitness_proportion2;
%accumulate(except best)
fitness_accumulate=zeros(initialnumber-1,1);
for i=2:initialnumber
    fitness_accumulate(i-1,1)=sum(initialmember_sort(2:i,end-2));
end
initialmember_sort(2:end,end-1)=fitness_accumulate;
end