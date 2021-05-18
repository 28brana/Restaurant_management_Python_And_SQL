-- Cursor to display name,post,salary of workers whoes salary is above 30000 and post is manager or chef

declare
cursor c1 is select name,post,salary from workers where salary >30000 and post in ('Manager','Chef');
begin
for i in c1
Loop 
 dbms_output.put_line(i.name || ' is ' ||i.post || ' and his or her salary is ' || i.salary);
end loop;
end;


-- display customers name and their ordered meal with their price of specific city

declare
cursor c1 is select customers.name,meals.name,meals.price from customers,orders,meals 
where customers.order_id=orders.order_id and meals.meal_id= Orders.meal_id and customers.address='Amritsar';
name customers.name%type;
meal meals.name%type;
price meals.price%type;
begin
open c1;
loop 
fetch c1 into name,meal,price;
dbms_output.put_line(name||' has ordered ' ||meal||' whoes price is '||price);
exit when c1 %notfound;
end loop;
close c1;
end;




