USE dke5td_db;

SELECT employees.first_name, employees.last_name, shift.shift_date, shift.manager, shift.hours
FROM employees
INNER JOIN shift ON employees.employee_id=shift.employee_id
WHERE shift.hours > 8;
