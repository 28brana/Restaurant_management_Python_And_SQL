-- Trigger to automatic create id for meals
create or replace trigger prime
before insert or update on meals
for each row
declare
prev number;
begin
select nvl(max(meal_id),0) into prev from meals;
:new.meal_id := prev+1;
end;

insert into meals (name,price) values('Curry',200);

---------------------------------------------------

-- Trigger for put validation on phone number

create or replace trigger validation
before insert or update of phone on customers
for each row
declare
small exception;
begin
  if(length(:new.phone) <10 ) then
  :new.phone := NULL;
  raise small;
  end if;
  
Exception
when small then
dbms_output.put_line('Phone number is very small');
end validation;


insert into customers (cust_id,name,phone) values (21,'jonny',12345);

