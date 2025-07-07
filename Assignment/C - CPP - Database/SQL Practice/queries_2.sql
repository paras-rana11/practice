

select * from sales;


-- Find the total sales amount (SUM(Amount)) for each salesperson.
select s.salespersonid, sp.firstname, sp.lastname, count(s.saleid) as product_sold, sum(s.amount) as total_selling_amt from sales s
join salespersons sp on s.salespersonid = sp.salespersonid
group by SalespersonID;



-- Task 1 (GROUP BY + HAVING):
-- Description: Write a query to show the total sales amount for each SalespersonID, and use the HAVING clause to filter only those salespeople whose total sales amount is greater than 1000.
SELECT s.salespersonid, sp.firstname, sp.lastname, sum(s.amount) as total_selling_amt
from sales s join salespersons sp on s.salespersonid = sp.salespersonid
group by s.salespersonid
having total_selling_amt > 1000;


-- Task 2 (GROUP BY + COUNT):
-- Description: Write a query to show the number of sales transactions (SaleID) for each SalespersonID. Make sure to use COUNT(SaleID) to count the number of sales per salesperson.
select s.salespersonid, sp.firstname, sp.lastname, count(s.saleid) as product_sold from sales s
join salespersons sp on s.salespersonid = sp.salespersonid
group by SalespersonID;


-- Task 3 (GROUP BY + MAX):
-- Description: Write a query to find the highest sale amount (Amount) for each SalespersonID. You should use the MAX() function to find the maximum sale amount for each salesperson.
select s.salespersonid, sp.firstname, sp.lastname, max(s.amount) as highest_selling_amount
from sales s join salespersons sp on s.salespersonid = sp.salespersonid
group by s.salespersonid;


-- Task 4 (GROUP BY + AVG):
-- Description: Write a query to calculate the average sale amount for each SalespersonID using the AVG() function. The result should show the SalespersonID and the average sale amount.
select s.salespersonid, sp.firstname, sp.lastname, avg(s.amount) as avg_selling_amount
from sales s join salespersons sp on s.salespersonid = sp.salespersonid
group by s.salespersonid;


-- Task 5 (DATE GROUPING + HAVING):
-- Description: Write a query to group the sales by month (using SaleDate). For each month, show the total sales amount and filter the results to show only the months where the total sales amount exceeds 1000.
select  year(saledate), month(saledate), sum(amount) as total_sales from sales
group by year(saledate), month(saledate)
having total_sales > 1000;

--  total sales for each sale date:
select  saledate, sum(amount) from sales
group by saledate;


















































