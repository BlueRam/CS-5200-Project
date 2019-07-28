drop database if exists coffee_database; 
create database if not exists coffee_database;

use coffee_database; 


drop table if exists user;  

create table user(
user_id int primary key auto_increment,
total_name varchar(250) not null, 
username varchar(250) not null,
password varchar(250) not null, 
email varchar(250) not null, 
address varchar(250) not null, 
subscriber tinyint default 0,
dob date not null, 
drink_frequency enum('1','2','3','4','5+'), 
roast_preference enum('light', 'medium', 'dark', 'espresso'), 
gender varchar(50));  


drop table if exists coffee_products;

create table coffee_products(
coffee_id int primary key auto_increment, 
title varchar(500) not null, 
roast enum('light', 'medium', 'dark', 'espresso'),
price double not null, 
description varchar(1000) not null, 
remaining int not null); 


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


drop table if exists reviews;

create table reviews( 
reviewer_id int primary key auto_increment,
coffee_id_r int not null,
rating varchar(50), 
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
date_subscribed datetime not null, 
membership enum('Gold', 'Silver', 'Bronze') not null, 
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
constraint coffee_id_co foreign key (coffee_id_co) references coffee_products (coffee_id), 
constraint order_id_co foreign key (order_id_co) references orders (order_id)); 


drop table if exists recomendations;

create table recommendations(
re_user_id int not null,
re_coffee_id int,
product_rank int,
constraint re_user_id foreign key (re_user_id) references user (user_id),
constraint re_coffee_id foreign key (re_coffee_id) references coffee_products (coffee_id));


-- Adding Data to Subscription Level Table -- 
insert into subscription_level(level_id, level_name, coffee_amount)
values 
(1, "Gold", 3),
(2, "Silver", 2),
(3, "Bronze", 1);  


-- Verifying Presence of Tables -- 
show tables;

select * from aroma; 
select * from aroma_coffee;
select * from coffee_order; 
select * from coffee_products; 
select * from coffee_to_farm; 
select * from farm; 
select * from orders; 
select * from origin; 
select * from reviews; 
select * from recommendations;
select * from subscription;
select * from subscription_level;
select * from user;

