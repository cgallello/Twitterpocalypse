drop table if exists accounts;
create table accounts (
	id integer primary key autoincrement,
	app_key varchar(15),
	app_secret varchar(15),
	access_token varchar(15),
	access_secret varchar(15),
	kindle_email varchar(45),
	personal_email varchar(45),
	created timestamp default current_timestamp
);
