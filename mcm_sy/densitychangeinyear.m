% density change in year
clc;close all;clear;
densitychangeinyears=importdata('100kmdensitychangeinyear.csv',',',1);
densitychangeinyears=densitychangeinyears.data;
monthchange=zeros(12,1);
month=densitychangeinyears(1:end,1);
for i=1:12
    monthchange(i,1)=mean(densitychangeinyears(i,4:8));
end


figure(1)
hold on
scatter(month,monthchange,'k*')
[P,res] = polyfit(month,monthchange,6);
month2=1:0.1:12;
monthchange2=polyval(P,month2);
plot(month2,monthchange2,'b')
hold off
n=res.normr;
y=sum((monthchange-mean(monthchange)).^2);
R2=1.0-((n^2)/y);