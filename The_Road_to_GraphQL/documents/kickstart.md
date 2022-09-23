## GraphQL
- When it comes to network requests between client and server applications, REST is one of the most popular choices to connect both worlds.
- GraphQL is an open source query language created by Facebook which went open source in 2015.
- **Overfetching:** A client application has to read multiple resources through mutliple network requests. This is overfetching.
- A query language like GraphQL on the server-side and client-side lets the client decide which data it needs by making a single request to the server.
- **Network usage was reduced dramatically for Facebook's mobile applications as a result, because GraphQL made it more efficient with data transfers.**
- A GraphQL operation is either a **query(read)**, **mutation(write)** or **subscription(continuous read)**.
- GraphQL is not opinionated about the network layer, which is often HTTP, nor about the payload format, which is usually JSON. It's not opinionated about the application architecture at all. It's only a query language.

### Code Playground
- **A GraphQL query:**
```GraphQL
author(id: "7") {
    id
    name
    avatarUrl
    articles(limit: 2) {
        name
        urlSlug
    }
}
```

- **A GraphQL query result:**
```GraphQL
{
  "data": {
    "author": {
      "id": "7",
      "name": "Robin Wieruch",
      "avatarUrl": "https://domain.com/authors/7",
      "articles": [
        {
          "name": "The Road to learn React",
          "urlSlug": "the-road-to-learn-react"
        },
        {
          "name": "React Testing Tutorial",
          "urlSlug": "react-testing-tutorial"
        }
      ]
    }
  }
}
```
- A RESTful architecture needs at least two waterfall requests to retrieve the author entity and its articles, but the GraphQL query made it happen in one.In addition, the query only selected the necessary fields instead of the whole entity.
- **The sever application offers a GraphQL schema, where it defines all available data with it's hierarchy and types, and a client application only queries the required data.**

## GraphQL Advantages
- **Declarative Data Fetching:**
  - **UI driven data fetching:** GraphQL embraces declarative data fetching with its queries. The client selects data along with its enetities with fields across in one query request. GraphQL decides which fields are needed for it's UI and it almost acts as UI-driven data fetching.
- **No overfetching with GraphQL:**
  - There is no overfetching with GraphQL. A mobile client usually overfetches data when there is an idential API as the web client with a RESTful API.
  - With GraphQL, the mobile client can choose a different set of fields, so it can fetch only the information needed for what's onscreen.
- **GrapQL for React, Angular, Node and Co.**
  - While Facebook showcased GraphQL on a client side application with React, it is decoupled from any frontend or backend solution.
  - The reference implementation of GraphQL is written in JavaScript, so the usage of GraphQL in Angular, Vue, Express, Hapi, Koa and other JavaScript libraries on the client-side and server-side is possible, and that's just the JavaScript ecosystem.

- **Single Source of Truth**
  - The GraphQL schema is the single source of truth in GraphQL applcations. It provides a central location, where all available data is described.
  - The GraphQL schema is usually defined on server-side, but clients can read(query) and write(mutation) data based on the schema.
  - Essentially the server-side application offers all information about what is available on it's side, and the client-side application asks for part of it by performing GraphQL queries, or alters part of it using GraphQL mutations.

- **GraphQL Schema Stiching**
  - Schema Stiching makes it possible to create one schema out of multiple schemas.
  - Each microservice can have it's own GraphQL endpoint, where one GraphQL API gateway consolidates all schemas into one global schema.

- **GraphQL Introspection**
  - A GraphQL Introspection makes it possible to retrieve the GraphQL schema from a GraphQL API.
  - It can also be used to mock the GraphQL schema client-side for testing or retrieving schemas from multiple microservices during schema stiching.

- **Strongly typed GraphQL**
  - GraphQL is a strongly typed query language because it is written in the expressive GraphQL Schema Definition Language(SDL).
  - Being strongly typed makes GraphQL less error prone, can be validated during compile-time.

- **GraphQL versioning**
  - In GraphQL there are no API versions as there used to be in REST and it's possible to deprecate an API on a field level.

## Should i go all in GraphQL?
- While migrating from a monolithic backend application to a microservice architecture is the perfect time to offer a GraphQL API for new microservices.
- With multiple microservices teams can introduce a GraphQL gateway with schema stiching to consolidate a global schema.
- The API gateway is also used for the monolithic REST application.

## GraphQL Disadvantages
- **Query Complexity**
  - People often GraphQL as a replacement for server-side databases, but it's just a query language.
  - Whether the request was made in a RESTful architecture or GraphQL, the varied resources and fields still have to be retrieved from a data source.
  - As a result, problems arise when client requests too many nested fields at once.
  - There must be a mechanism like **maximum query depths, query complexity weighting, avoiding recursion, or persistent queries** for stopping inefficient requests from the other side.