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



--

I had upgraded and uninstalled the right version of postgres.  To recover the data in 
```
/usr/local/var/postgres
```

I just needed to install an old version
```brew install postgresql@9.5```

Make sure that we point the installation to the right place:
```
export PATH="/usr/local/opt/postgresql@9.5/bin:$PATH"
```
And then start postgres pointing it at the folder where all the data was (note, no initdb required here - the data was all there already)

```
pg_ctl -D /usr/local/var/postgres -l logfile start
```
