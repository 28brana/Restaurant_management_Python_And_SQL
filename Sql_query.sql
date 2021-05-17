
-- 1.select query to display all records : 

select * from Customers;
select * from Orders;
select * from Meals;
select * from Workers;
select * from Managers;

-- 2.Display all customers whoes name starts with S

select * from Customers where name is like 'S%';

-- 3.Display Meals according in Sorted order by there Name

select * from Meals Order by name;

--4.Display All records of orders where Quantity is bigger then 5

select * from Orders where Quantity>5;

--5.Display name,post,hiredate of Workers whoes month of hiredare = Aug

select name , post , Hiredate from Workers
where to_char(Hiredate,'Mon'='Aug');

--6.Display count,Max salary,Min salary,Avg salary of Chef in workers table

select count(*)"Count",Max(salary)"MAX",Avg(salary)"AVERAGE",Min(salary)"MIN" from workers where post='Chef';

--7.Display Workers who where born in between 2018 to 2019
select * from workers where to_char(hiredate,'YY') between 18 and 19

--8.Display Workers who where hire on sunday and salary is above 30000
select * from workers where to_char(hiredate,'DY')='SUN' and salary > 30000;

--9.Display from manager table whoes no of workers working under them are 100 250 150
select * from managers where nw in (100,250,150);

--10.Display Unique post form worker table with there count 
select post,count(*)"No of workers" from workers group by post;
