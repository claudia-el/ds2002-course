USE dke5td_db;


INSERT INTO employees (first_name, last_name, start_date) VALUES ('Olivia', 'Benson', '2026-04-01');
INSERT INTO employees (first_name, last_name, start_date) VALUES ('Liam', 'Turner', '2026-03-15');
INSERT INTO employees (first_name, last_name, start_date) VALUES ('Noah', 'Harris', '2026-02-20');


INSERT INTO shift (employee_id, hours, shift_date, manager) VALUES (11, 8, '2026-04-05', 'Mincer'); 
INSERT INTO shift (employee_id, hours, shift_date, manager) VALUES (12, 10, '2026-04-06', 'Walterson');