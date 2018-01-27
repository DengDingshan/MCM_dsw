% dirty water pool (mathematical models p37 extra question 2) 
clc;clear all;close all;
time=0:1:23;
ll=[150.12,115.56,84.96,66.6,68.04,71.64,82.08,132.84,...
    185.04,226.8,246.6,250.92,261,271.44,273.96,279,...
    291.6,302.04,310.68,290.52,281.16,248.4,210.24,186.84];
data=[time;ll];



%% cha fen fa
%flow of every hour in one day
figure(1)
hold on
time_new=0:0.0001:23;
ll_new=interp1(time,ll,time_new,'spline');
ll_mean=mean(ll_new);
plot(time_new,ll_new)
plot([0,23],[ll_mean,ll_mean])
hold off


%% assume that 0:00 the rl of pond is 0
%use ti xing fa to calculate continuous flow 
rl=zeros(1,24); %rl means rong liang
for i=1:23;
    rl(i+1)=txf(time_new,ll_new,i-1,i)+rl(i)-ll_mean;
end

%calculate the water in pool of each hour 
rl_min=min(rl);
rl=rl-rl_min;
figure(2)
plot(time,rl)

%% 
%assume that the height of pool is 3m,price of the bottom square of pool is 340 yuan each m^2,
%the long side and one short side is 250yuan/m,another short side is 450/m,
h=3;
rl_pool=1.25*max(rl);
square_bottom=rl_pool/h;
syms l price
price=(340*square_bottom)+250*(2*l+(square_bottom/l))+450*(square_bottom/l);
y=diff(price)
l_result=solve(y)   %caculate the min price and suitable long side and short side
l_result=double(l_result);
l_end=l_result(l_result>0);
price_end=double(subs(price,'l',l_end));
w_end=square_bottom/l_end;








