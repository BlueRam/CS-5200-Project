drop database if exists coffee_database;
create database if not exists coffee_database;

use coffee_database; 


drop table if exists origin; 

create table origin(
origin_id int primary key auto_increment, 
state varchar(50) not null, 
country varchar(50) not null);


drop table if exists farm;

create table farm(
farm_id int primary key auto_increment, 
operation_name varchar(1000) not null, 
origin_id int not null,
constraint origin_id foreign key (origin_id) references origin (origin_id));


drop table if exists coffee_products;

create table coffee_products(
coffee_id int primary key auto_increment, 
title varchar(500) not null, 
roast enum('light', 'medium', 'dark', 'espresso'),
price double not null, 
description varchar(1000) not null, 
remaining int not null); 


drop table if exists coffee_to_farm;  

create table coffee_to_farm(
coffee_id int not null, 
farm_id int not null, 
constraint coffee_id foreign key (coffee_id) references coffee_products (coffee_id),
constraint farm_id foreign key (farm_id) references farm (farm_id));


drop table if exists aroma; 

create table aroma(
flavor_aroma_id int primary key auto_increment,
flavor_aroma_description varchar(100) not null); 


drop table if exists aroma_coffee;

create table aroma_coffee(
flavor_aroma_id int not null, 
coffee_id_a int not null, 
constraint flavor_aroma_id foreign key (flavor_aroma_id) references aroma (flavor_aroma_id), 
constraint coffee_id_a foreign key (coffee_id_a) references coffee_products (coffee_id));  


drop table if exists user;  

create table user(
user_id int primary key auto_increment,
total_name varchar(50) not null,
username varchar(50) not null,
password varchar(50) not null, 
email varchar(50) not null, 
address varchar(500) not null, 
subscriber tinyint default 0,
dob date not null, 
drink_frequency enum('1','2','3','4','5+'), 
roast_preference enum('light', 'medium', 'dark', 'espresso'), 
gender enum('M', 'F', 'Other'));  


drop table if exists rating;

create table rating( 
reviewer_id int primary key auto_increment,
coffee_id_r int not null,
rating enum('1','2','3','4','5'), 
constraint reviewer_id foreign key (reviewer_id) references user (user_id), 
constraint coffee_id_r foreign key (coffee_id_r) references coffee_products (coffee_id)); 

drop table if exists subscription_level;

create table subscription_level(
level_id int primary key,
level_name ENUM('Bronze','Silver','Gold'),
coffee_amount ENUM('1','2','3'));

drop table if exists subscription;  

create table subscription(
subscription_id int primary key auto_increment,
date_subscribed date not null,  
user_id int not null,
level_id int not null,
constraint user_id foreign key (user_id) references user (user_id),
constraint level_id foreign key (level_id) references subscription_level(level_id)); 

drop table if exists orders; 

create table orders(
order_id int primary key auto_increment, 
order_date date not null, 
subscription_order tinyint, 
user_id_o int not null, 
constraint user_id_o foreign key (user_id_o) references user (user_id)); 


drop table if exists coffee_order; 

create table coffee_order( 
coffee_id_co int not null, 
order_id_co int not null,
count_prod int,

constraint coffee_id_co foreign key (coffee_id_co) references coffee_products (coffee_id), 
constraint order_id_co foreign key (order_id_co) references orders (order_id)); 


drop table if exists recomendations;

create table recommendations(
re_user_id int not null,
re_coffee_id int,
product_rank int,

constraint re_user_id foreign key (re_user_id) references user (user_id),
constraint re_coffee_id foreign key (re_coffee_id) references coffee_products (coffee_id)

);

drop table if exists kart;
drop table if exists kart;
create table kart (
user_id_k int not null,
constraint user_id_k foreign key (user_id_k) references user (user_id),
coffee_id_k int not null,
constraint coffee_id_k foreign key (coffee_id_k) references coffee_products (coffee_id),
num_in_cart int not null Default 0);



-- Create Add User Procedure-- 
drop procedure if exists add_user; 

delimiter // 
create procedure add_user 
(	in user_id_param varchar(50), 
	in name_param varchar(50),
    in username_param varchar(50),
	in password_param varchar(50), 
	in email_param varchar(200), 
	in address_param varchar(500),
	in subscriber_stat_param tinyint, 
	in dob_param date, 
	in drink_frequency_param enum('1','2','3','4','5+'),
	in roast_preference_param enum('light','medium','dark','espresso'),
	in gender_param enum('M','F','Other')
	
)
begin
	insert into user
	values (
		user_id_param, name_param, username_param,password_param, email_param,
		address_param, subscriber_stat_param, dob_param, drink_frequency_param,
		roast_preference_param, gender_param); 
	select concat(name_param, ' added to Users Table.') as status; 
end // 
delimiter ; 





drop procedure if exists upgrade_sub;

DELIMITER //

CREATE PROCEDURE upgrade_sub
(
	IN user_id_param int,
    IN level_id_param int
)
begin
	update user
    set subscriber = 1
    where user_id = user_id_param;

	if user_id_param not in (select user_id from subscription) then
		insert into subscription
        values (NULL,curdate(),user_id_param,level_id_param);
	end if;
    
    IF user_id_param in (select user_id from subscription) then
		update subscription
        set level_id = level_id_param
        where user_id = user_id_param;
	end IF;
    
end //
DELIMITER ;



-- Test Subscription update trigger 
-- update user 
-- set subscriber = true
-- where user_id = 1;

-- select * from user; 
-- select * from subscription; 




-- Purchase PROCEDURE

drop procedure if exists purchase;

DELIMITER //

create procedure purchase
(	IN order_id_param int,
	IN order_date_param datetime,
	IN subs_order_param tinyint(4),
	IN user_id_param int
        
)
begin
    insert into orders
    values (order_id_param, order_date_param,subs_order_param,user_id_param);
    
end //
DELIMITER ;


drop procedure if exists purchase_join;
DELIMITER //
create procedure purchase_join
(
	IN order_id_param int,
    IN coffee_id_param int,
    IN count_param int
)
begin
	insert into coffee_order
    values (order_id_param, coffee_id_param, count_param);
    
end //
DELIMITER ;






-- Rating Product procedure

drop procedure if exists rate_product;

DELIMITER //

create procedure rate_product
(
	IN reviewer_id_param int,
    IN coffee_id_param int,
    IN rating_param ENUM('1','2','3','4','5')
)
begin

	INSERT INTO rating
    VALUES (reviewer_id_param,coffee_id_param,rating_id_param);
    
end // 
DELIMITER ;

INSERT INTO subscription_level
VALUES
	(1,'Bronze',1),
    (2,'Silver',2),
    (3,'Gold',3);

select user_id_o, max(order_date) as recent
from orders
where subscription_order = 1
group by user_id_o
having datediff(curdate(),recent)= 30;


drop event if exists sub_order;
DELIMITER //
create event sub_order
	ON schedule
    every 1 day
    do
		BEGIN
		insert into orders
        select user_id_o as user, curdate() as today, 1 as sub_order
		from
		(select user_id_o, max(order_date) as recent
			from orders
			where subscription_order = 1
			group by user_id_o
			having datediff(curdate(),recent)= 30)ord
		left join user us on user_id_o = user_id
		left join subscription su on us.user_id = su.user_id
		left join recommendations on us.user_id = re_user_id
        where product_rank <= level_id;
        INSERT INTO 
		END;
        

        


