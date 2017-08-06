## Installing postgres on mac

Install postgres
```brew install postgres```

Initialise a database in folder postgres9.6
```
initdb /usr/local/var/postgres9.6 -E utf8
```

Start the postgres server
```
pg_ctl -D /usr/local/var/postgres9.6 -l logfile start
```

You can now connect. Note that username is your mac username `echo $USER`, not `postgres` like it is on Windows system.

If you have connection problems, go to 
```
/usr/local/var/postgres/postgresql.conf
```
