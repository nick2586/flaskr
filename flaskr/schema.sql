drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null,
  user text not null
);
drop table if exists users;
create table users (
  id integer primary key autoincrement,
  user_id text not null unique,
  password text not null
);