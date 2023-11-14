create table if not exists dummy
(
    id varchar
        constraint dummy_pk primary key
);

insert into dummy (id)
values ('dummy-table-id-1')
on conflict on constraint dummy_pk do nothing;