CREATE TABLE Customers (
    CustomerID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    StreetAddress VARCHAR(200),
    City VARCHAR(50),
    State VARCHAR(50),
    PostalCode VARCHAR(20),
    Country VARCHAR(50) DEFAULT 'United States',
    DateOfBirth DATE,
    RegistrationDate TIMESTAMP,
    IsActive BOOLEAN,
    Latitude DECIMAL(9,6),
    Longitude DECIMAL(9,6)
);
