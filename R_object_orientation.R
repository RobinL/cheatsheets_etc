makeCacheMatrix <- function( m = matrix() ) {

	## Initialize the inverse property
    i <- NULL

    ## Method to set the matrix
    set <- function( matrix ) {
            m <<- matrix
            i <<- NULL
    }

    ## Method the get the matrix
    get <- function() {
    	## Return the matrix
    	m
    }

    ## Method to set the inverse of the matrix
    setInverse <- function(inverse) {
        i <<- inverse
    }

    ## Method to get the inverse of the matrix
    getInverse <- function() {
        ## Return the inverse property
        i
    }

    ## Return a list of the methods
    list(set = set, get = get,
         setInverse = setInverse,
         getInverse = getInverse)
}

# Note that you cannot do something like this:

rc_factory <- function() {
  
  creds <- list()
  creds$a <- 1
  myvar <- 1
  
  creds$update <- function() {
    creds$a <<- creds$a + 1
    myvar <<- myvar + 1
  }
  
  creds
  
}
creds <- rc_factory()
creds$update()
creds$a
# One way to think about this is that R passes everything by value rather than reference, so the creds which is returned is actually a copy of crds
# See https://stackoverflow.com/questions/44822994/accessing-variables-in-closure-in-r
