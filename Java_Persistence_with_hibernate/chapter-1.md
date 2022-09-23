## What is persistence?
- Objecte persistence means **individual objects can outlive the application process**. 
- **They can be saved to a data store and be re-created at a later point in time**.
- **When we talk about persistence in Java, we are normally talking about mapping and storing object instances in a database using SQL.**

## Understanding SQL
- **We use SQL as a DDL(Data definition language) when creating, altering, and dropping artifacts such as tables and constraints in the catalog of the DBMS.**
- **When the schema is ready, we use SQL as a DML(Data manipulation language) to perform operations on data, including insertions, updates and deletions.**
- **We retrieve data by executing queries with `restrictions`, `projections` and `cartesian products`.**
- **For Efficient reporting, we use SQL to `join`, `aggregate` and `group` data as necessary.**
- **Subselect:** We can even nest SQL statements inside each other an technique that uses `subselects`.
- **schema evolution:** When our business requirements change, we'll have to modify the database schema again with DDL statements after data has been stored. This is known as `schema evolution`.

## Relational systems at internet scale
- **CAP theorem:** A distributed system can not be consistent, available and tolerant against partition failures all at the same time.
- That's why relational systems, and the data integrity guarantees associated with them are difficult to scale.