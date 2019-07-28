-- The following is a script that imports csv from local disk into pre-existing tables 
-- in MySQL 

-- NOTE: Prof. Rachlin says that this will not work in MySQL Workbench.  
-- This mean's you'll either have to run MySQL from the command line and enter 
-- the import commmands, or use a different client like DBeaver.  


use coffee_database;

-- returns full name of the variable we need to grant permissions
show variables like '%local%';

-- grant permissions to import data from local 
set global local_infile = on; 

-- import the aroma data and populate aroma data 
LOAD DATA LOCAL INFILE 'C:\\Users\\noahd\\Music\\coffee_data\\aromas.csv'
	 INTO TABLE coffee_database.aroma
	 FIELDS TERMINATED BY ','
	 ENCLOSED BY '"'
 	 LINES TERMINATED BY '\n' -- \n means "new line"
 IGNORE 1 ROWS;


-- verify aroma import
select * from coffee_database.aroma;

-- import the coffee_product data and populate coffee_product data 
LOAD DATA LOCAL INFILE 'C:\\Users\\noahd\\Music\\coffee_data\\coffee_products.csv'
	 INTO TABLE coffee_database.coffee_products
	 FIELDS TERMINATED BY ','
	 ENCLOSED BY '"'
 	 LINES TERMINATED BY '\n' -- \n means "new line"
 IGNORE 1 ROWS;


-- verify coffee_product import
select * from coffee_database.coffee_products;



-- import the coffee_product data and populate coffee_product data 
LOAD DATA LOCAL INFILE 'C:\\Users\\noahd\\Music\\coffee_data\\origin.csv'
	 INTO TABLE coffee_database.origin
	 FIELDS TERMINATED BY ','
	 ENCLOSED BY '"'
 	 LINES TERMINATED BY '\n' -- \n means "new line"
 IGNORE 1 ROWS;




-- import the coffee_product data and populate coffee_product data 
LOAD DATA LOCAL INFILE 'C:\\Users\\noahd\\Music\\coffee_data\\farmers.csv'
	 INTO TABLE coffee_database.farm
	 FIELDS TERMINATED BY ','
	 ENCLOSED BY '"'
 	 LINES TERMINATED BY '\n' -- \n means "new line"
 IGNORE 1 ROWS;


-- verify coffee_product import
select * from coffee_database.coffee_products;


LOAD DATA LOCAL INFILE 'C:\\Users\\noahd\\Music\\coffee_data\\coffee-to-farm.csv'
	 INTO TABLE coffee_database.coffee_to_farm
	 FIELDS TERMINATED BY ','
	 ENCLOSED BY '"'
 	 LINES TERMINATED BY '\n' -- \n means "new line"
 IGNORE 1 ROWS;


-- verify coffee_product import


LOAD DATA LOCAL INFILE 'C:\\Users\\noahd\\Music\\coffee_data\\aromascoffee.csv'
	 INTO TABLE coffee_database.aroma_coffee
	 FIELDS TERMINATED BY ','
	 ENCLOSED BY '"'
 	 LINES TERMINATED BY '\n' -- \n means "new line"
 IGNORE 1 ROWS;

select * from coffee_database.aroma_coffee;


load DATA LOCAL INFILE 'C:\\Users\\noahd\\Music\\coffee_data\\user_clean.csv'
	 INTO TABLE coffee_database.user
	 FIELDS TERMINATED BY ','
	 ENCLOSED BY '"'
 	 LINES TERMINATED BY '\n' -- \n means "new line"
 IGNORE 1 ROWS;

select* from user;

load DATA LOCAL INFILE 'C:\\Users\\noahd\\Music\\coffee_data\\rating.csv'
	 INTO TABLE coffee_database.rating
	 FIELDS TERMINATED BY ','
	 ENCLOSED BY '"'
 	 LINES TERMINATED BY '\n' -- \n means "new line"
 IGNORE 1 ROWS;

select * from rating;

load DATA LOCAL INFILE 'C:\\Users\\noahd\\Music\\coffee_data\\order.csv'
	 INTO TABLE coffee_database.orders
	 FIELDS TERMINATED BY ','
	 ENCLOSED BY '"'
 	 LINES TERMINATED BY '\n' -- \n means "new line"
 IGNORE 1 ROWS;

select * from orders;

load DATA LOCAL INFILE 'C:\\Users\\noahd\\Music\\coffee_data\\coffee_order.csv'
	 INTO TABLE coffee_database.coffee_order
	 FIELDS TERMINATED BY ','
	 ENCLOSED BY '"'
 	 LINES TERMINATED BY '\n' -- \n means "new line"
 IGNORE 1 ROWS;

select * from coffee_order;

load DATA LOCAL INFILE 'C:\\Users\\noahd\\Music\\coffee_data\\farmers.csv'
	 INTO TABLE coffee_database.farm
	 FIELDS TERMINATED BY ','
	 ENCLOSED BY '"'
 	 LINES TERMINATED BY '\n' -- \n means "new line"
 IGNORE 1 ROWS;

select * from farm;

load DATA LOCAL INFILE 'C:\\Users\\noahd\\Music\\coffee_data\\subs.csv'
	 INTO TABLE coffee_database.subscription
	 FIELDS TERMINATED BY ','
	 ENCLOSED BY '"'
 	 LINES TERMINATED BY '\n' -- \n means "new line"
 IGNORE 1 ROWS;

select * from subscription;

load DATA LOCAL INFILE 'C:\\Users\\noahd\\Music\\coffee_data\\coffee_farmer.csv'
	 INTO TABLE coffee_database.coffee_to_farm
	 FIELDS TERMINATED BY ','
	 ENCLOSED BY '"'
 	 LINES TERMINATED BY '\n' -- \n means "new line"
 IGNORE 1 ROWS;