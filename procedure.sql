
-- Procedure to increase salary of workers of specified year of hireday
create or replace procedure incre(amount workers.salary%type, y number)
is  
To_many_increment exception;
begin
if amount>50 then
    raise To_many_increment;
else 
    update workers
    set salary=salary+salary*(amount/100)
    where to_char(hiredate,'YYYY')=y;
end if;
Exception
  when To_many_increment then
      dbms_output.put_line('Cannot increase more then 50% salary ');
  when others then
      dbms_output.put_line(sqlerrm || sqlcode);
end incre;

exec incre(2,2019)


-- Procedure to display customer detail of specified id

create or replace procedure display(x customers.cust_id%type)
is
row customers%rowtype;
begin
select * into row from customers where cust_id =x;
dbms_output.put_line(row.name||' '||row.phone||' '||row.address||' '||row.order_id);
Exception
when no_data_found then
    dbms_output.put_line('No row found , wrong id');
when others then
    dbms_output.put_line(sqlerrm || sqlcode);
end ;

exec display(6);

