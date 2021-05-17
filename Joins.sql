--  Joins 
--1.Join to display Meals record and order record from comman meal_id

select * from meals natural join orders;

--2.Display Order record whoes price is bigger than  80 using left inner join

select * from orders left join meals using (meal_id) where price >80;

--3.Display manager record with there department details

select * from managers join workers using (wid ) where post ='Manager';

--4.Display name and their Quantity of food order by them
select name,Quantity from customers right join Orders using (order_id);

--5.Display customer and their order dish along with their price and order number
select customers.name,meals.name,meals.price,orders.order_id 
from customers,meals,orders
where customers.order_id=orders.order_id and orders.meal_id=meals.meal_id ;