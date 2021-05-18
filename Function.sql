-- Function of changing status of order from pending to servered 

create or replace function status(x orders.order_id%type)
return varchar is
s orders.status%type;
begin
select status into s from orders where order_id=x;
if( s = 'Pending') then
    update orders 
    set status='Servered'
    where order_id=x;
    return ('Servered to the '||x);
else
    return ('Already servered');
end if;

Exception 
when no_data_found then
    dbms_output.put_line('No row found , wrong id');
    return -1;
when others then
    dbms_output.put_line(sqlerrm || sqlcode);
    return -1;
end ;
 

declare
x orders.order_id%type;
begin
x := %ID;
dbms_output.put_line(status(x));
end;

--Function to display max salary and min salary of workers of specified post

create or replace function min_max(job workers.post%type,y out number)
return number is
x number;
begin 
select min(salary),max(salary) into x,y from workers 
where post=job;
return x;
Exception
when no_data_found then
    dbms_output.put_line('No row found , wrong input');
    return -1;
when Too_many_rows then
    dbms_output.put_line('To many rows found ');
    return -1;
when others then
    dbms_output.put_line(sqlerrm || sqlcode);
    return -1;
end;


declare
x number;
y number;
input workers.post%type;
begin
input := &post;
x := min_max(input,y);
dbms_output.put_line('Min value is '|| x ||' Max value is '||y ||' of '||input ||'Department');
end;

