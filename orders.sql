CREATE TABLE Orders (
    OrderID SERIAL PRIMARY KEY,
    Segment VARCHAR(50),
    CustomerID INT,
    OrderDate TIMESTAMP,
    ShippingType VARCHAR(50),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
