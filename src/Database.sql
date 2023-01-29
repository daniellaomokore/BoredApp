CREATE DATABASE BoredApp_users;
USE BoredApp_users;

-- CREATING THE Database Tables:

CREATE TABLE the_users (
    UserID int(10) AUTO_INCREMENT NOT NULL UNIQUE,
    FirstName varchar(65),
	LastName varchar(65),
    Email varchar(65) UNIQUE,
    DOB DATE,
    City varchar(65),
    Username varchar(65) UNIQUE,
	Password varchar(65),
    CONSTRAINT pk_the_users PRIMARY KEY (UserID)
    );

CREATE TABLE favourites (
    activityID int(10) NOT NULL UNIQUE,
	UserID int(10) NOT NULL ,
    activity varchar(1000) NOT NULL,
    participants int(100) NOT NULL,
    price float NOT NULL,
    type varchar(20) NOT NULL,
    CONSTRAINT pk_favourites PRIMARY KEY (activityID),
    CONSTRAINT fk_favourites FOREIGN KEY (UserID) REFERENCES the_users (UserID)
    );


--  DEFAULT DATA TO POPULATE THE 'the_users' TABLE WITH

INSERT INTO the_users (FirstName, LastName, Email, DOB, City, Username, Password)
VALUES ('Jake', 'Callow', 'jcal@email.com', str_to_date('05-12-1992', '%d-%m-%Y'), 'London', 'jcal11', 'Cat123!'),
('Fred', 'Smith', 'fsmith@email.com', str_to_date('19-02-1995', '%d-%m-%Y'),'Bristol', 'freddy95', 'bristol11!'),
('Hayley', 'Bieber', 'hayley99@email.com', str_to_date('01-09-1997', '%d-%m-%Y'), 'Cambridge', 'hbieber1997!', 'ilovejustin!1'),
('Luciano', 'Sovino', 'lucosovino89@email.com', str_to_date('02-10-1989', '%d-%m-%Y'), 'Cardiff', 'lucosov89', 'helloworld!0');
