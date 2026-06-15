CREATE TABLE employees (
 id SERIAL PRIMARY KEY,
 name VARCHAR(50),
 department VARCHAR(50)
);

INSERT INTO employees(name, department)
VALUES
('Sanjay','IT'),
('Minaxi','HR'),
('Sagar','Finance'),
('Simaran','Operations'),
('Mitul','Marketing'),
('Meera','IT'),
('Monika','Support'),
('Nirav','Safety'),
('Hetvi','Production');