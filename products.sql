CREATE TABLE Products (
    ProductID SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    CategoryID INT,
    Price DECIMAL(10, 2),
    Cost DECIMAL(10, 2)
);
