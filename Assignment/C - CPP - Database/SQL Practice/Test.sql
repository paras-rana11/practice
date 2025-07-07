create table Products (
	product_id int primary key,
    product_name varchar(50),
    category varchar(50),
    unit_price int);

CREATE TABLE Sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    quantity_sold INT,
    sale_date DATE,
    total_price INT,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);


INSERT INTO Sales (sale_id, product_id, quantity_sold, sale_date, total_price) VALUES
( 1, 101, 5, "2024-01-01", 2500 ),
( 2, 102, 3, "2024-01-02", 900 ),
( 3, 103, 2, "2024-01-02", 60 ),
( 4, 104, 4, "2024-01-03", 80 ),
( 5, 105, 6, "2024-01-03", 90 ),

(6, 107, 3, '2024-04-18', 360),
(7, 108, 5, '2024-03-29', 600),
(8, 110, 6, '2024-06-01', 2520), 
(9, 102, 3, '2024-01-28', 2700), 
(10, 122, 7, '2024-05-19', 1260),

(11, 105, 10, '2024-01-28', 1500),
(12, 109, 6, '2024-04-09', 1800), 
(13, 115, 5, '2024-02-04', 1125), 
(14, 121, 4, '2024-03-29', 960),
(15, 118, 5, '2024-02-26', 6250), 

(16, 113, 2, '2024-03-02', 85),
(17, 111, 4, '2024-04-09', 480), 
(18, 114, 8, '2024-06-20', 3600),
(19, 107, 7, '2024-03-29', 1960),
(20, 119, 4, '2024-04-25', 640),

(21, 106, 3, '2024-06-12', 600),
(22, 104, 7, '2024-02-20', 1120),
(23, 120, 3, '2024-06-02', 1350),
(24, 108, 6, '2024-01-22', 1080),
(25, 122, 6, '2024-03-25', 1080),

(26, 110, 5, '2024-01-08', 1750),
(27, 121, 4, '2024-02-14', 70),
(28, 116, 8, '2024-04-09', 2880),
(29, 109, 5, '2024-03-29', 1500),
(30, 112, 4, '2024-05-10', 400),

(31, 116, 6, '2024-05-14', 2880), 
(32, 104, 8, '2024-03-29', 1280),
(33, 113, 2, '2024-01-28', 100), 
(34, 119, 4, '2024-02-16', 640), 
(35, 106, 4, '2024-01-13', 400);

INSERT INTO Products (product_id, product_name, category, unit_price)
VALUES 
    (101, 'Laptop', 'Electronics', 500),
    (102, 'Smartphone', 'Electronics', 300),
    (103, 'Headphone', 'Electronics', 30),
    (104, 'Keyboard', 'Electronics', 20),
    (105, 'Mouse', 'Electronics', 15),
    (106, 'Shirt', 'Clothing', 25),
    (107, 'Jeans', 'Clothing', 40),
    (108, 'Jacket', 'Clothing', 60),
    (109, 'Sneakers', 'Footwear', 50),
    (110, 'Boots', 'Footwear', 70),
    (111, 'Sandals', 'Footwear', 30),
    (112, 'Watch', 'Accessories', 100),
    (113, 'Sunglasses', 'Accessories', 25),
    (114, 'Hat', 'Accessories', 15),
    (115, 'Backpack', 'Bags', 45),
    (116, 'Handbag', 'Bags', 80),
    (117, 'Wallet', 'Accessories', 20),
    (118, 'Tablet', 'Electronics', 250),
    (119, 'Bluetooth Speaker', 'Electronics', 40),
    (120, 'Camera', 'Electronics', 150),
    (121, 'Coffee Maker', 'Appliances', 60),
    (122, 'Toaster', 'Appliances', 30),
    (123, 'Microwave', 'Appliances', 90),
    (124, 'Binoculars', 'Appliances', 120);
 

-- 0. Retrieve all columns from the Sales table.
select * from sales;

-- 1. Retrieve all columns from both tables.
select s.sale_id, s.product_id, s.quantity_sold, s.sale_date, s.total_price, p.product_id, p.product_name, p.category, p.unit_price
from sales s left join products p on s.product_id = p.product_id;




-- 2. Retrieve the product_name and unit_price from the Products table
select product_name, unit_price from products;


-- 3. Retrieve the product_name and unit_price from the Products table.
select product_name, unit_price from products;


-- 4. Filter the Sales table to show only sales with a total price greater than $100
select * from sales where total_price > 100;


-- 5. Filter the Products table to show only products in the 'Electronics' category
select * from products where category = 'Electronics';


-- 6. Retrieve the sale_id and total_price from the Sales table for sales made on January 3, 2024.
select sale_id, total_price from sales where sale_date = "2024-01-03";


-- 7. Retrieve the product_id and product_name from the Products table for products with a unit_price greater than $100.
select product_id, product_name from products where unit_price > 100;


-- 8. Calculate the total revenue generated from all sales in the Sales table.
select sum(total_price) as Total_Revenue from sales;


-- 9. Calculate the average unit price of products in the Products table
select avg(unit_price) as Avg_Unit_Price from products;


-- 10. Count Sales Per Day from the Sales table
select sale_date, sum(total_price), count(sale_id) from sales group by sale_date order by sale_date;


-- 11. Retrieve product_name and unit_price from the Products table with the Highest Unit Price
select product_name, unit_price from products order by unit_price desc limit 1;


-- 12. Retrieve the total price of all sales, rounding the values to two decimal places.
select round(sum(total_price), 2) AS total_sales_price from Sales;


-- 13. Retrieve the product_name and category from the Products table, ordering the results by category in ascending order.
select product_name, category from products order by category;


-- 14. Calculate the total quantity_sold of products in the 'Electronics' category.
select sum(s.quantity_sold) as total_quantity_sold from sales s 
join products p on s.product_id = p.product_id
where p.category = "electronics";  


-- 15. Retrieve the product_name and total_price from the Sales table, calculating the total_price as quantity_sold multiplied by unit_price.
select p.product_name, p.unit_price, sum(quantity_sold), sum( s.quantity_sold * p.unit_price ) as TOTAL_PRICE 
from sales s join products p on s.product_id = p.product_id
group by p.product_name, p.unit_price;


select sum(quantity_sold) from sales group by product_id having product_id=102;


-- 16. Find the Products Not Sold from Products table.
select  p.product_id, p.product_name, p.category, p.unit_price from products p
left join sales s on p.product_id = s.product_id
where s.sale_id is null or s.sale_id = "";


-- 17. Calculate the total revenue generated from sales for each product category.
select p.category, sum(s.total_price)  AS total_revenue from sales s 
join products p on  s.product_id = p.product_id
group by p.category;



-- 18. Calculate the number of days between the current date and the sale date for each sale.
SELECT DATEDIFF(CURDATE(), '2024-05-07') AS days_difference;

select sale_id, product_id, sale_date, DATEDIFF(CURDATE(), sale_date) AS days_difference from Sales;


-- 19. Categorize sales as "High", "Medium", or "Low" based on total price (e.g., > $200 is High, $100-$200 is Medium, < $100 is Low).
select *,
	case
		when total_price > 1000 then "HIGH"
        when total_price between 501 and 1000 then "MEDIUM"
        else "LOW" 
	end as Sale_Category
from sales;

-- 20. Count the number of sales made in each month.
select year(sale_date) as sale_year, month(sale_date) as sale_month, count(quantity_sold) as total_quantity_sold
from Sales
group by year(sale_date), month(sale_date)
order by sale_year, sale_month;






















-- categorize sale:
delimiter !!
	create procedure categorizeSale(in total_price int)
	begin
		declare price_category varchar(50);
        
        if total_price > 1000 then
			set price_category = "HIGH";
		elseif total_price between 500 and 1000 then
			set price_category = "MEDIUM";
		else
			set price_category = "LOW";
        end if;
        
        SELECT price_category AS categorize_sale;
    end !!
delimiter ;

call categorizeSale( (select total_price from sales where sale_id=23) );

call categorizeSale( (select total_price from sales where sale_id=14) );

call categorizeSale( (select total_price from sales where sale_id=16) );









