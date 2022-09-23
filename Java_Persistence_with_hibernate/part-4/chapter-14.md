# Chapter-14: Creating and executing queries

## Major new features in JPA 2
- We can now declare up front the type of a query result with the new **TypedQuery** interface.
- We can programmatically save a **Query(JPQL, criteria or native SQL)** for later use as a named query.
- **In addition to being able to set query parameters, hints, maximum results, and flush an lock modes, JPA 2 extends the Query API with various getter methods for obtaining the current settings.**
- JPA now standardizes **several query hints (timeout, cache usage).**

## Criteria queries
- JPA returns a query with a `javax.persistence.Query` or `javax.persistence.TypedQuery` instance.
- We create queries with the `EntityManager#createQuery()` method and it's variants.
- We can write the query in the JPQL, construct it with the `CriteriaBuilder` and `CriteriaQuery` APIs, or use plain SQL.

## The JPA query interfaces
- To retrieve all `Item` entity instances from the database we can use such JPQL query
```
Query query = em.createQuery("select i from Item i");
``` 
- The JPA provider returns a fresh `Query` and so far Hibernate hasn't sent any SQL to the database. Further preparation and execution of the query are seperate steps.
- **JPQL is compact and instead of table and column names, JPQL relies on entity class and property names.**
- Except for these class and property names, **JPQL is case-insensitive, so it doesn't matter whether we write `SeLEct` or `select`.**
- **In larger applications, we can move the query strings out of our data-access code and into annotations or XML.** A query is then accessed by name with `EntityManager#createNamedQuery()`.
- **A signinficant disadvantage of JPQL surfaces as problems during refactoring of the domain model, if we rename the `Item` class, our JPQL query will break.**

| Keyword       | JPA                                                                                                                                           | Hibernate                                                                                                                         |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Location      | Described in `javax.persistence` package                                                                                                      | Described in `org.hibernate`                                                                                                      |
| Intent        | It's only Java speicification                                                                                                                 | It's is an implementation of JPA.                                                                                                 |
| Functionality | It describes the handling of relational data in Java applications                                                                             | Hibernate is an Obejct relational mapping (ORM) tool that is used to save the Java objects in the relational database system      |
| Standard API  | It's a standard API that permits to perform database operations                                                                               | It is used in mapping Java data types with SQL data types and database tables                                                     |
| CRUD action   | To perform CRUD actions for instances of mapped entity classes, it uses `EntityManager` interface which is supplied by `EntityManagerFactory` | To perform CRUD actions for instances of mapped entity classes, it uses `Session` interface which is supplied by `SessionFactory` |