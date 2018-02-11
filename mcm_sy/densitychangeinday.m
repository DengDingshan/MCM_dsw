% density change in year
clc;close all;clear;
densitychangeindays=importdata('100kmdensitychangeinday.csv',',',1);
densitychangeindays=densitychangeindays.data;
densitychangeindays=densitychangeindays(1:25,1:end);
hour=densitychangeindays(1:end,5);
for i=1:25
    hour(i)=round(hour(i)+24/460*densitychangeindays(1,4));
    if hour(i)>24
        hour(i)=hour(i)-24;
    end
end
density=zeros(25,1);
for i=1:25
    density(i,1)=mean(densitychangeindays(i,6:end));
end
figure(1)
hold on
scatter(hour,density)
[P,res] = polyfit(hour,density,3);
hour2=0:0.1:24;
daychange2=polyval(P,hour2);
plot(hour2,daychange2,'r')
hold off
n=res.normr;
y=sum((density-mean(density)).^2);
R2=1.0-((n^2)/y);