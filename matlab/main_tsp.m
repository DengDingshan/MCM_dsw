%que ding parameter
clc;clear;close all;
global yb citycount bianyilv xuanzelv jiaochalv
yb=importdata('tspdata.csv',',');
initialnumber=500;
xuanzelv=0.02;
jiaochalv=0.9;
bianyilv=0.1;

size_yb=size(yb);
city=1:1:size(1);
citycount=size_yb(1);
initialmember=zeros(initialnumber,citycount+3);
for i=1:initialnumber   %create initial member
    initialmember(i,1:end-3)=randperm(citycount);
end


% calculate fitness
best_martix=[];
size_best_martix=size(best_martix);

a=0;
while a<15000 || (best_martix(end,end)/best_martix(end-1,end))<0.1
    [best,initialmember_sort]=TSP_fitness(initialnumber,initialmember);
    best_martix=[best_martix;best];
    size_best_martix=size(best_martix);
    %across
    [child,wait_across]=TSP_across(initialnumber,initialmember_sort);
    %variation
    [initialnumber,initialmember]=TSP_variation(initialnumber,child,best);
    
    a=a+1;
end
display(a)
display(best_martix(end,end))