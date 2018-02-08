function[initialnumber,initialmember]=TSP_variation(initialnumber,child,best)
global citycount bianyilv
% variation

wait_variation=[];
for i=1:initialnumber-1
    judge_variation=rand(1);
    if judge_variation<=bianyilv
        wait_variation=[wait_variation;child(i,1:end),i];
    end
end

size_wait_variation=size(wait_variation);
variationnumber=size_wait_variation(1);

randomnumber2=zeros(1,2);
for i=1:variationnumber % assure that we will not create an unvalid child
    randomnumber2(1)=randi(citycount,1);
    randomnumber2(2)=randi(citycount,1);
    if randomnumber2(1)~=randomnumber2(2)
        middle=wait_variation(i,randomnumber2(1));
        wait_variation(i,randomnumber2(1))=wait_variation(i,randomnumber2(2));
        wait_variation(i,randomnumber2(2))=middle;
    end
    child(wait_variation(i,end),1:citycount)=wait_variation(i,1:citycount);

end

%new member
initialmember=[];
initialmember=[best(1:citycount+3);child(1:end,1:citycount+3)];
size_initialmember=size(initialmember);
initialnumber=size_initialmember(1)

end