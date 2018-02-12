% density change in year
clc;close all;clear;
densitychangeindays=importdata('200kmdensitychangeinday.csv',',',1);
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
hour=hour(1:end-1,1);
density=density(1:end-1,1);
hour1=zeros(24,1);
density1=zeros(24,1);
for i=18:24
    hour1(i-17,1)=hour(i,1);
    density1(i-17,1)=density(i,1);
end
for i=1:17
    hour1(i+7,1)=hour(i,1);
    density1(i+7,1)=density(i,1);
end
scatter(hour1,density1,'*k')
plot(hour1,density1,'b')
xlabel('hour');
ylabel('Ne(m^-3)');
title('electronic number density change in one day(F2)');
figure(2)

fc=9*((density1).^(1/2))/(10^6);
seta=pi/6;
MUF=fc/cos(seta);
plot(hour1,MUF)

hold off

