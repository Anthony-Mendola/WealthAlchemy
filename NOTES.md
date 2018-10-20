# SCHEMA NOTES

## MODEL/DB FIELDS

### OFFERING
id: INT
affiliate: INT (FOREIGN KEY [affiliate])
title: STR
industry: STR
description: TEXT
minimum: INT
annual_interest: INT
offering_size: INT
percent_funded: INT [0]
term: INT
is_published: BOOL [true]
is_open: BOOL [true]
offer_date: DATE
photo_main: STR
photo_1: STR
photo_2: STR
photo_3: STR



### AFFILIATE
id: INT
name: STR
photo: STR
description: TEXT
email: STR
phone: STR
is_mvp: BOOL [0]



### CONTACT
id: INT
user_id: INT
offering: INT
offering_id: INT
name: STR
email: STR
phone: STR
message: TEXT
contact_date: DATE



