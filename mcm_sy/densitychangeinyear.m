% density change in year
clc;close all;clear;
densitychangeinyear=importdata('100kmdensitychangeinyear.csv',',',1);
densitychangeinyear=densitychangeinyear.data;
monthchange=zeros(12,1);
month=densitychangeinyear(1:end,1);
for i=1:12
    monthchange(i,1)=mean(densitychangeinyear(i,4:8));
end


figure(1)
hold on
scatter(month,monthchange)
P = polyfit(month,monthchange,6);
month2=1:0.1:12;
monthchange2=polyval(P,month2);
plot(month2,monthchange2,'r')
hold off