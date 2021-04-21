drop table if exists users;
    create table admins (
    id integer primary key autoincrement,
    username text unique not null,
    password text not null
);
