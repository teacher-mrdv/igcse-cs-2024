-- Example of setting up a relational database with 2 tables
-- SQLite3

.nullvalue NULL
.headers on
PRAGMA foreign_keys = ON;

CREATE TABLE Persons (
    PersonID int NOT NULL,
    PersonName TEXT NOT NULL,
    PersonEmail TEXT NOT NULL,
    PRIMARY KEY (PersonID)
);


CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);

INSERT INTO Persons (PersonID, PersonName, PersonEmail)
VALUES (123456, 'Juan Perez', 'js@home.org');

INSERT INTO Orders (OrderID, OrderNumber, PersonID)
VALUES (100001, 'Tooth paste', 123456);

PRAGMA table_info(Persons);
SELECT * FROM Persons;

PRAGMA table_info(Orders);
SELECT * FROM Orders;
