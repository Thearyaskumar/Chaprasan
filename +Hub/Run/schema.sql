drop table if exists devices;
create table devices (
  location text primary key not null,
  inputs text not null,
  outputs text not null
);
