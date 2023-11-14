create table if not exists dummy_uuid
(
    id varchar
        constraint dummy_uuid_pk primary key
);

insert into dummy_uuid (id)
values ('dummy-uuid-id-1')
on conflict on constraint dummy_uuid_pk do nothing;