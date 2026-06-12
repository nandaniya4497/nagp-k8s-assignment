CREATE TABLE employees (
 id SERIAL PRIMARY KEY,
 name VARCHAR(50),
 department VARCHAR(50)
);

INSERT INTO employees(name, department)
VALUES
('John','IT'),
('Smith','HR'),
('David','Finance'),
('Lisa','Operations'),
('Peter','Marketing'),
('Tony','IT'),
('James','Support');