# Installing with Global Cache Enabled

Setting up caching with packrat with the following command.

```R
#Optional to set location of cache, may be useful if we want a global cache for shiny deployment? Can be saved in .Renviron, I think. 

#Sys.setenv(R_PACKRAT_CACHE_DIR = "/home/willbowditch/R/packratcache")

packrat::set_opts(use.cache=TRUE)
```



This is written to `packrat.opts`, which decides whether the cache is used when a project is opened in Rstudio. 

```
auto.snapshot: TRUE
use.cache: TRUE
print.banner.on.startup: auto
vcs.ignore.lib: TRUE
vcs.ignore.src: FALSE
external.packages:
local.repos:
load.external.packages.on.startup: TRUE
ignored.packages:
quiet.package.installation: TRUE
snapshot.recommended.packages: FALSE
snapshot.fields:
    Imports
    Depends
    LinkingTo
```



Both base libs and installed libs get stored in the cache and symlinked 

``` 	sh
./packrat/lib/x86_64-pc-linux-gnu/3.4.0:
total 2
drwxr-xr-x 2 willbowditch staff  4 Jun 14 16:21 .
drwxr-xr-x 3 willbowditch staff  3 Jun 14 16:20 ..
lrwxrwxrwx 1 willbowditch staff 99 Jun 14 16:21 CheckDigit -> /home/willbowditch/R/packratcache/v2/library/CheckDigit/0ab3083cafb11382646fdda41ddb8b98/CheckDigit
lrwxrwxrwx 1 willbowditch staff 93 Jun 14 16:21 packrat -> /home/willbowditch/R/packratcache/v2/library/packrat/6ad605ba7b4b476d84be6632393f5765/packrat

./packrat/lib-ext:
total 9
drwxr-xr-x 2 willbowditch staff 2 Jun 14 16:20 .
drwxr-xr-x 6 willbowditch staff 9 Jun 14 16:20 ..

./packrat/lib-R:
total 24
drwxr-xr-x 2 willbowditch staff 16 Jun 14 16:20 .
drwxr-xr-x 6 willbowditch staff  9 Jun 14 16:20 ..
lrwxrwxrwx 1 willbowditch staff 29 Jun 14 16:20 base -> /usr/local/lib/R/library/base
lrwxrwxrwx 1 willbowditch staff 33 Jun 14 16:20 compiler -> /usr/local/lib/R/library/compiler
lrwxrwxrwx 1 willbowditch staff 33 Jun 14 16:20 datasets -> /usr/local/lib/R/library/datasets
lrwxrwxrwx 1 willbowditch staff 33 Jun 14 16:20 graphics -> /usr/local/lib/R/library/graphics
lrwxrwxrwx 1 willbowditch staff 34 Jun 14 16:20 grDevices -> /usr/local/lib/R/library/grDevices
lrwxrwxrwx 1 willbowditch staff 29 Jun 14 16:20 grid -> /usr/local/lib/R/library/grid
lrwxrwxrwx 1 willbowditch staff 32 Jun 14 16:20 methods -> /usr/local/lib/R/library/methods
lrwxrwxrwx 1 willbowditch staff 33 Jun 14 16:20 parallel -> /usr/local/lib/R/library/parallel
lrwxrwxrwx 1 willbowditch staff 32 Jun 14 16:20 splines -> /usr/local/lib/R/library/splines
lrwxrwxrwx 1 willbowditch staff 30 Jun 14 16:20 stats -> /usr/local/lib/R/library/stats
lrwxrwxrwx 1 willbowditch staff 31 Jun 14 16:20 stats4 -> /usr/local/lib/R/library/stats4
lrwxrwxrwx 1 willbowditch staff 30 Jun 14 16:20 tcltk -> /usr/local/lib/R/library/tcltk
lrwxrwxrwx 1 willbowditch staff 30 Jun 14 16:20 tools -> /usr/local/lib/R/library/tools
lrwxrwxrwx 1 willbowditch staff 30 Jun 14 16:20 utils -> /usr/local/lib/R/library/utils
```

If you try and install a package it overwrites the symlink, rather than fetching the package from the cache, so it cannot be used to speed up the install of packages.

```R
install.packages('CheckDigit')
## Error: Can't find directory CheckDigit
```

But it **does** speed up the initiation of packrat projects that you are write a package using a cached repo an then `packrat::init()` or `packrat::restore()` . This only applies to packages that have already been used in a packrat. 

```
> packrat::init()
Initializing packrat project in directory:
- "~/six"
Fetching sources for BH (1.62.0-1) ... OK (CRAN current)
Fetching sources for DBI (0.6-1) ... OK (CRAN current)
Fetching sources for R6 (2.2.0) ... OK (CRAN current)
Fetching sources for Rcpp (0.12.10) ... OK (CRAN current)
Fetching sources for assertthat (0.2.0) ... OK (CRAN current)
Fetching sources for dplyr (0.5.0) ... OK (CRAN current)
Fetching sources for lazyeval (0.2.0) ... OK (CRAN current)
Fetching sources for magrittr (1.5) ... OK (CRAN current)
Fetching sources for packrat (0.4.8-1) ... OK (CRAN current)
Fetching sources for stringi (1.1.5) ... OK (CRAN current)
Fetching sources for tibble (1.3.0) ... OK (CRAN current)
Fetching sources for tidyr (0.6.2) ... OK (CRAN current)
Fetching sources for whisker (0.3-2) ... OK (CRAN current)
Snapshot written to '/home/willbowditch/six/packrat/packrat.lock'
Installing BH (1.62.0-1) ... 
	OK (symlinked cache)
Installing DBI (0.6-1) ... 
	OK (symlinked cache)
Installing R6 (2.2.0) ... 
	OK (symlinked cache)
Installing Rcpp (0.12.10) ... 
	OK (symlinked cache)
Installing assertthat (0.2.0) ... 
	OK (symlinked cache)
Installing lazyeval (0.2.0) ... 
	OK (symlinked cache)
Installing magrittr (1.5) ... 
	OK (symlinked cache)
Installing packrat (0.4.8-1) ... 
	OK (symlinked cache)
Installing stringi (1.1.5) ... 
	OK (symlinked cache)
Installing whisker (0.3-2) ... 
	OK (symlinked cache)
Installing tibble (1.3.0) ... 
	OK (symlinked cache)
Installing dplyr (0.5.0) ... 
	OK (symlinked cache)
Installing tidyr (0.6.2) ... 
	OK (symlinked cache)
Initialization complete!
```

In other words packages dont seem to go from global library to cache, but they can go from other packrat libraries to the cache. 

**If a cache could be shared across shiny deployment nodes then this would proably speed up the deployment of shiny apps significantly**



# Installing packages from the users home (~) library quickly

As far as I can tell you can't use packages that haven't already been installed in packrat to shorten loading times with the cache option. But there are a couple of workarounds I've explored.   

## Workaround 1

A straightforward workaround is to symlink the users package library to an empty packrat directory. Install time via this method is a few seconds and it doesn't seem to interfere with the process of creating a snapshot as long as `packrat::clean()` is run at the end of development. 

#### Steps

1. New Project > using packrat 

2. ```R
   source('https://raw.githubusercontent.com/willbowditch/ratpack/master/R/ratpack.R')
   symlink_packages()
   #Develop as normal then run 
   packrat::clean()
   packrat::snapshot(ignore.stale=TRUE) 
   ```

   ​

## Workaround 2

Packrat does provide a workaround for large packages with the `packrat::set_opts(external.packages=c('pkgname'))` command, **but** packages installed in this way aren't included in the packrat/src folder.

In effect, the option symlinks the package directories to the `packrat/lib-ext` diretory. 

I had a go at automating this, in the same way as the symlinking option - to grab all the users packages in their home directory and add them to the external.packages option. 

#### Steps

1. New Project > using packrat 

2. ```R
   source('https://raw.githubusercontent.com/willbowditch/ratpack/master/R/ratpack.R')
   import_user_packages()
   #All installed packages will now be accessable within the packrat session
   ```

3. To reset at the end of development 

   ```R
   packrat::set_opts(external.packages=NULL)
   packrat::snapshot()
   packrat::restore() #This step will install the packages if they're not in the cache
   ```



## The simplest option 

Somewhere in between these options might make the most sense - users currate their list of large but commonly used packages to be symlinked (i.e.`packrat::set_opts(external.packages=c('tidyverse', 'data.table'))` ) and then put up with installing smaller packages on a project by project basis. 

Not sure what this will mean for deployment….
