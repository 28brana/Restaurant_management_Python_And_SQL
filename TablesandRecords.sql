-- Tables and Records of Data

-- 1. Customers tables
create table Customers(
Cust_id number primary key,
Name varchar2(20) not null,
Phone varchar2(10) ,
Address varchar(30),
order_id number
);

--1.Customers Records

insert into Customers values(1,'Bharat','9207958804','Amritsar',100);
insert into Customers values(2,'Aman','9213958301','Delhi',101);
insert into Customers values(3,'Gourav','7212936404','Bihar',102);
insert into Customers values(4,'Bittu','9317956608','Bihar',103);
insert into Customers values(5,'Anuj','8217923404','Amritsar',104);
insert into Customers values(6,'Rahul','9237928814','Chandighar',105);
insert into Customers values(7,'Mohit','7211958104','Amritsar',106);
insert into Customers values(8,'Suman','9317453305','Ludhiana',107);
insert into Customers values(9,'Anjali','7217158204','Uttrakhand',108);
insert into Customers values(10,'Rupali','8117928309','Amritsar',109);
insert into Customers values(11,'Summit','6117978894','Jalander',110);
insert into Customers values(12,'Shelly','9661754404','Amritsar',111);
insert into Customers values(13,'Tanu','6237955504','Delhi',112);
insert into Customers values(14,'Tushar','9327956604','Amritsar',113);
insert into Customers values(15,'Vicky','9327958804','Amritsar',114);
insert into Customers values(16,'Gagan','7517953404','Bihar',115);
insert into Customers values(17,'Sejal','9573954404','Amritsar',116);
insert into Customers values(18,'Tammana','8347958944','Amritsar',117);
insert into Customers values(19,'Ajay','8271988344','Amritsar',118);
insert into Customers values(20,'Sukhman','8217958434','Amritsar',119);

-- ORDER Table

create table Orders(
Order_id number primary key,
Time date not null ,
status varchar2(10) check(status = 'Servered' or status = 'Pending'),
Quantity number not null,
Meal_id number references Meals(Meal_id)
);

--ORDER Recordes

insert into Orders values(100,sysdate,'Pending',5,2);
insert into Orders values(101,sysdate,'Pending',2,1);
insert into Orders values(102,sysdate,'Pending',5,19);
insert into Orders values(103,sysdate,'Pending',1,10);
insert into Orders values(104,sysdate,'Pending',5,11);
insert into Orders values(105,sysdate,'Pending',2,11);
insert into Orders values(106,sysdate,'Pending',6,19);
insert into Orders values(107,sysdate,'Pending',2,2);
insert into Orders values(108,sysdate,'Pending',3,5);
insert into Orders values(109,sysdate,'Pending',3,8);
insert into Orders values(110,sysdate,'Pending',10,5);
insert into Orders values(111,sysdate,'Pending',7,8);
insert into Orders values(112,sysdate,'Pending',8,17);
insert into Orders values(113,sysdate,'Pending',7,15);
insert into Orders values(114,sysdate,'Pending',6,9);
insert into Orders values(115,sysdate,'Pending',11,7);
insert into Orders values(116,sysdate,'Pending',9,3);
insert into Orders values(117,sysdate,'Pending',9,12);
insert into Orders values(118,sysdate,'Pending',8,11);
insert into Orders values(119,sysdate,'Pending',2,20);

--Meals Table

create table Meals(
Meal_id number primary key,
Name varchar2(25) not null,
Price number not null
);

--Meals Records

insert into Meals values(1,'Aloo tikki',20);
insert into Meals values(2,'Amritsari kulche',30);
insert into Meals values(3,'Butter chicken',150);
insert into Meals values(4,'Biryani',100);
insert into Meals values(5,'Chicken tikka',120);
insert into Meals values(6,'Chole bhature',50);
insert into Meals values(7,'Kadai panner',80);
insert into Meals values(8,'Malayi kofte',80);
insert into Meals values(9,'Kulfi falooda',50);
insert into Meals values(10,'Palak panner',90);
insert into Meals values(11,'Samose',10);
insert into Meals values(12,'Tandoori chicken',250);
insert into Meals values(13,'Fish Tikka',200);
insert into Meals values(14,'Dosa',80);
insert into Meals values(15,'Kulfi',20);
insert into Meals values(16,'Gajar Halwa',50);
insert into Meals values(17,'Momo',50);
insert into Meals values(18,'Fish curry',250);
insert into Meals values(19,'Dal roti',80);
insert into Meals values(20,'Manchuriyan',100);

--Workers Tables

create table Workers(
Wid number primary key,
Name varchar2(20) not null,
Post varchar2(25) not null,
Salary number ,
Hiredate date not null
);

--Workers Recordes

insert into Workers values(100,'Suhail','Manager',50000,'21-May-19');
insert into Workers values(101,'Sumit','Manager',45000,'1-Jan-19');
insert into Workers values(102,'Rohan','Manager',60000,'5-Feb-15');
insert into Workers values(103,'Aman','Waiter',5000,'20-March-20');
insert into Workers values(104,'Rohit','Waiter',10000,'8-May-17');
insert into Workers values(105,'Mohit','Cashier',20000,'12-Dec-18');
insert into Workers values(106,'Akshay','Cashier',30000,'22-Dec-17');
insert into Workers values(107,'Robin','Chef',20000,'2-March-19');
insert into Workers values(108,'Suman','Chef',25000,'19-Aug-19');
insert into Workers values(109,'Bharat','HeadChef',80000,'28-Aug-10');
insert into Workers values(110,'Rupali','Chef',40000,'2-April-19');
insert into Workers values(111,'Sunil','Manager',60000,'10-May-17');
insert into Workers values(112,'Anuj','Chef',45000,'1-July-19');
insert into Workers values(113,'Bittu','Manager',55000,'2-Aug-18');
insert into Workers values(114,'Gourav','Manager',50000,'21-April-19');
insert into Workers values(115,'Gagan','Manager',40000,'1-Dec-19');
insert into Workers values(116,'Sourav','Waiter',8000,'11-Nov-18');
insert into Workers values(117,'Tushar','Waiter',7000,'8-Oct-17');
insert into Workers values(118,'Vishal','Chef',10000,'6-Oct-18');
insert into Workers values(119,'Shelly','Chef',57000,'22-Dec-15');
insert into Workers values(200,'Tonny','Cleaner',4000,'23-Feb-17');
insert into Workers values(201,'Golu','Cleaner',3000,'21-April-18');
insert into Workers values(202,'Abhi','Cleaner',5000,'3-Aug-18');
insert into Workers values(203,'Aditya','Cleaner',3000,'13-Feb-17');

--Managers Table

create table Managers(
    Wid number references Workers(Wid),
    Department varchar2(20),
    NW number default 20 --no fo workers work under them
);

--Managers Records

insert into Managers values(100,'Cleaning',100);
insert into Managers values(101,'Food',250);
insert into Managers values(102,'Service',150);
insert into Managers values(111,'Service',120);
insert into Managers values(113,'Head-Manager',200);
insert into Managers values(114,'Food-storage',150);
insert into Managers values(115,'Chef',310);

