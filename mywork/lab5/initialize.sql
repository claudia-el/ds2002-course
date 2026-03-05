CREATE DATABASE staff;

USE staff;

CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT,
    first_name VARCHAR(25),
    last_name VARCHAR(25),
    start_date DATE,
    PRIMARY KEY (employee_id)
    
);

CREATE TABLE shift (
    shift_id INT AUTO_INCREMENT,
    employee_id INT,
    shift_date DATE,
    hours INT,
    manager VARCHAR(50),
    PRIMARY KEY (shift_id)
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
)

INSERT INTO employees (first_name, last_name, start_date) VALUES ("Alice", "Robbins", "2002-05-14")
INSERT INTO employees (first_name, last_name, start_date) VALUES ("Margo", "Fork", "2020-07-28")
INSERT INTO employees (first_name, last_name, start_date) VALUES ("Ethan", "Pearl", "2023-01-01")
INSERT INTO employees (first_name, last_name, start_date) VALUES ("Russel", "Wealth", "2000-03-31")
INSERT INTO employees (first_name, last_name, start_date) VALUES ("Lena", "Brussel", "2017-10-21")
INSERT INTO employees (first_name, last_name, start_date) VALUES ("Sabrina", "Moon", "2012-12-12")
INSERT INTO employees (first_name, last_name, start_date) VALUES ("Daniel", "Levinson", "2026-2-02")
INSERT INTO employees (first_name, last_name, start_date) VALUES ("Tyler", "Quilter", "2001-4-03")
INSERT INTO employees (first_name, last_name, start_date) VALUES ("Gina", "Homeston", "2010-8-11")
INSERT INTO employees (first_name, last_name, start_date) VALUES ("Fontaine", "Price", "2017-10-21")

INSERT INTO employees (employee_id, hours, manager) VALUES (1, 8, "2026-12-02", "Walterson")
INSERT INTO employees (employee_id, hours, manager) VALUES (1, 12, "2026-10-01", "Mincer")
INSERT INTO employees (employee_id, hours, manager) VALUES (3, 8, "2026-03-02", "Walterson")
INSERT INTO employees (employee_id, hours, manager) VALUES (5, 8, "2026-12-02", "Walterson")
INSERT INTO employees (employee_id, hours, manager) VALUES (2, 8, "2026-01-02", "Walterson")
INSERT INTO employees (employee_id, hours, manager) VALUES (6, 9, "2026-05-03", "Mincer")
INSERT INTO employees (employee_id, hours, manager) VALUES (9, 10, "2026-01-03", "Mincer")
INSERT INTO employees (employee_id, hours, manager) VALUES (8, 8, "2026-01-02", "Walterson")
INSERT INTO employees (employee_id, hours, manager) VALUES (10, 8, "2026-01-07", "Walterson")
INSERT INTO employees (employee_id, hours, manager) VALUES (7, 8, "2026-01-21", "Walterson")
INSERT INTO employees (employee_id, hours, manager) VALUES (4, 8, "2026-02-15", "Mincer")









