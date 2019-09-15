Querying graphql json from `gatsby-transformer-json`

```
query nbds {
  allMydataJson(filter: {id: {eq: "1"}}) {
    nodes {
      p
      id
    }
  }
}
```

or 
```
query nbds {
  mydataJson(id: {eq: "2"}) {
    id
    p
  }
}

```

This will only ever return one result, even with no query
