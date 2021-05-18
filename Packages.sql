-- Package specification
create or replace Package Math as
    function max_sal return number;
    function min_sal return number;
    function avg_sal return number;
end Math;

-- Package Body
create or replace Package Body Math As
    -- Max salary function

    function max_sal return number is
    x number;
    begin 
        select max(salary) into x from workers;
        return x;
    end max_sal;

    -- Min salary function

    function min_sal return number is
    x number;
    begin 
        select min(salary) into x from workers;
        return x;
    end min_sal;

    -- Average salary function

    function avg_sal return number is
    x number;
    begin 
        select avg(salary) into x from workers;
        return x;
    end avg_sal;

end Math;

--Execution
begin 
dbms_output.put_line('MAX salary '|| math.max_sal);
dbms_output.put_line('MIN salary '|| math.min_sal);
dbms_output.put_line('AVG salary '|| math.avg_sal);
end;

-----------------------------------------------------------------------------------------

-- Package that display info about any table by their id

-- Package specification

create or replace package info As
  procedure disp_customer(x customers.cust_id%type);
  procedure disp_order(x orders.order_id%type);
  procedure disp_worker(x workers.wid%type);
  procedure disp_manager(x managers.wid%type);
  procedure disp_meal(x meals.meal_id%type);
end info;

-- Package body

create or replace package body info As

    -- Customers info
    procedure disp_customer(x customers.cust_id%type) is
    temp customers%rowtype;
    begin
    select * into temp from customers where cust_id=x;
    dbms_output.put_line(temp.name||' '||temp.address||' '||temp.order_id);
    end disp_customer;
     
    -- Order info
    procedure disp_order(x orders.order_id%type) is
    temp orders%rowtype;
    begin
    select * into temp from orders where order_id=x;
    dbms_output.put_line(temp.order_id||' '||temp.status||' '||temp.quantity);
    end disp_order;
    
    -- Worker info
    procedure disp_worker(x workers.Wid%type) is
    temp workers%rowtype;
    begin
    select * into temp from workers where wid=x;
    dbms_output.put_line(temp.wid||' '||temp.name||' '||temp.post||' '||temp.salary||' '||temp.hiredate);
    end disp_worker;
    
    -- Manager info
    procedure disp_manager(x managers.Wid%type) is
    temp managers%rowtype;
    begin
    select * into temp from managers where wid=x;
    dbms_output.put_line(temp.wid||' '||temp.department||' '||temp.nw);
    end disp_manager;
    
    -- Meal info
    procedure disp_meal(x meals.meal_id%type) is
    temp meals%rowtype;
    begin
    select * into temp from meals where meal_id=x;
    dbms_output.put_line(temp.meal_id||' '||temp.name||' '||temp.price);
    end disp_meal;
    
    
end info;
   
-- Execution
exec info.disp_customer(1);
exec info.disp_order(101);
exec info.disp_meal(2);
exec info.disp_worker(108);
exec info.disp_manager(101);
    