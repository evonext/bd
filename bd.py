ВНИМАНИЕ МАТЕРИАЛ НИЖЕ ПРЕДСТАВЛЕН ТОЛЬКО В ОБУЧАЮЩИХ ЦЕЛЯХ! ИСПОЛЬЗОВАНИЕ МАТЕРИАЛАХ В ИНЫХ ЦЕЛЯХ НЕ ПРЕДУСМОТРЕНО! 

Вопрос №1

Решите следующую задачу, используя диаграмму, приведенную на рис.1
а) Напишите SQL-запрос, возвращающий полное имя (имя и фамилию) сотрудника, идентификатор и название страны, в которой он в настоящее время работает. 
 

Ответ:
SELECT 
    e.employee_id, -- Идентификатор сотрудника
    e.first_name || ' ' || e.last_name AS full_name, -- Полное имя сотрудника (Имя + Фамилия)
    c.country_name -- Название страны, где работает сотрудник
FROM 
    employees e -- Основная таблица сотрудников (employees), присваиваем ей алиас 'e'
JOIN 
    departments d ON e.department_id = d.department_id -- Соединяем с таблицей departments по полю department_id
JOIN 
    locations l ON d.location_id = l.location_id -- Соединяем с таблицей locations по полю location_id
JOIN 
    countries c ON l.country_id = c.country_id; -- Соединяем с таблицей countries по полю country_id





Вопрос №2
Решите следующую задачу, используя диаграмму, приведенную на рис.1
а) Напишите запрос на SQL для вывода информации о названии отдела, средней зарплате и количестве сотрудников, работающих в этом отделе и получивших комиссионные.

 

Ответ:
SELECT hr.departments.department_name,
       AVG(hr.employees.salary) AS avg_salary,
       COUNT(*) AS num_employees
FROM hr.employees
JOIN hr.departments ON hr.employees.department_id = hr.departments.department_id
WHERE hr.employees.commission_pct IS NOT NULL
GROUP BY hr.departments.department_name;






Вопрос №3
Решите следующую задачу, используя диаграмму, приведенную на рис.1
а) Напишите SQL-запрос для вывода имени, фамилии и зарплаты всех сотрудников, работающих в Лондоне.
 

Ответ:
SELECT e.first_name, e.last_name, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
WHERE l.city = 'London';





Вопрос №4
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL-запрос, возвращающий идентификаторы, название должности и количество дней, отработанных сотрудниками в отделе с идентификатором 80. 
 

Ответ:
SELECT e.employee_id, j.job_title, 
       (jh.end_date - jh.start_date) AS days_worked
FROM employees e
JOIN job_history jh ON e.employee_id = jh.employee_id
JOIN jobs j ON e.job_id = j.job_id
WHERE jh.department_id = 80;



Вопрос №5
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL-запрос, возвращающий название отдела, имя, фамилию и город менеджера.
 

Ответ:
SELECT
    hr.employees.first_name,
    hr.employees.last_name,
    hr.departments.department_name,
    hr.locations.city
FROM
         hr.employees
JOIN hr.departments ON hr.employees.department_id = hr.departments.department_id
JOIN hr.locations ON hr.departments.location_id = hr.locations.location_id



Вопрос №6
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL-запрос для вывода списка сотрудников, которые зарабатывают 1800$ и более. Возвращает идентификатор сотрудника, дату начала, дату окончания, идентификатор вакансии и идентификатор отдела.

Ответ:
SELECT
    hr.job_history.employee_id,
    hr.job_history.start_date,
    hr.job_history.end_date,
    hr.job_history.job_id,
    hr.job_history.department_id,
    hr.employees.salary
FROM hr.job_history
JOIN hr.employees ON hr.employees.employee_id = hr.job_history.employee_id
WHERE hr.employees.salary >= 1800;





Вопрос №7
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) напишите SQL-запрос для расчета средней зарплаты сотрудников по каждой должности.
 

Ответ:
SELECT j.job_title,
       AVG(e.salary) AS avg_salary
FROM hr.employees e
JOIN hr.jobs j ON e.job_id = j.job_id
GROUP BY j.job_title;



Вопрос №8
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) напишите SQL-запрос для расчета разницы между максимальной зарплатой и зарплатой всех сотрудников, работающих в отделе с идентификатором 110. Возвращает название должности, имя сотрудника и разницу в зарплате.
 

Ответ:
SELECT 
    e.JOB_ID,
    e.FIRST_NAME,
    (max_salary - e.salary) AS salary_difference
FROM 
    employees e,
    (SELECT MAX(salary) AS max_salary
     FROM employees
     WHERE department_id = 110) m
WHERE 
    e.department_id = 110;

(В вопросе не понятно как и что именно выводить, в отделе 110 всего 2 сотрудника и скрипт выводит их должность, имена и разница в зарплате, так как у первого зарплата максимальная для департамента он выводит что разница в зарплате у него 0)




Вопрос №9
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) напишите SQL-запрос для вывода списка тех сотрудников (фамилия, имя), которые получают более высокую зарплату, чем сотрудник с идентификатором 124.
 

Ответ:
SELECT 
    e.last_name,
    e.first_name
FROM 
    hr.employees e
WHERE 
    e.salary > (SELECT salary FROM hr.employees WHERE employee_id = 124);





Вопрос №10
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) напишите запрос SQL, возвращающий названия, идентификаторы отделов, количество сотрудников в которых больше 20 человек.
 

Ответ:
SELECT 
    d.department_id, d.department_name, COUNT(e.employee_id) AS NumberOfEmployees
FROM 
    departments d
JOIN 
    employees e ON d.department_id = e.department_id
GROUP BY 
    d.department_id, d.department_name
HAVING 
    COUNT(e.employee_id) > 20;





Вопрос №11
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) напишите SQL-запрос, возвращающий название страны, города и количество отделов, в которых работают не менее 2 сотрудников. 
 

Ответ:
SELECT 
    hr.countries.country_name,
    hr.locations.city,
    COUNT(hr.departments.department_id) AS number_of_departments
FROM
    hr.departments
JOIN
    hr.employees ON hr.departments.department_id = hr.employees.department_id
JOIN
    hr.locations ON hr.departments.location_id = hr.locations.location_id
JOIN
    hr.countries ON hr.locations.country_id = hr.countries.country_id
GROUP BY
    hr.countries.country_name,
    hr.locations.city
HAVING
    COUNT(hr.employees.employee_id) >= 2;





Вопрос №12
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) напишите SQL-запрос, возвращающий имена, фамилии, идентификаторы и зарплату сотрудников, которые подчиняются менеджеру с фамилией Hunold. 
 

Ответ:
SELECT e.first_name, e.last_name, e.employee_id, e.salary
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id
WHERE m.last_name = 'Hunold';




Вопрос №13
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL-запрос для вывода полной информации о сотрудниках, чья зарплата находится в диапазоне от наименьшей зарплаты до 2500. 
 

Ответ:
SELECT * FROM employees
WHERE salary BETWEEN (SELECT MIN(salary) FROM employees) AND 2500;



Вопрос №14
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL-запрос, возвращающий имена, фамилии и дату приема на работу тех сотрудников, которые работают в том же отделе, что и «Hall». Исключите записи, содержащие фамилию «Hall». 
 

Ответ:
SELECT e.first_name, e.last_name, e.hire_date
FROM employees e
WHERE e.department_id = (SELECT department_id 
FROM employees 
WHERE last_name = 'Hall')
AND e.last_name <> 'Hall';




Вопрос №15
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL-запрос, возвращающий список тех сотрудников, которые работают в отделе, название которого начинается с символа «S».
 

Ответ:
SELECT e.employee_id,
       e.first_name,
       e.last_name,
       d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE d.department_name LIKE 'S%';




Вопрос №16
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL-запрос для вывода информации о тех сотрудниках, зарплата которых ниже, чем у сотрудников, работающих на должности «SH_CLERK». 
 

Ответ:
SELECT e.employee_id, e.first_name || ' ' || e.last_name AS full_name, e.salary, e.job_id
FROM hr.employees e
WHERE e.salary < (
    SELECT MIN(salary)
    FROM hr.employees ee
    WHERE ee.job_id = 'SH_CLERK'
);



Вопрос №17
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL-запрос, возвращающий список тех сотрудников, зарплата которых выше средней по всем отделам.
 

Ответ:
SELECT e.employee_id, e.first_name, e.last_name, e.salary FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > (
SELECT AVG(salary) FROM employees
);



Вопрос №18
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL-запрос для расчета средней зарплаты и количества сотрудников, получающих комиссионные в этом отделе. Возвращает название отдела, среднюю зарплату и количество сотрудников.
 

Ответ:
SELECT hr.departments.department_name,
       AVG(hr.employees.salary) AS avg_salary,
       COUNT(*) AS num_employees
FROM hr.employees
JOIN hr.departments ON hr.employees.department_id = hr.departments.department_id
WHERE hr.employees.commission_pct IS NOT NULL
GROUP BY hr.departments.department_name;





Вопрос №19
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL-запрос, возвращающий список сотрудников, которые были приняты на работу 1 января 1993 г. или после этой даты и 31 августа 1997 г. или ранее. Возвращает название должности, название отдела, имя, фамилию сотрудника и дату вступления в должность.
 

Ответ:
SELECT j.job_title, d.department_name, e.first_name, e.last_name, e.hire_date
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
JOIN departments d ON e.department_id = d.department_id
WHERE e.hire_date BETWEEN TO_DATE('1993-01-01', 'YYYY-MM-DD') AND TO_DATE('1997-08-31', 'YYYY-MM-DD');




Вопрос №20. 
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL-запрос для вывода списка менеджеров, имеющих в подчинении больше шести сотрудников.
 

Ответ:
SELECT manager_id FROM employees
GROUP BY manager_id
HAVING COUNT(*) > 6




Вопрос №21
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL-запрос, возвращающий список отделов, в которых максимальная зарплата превышает 10000.
 

Ответ:
SELECT * FROM departments
WHERE department_id IN (
    SELECT department_id FROM employees
    WHERE salary > 10000
)





Вопрос №22
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL-запрос, возвращающий список отделов, включая те, в которых нет сотрудников. 
 

Ответ:
SELECT d.department_id, d.department_name, e.employee_id  -- Выбираем идентификатор отдела, название отдела и идентификатор сотрудника
FROM departments d  -- Таблица departments становится основной таблицей для запроса
LEFT JOIN employees e ON d.department_id = e.department_id;  -- Используем LEFT JOIN, чтобы включить все отделы, даже если у них нет сотрудников





Вопрос №23
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL запрос для вывода списка сотрудников отдела 80, получающих оклад больше любого в отделе 100.
 

Ответ:
SELECT e.first_name, e.last_name, e.salary  -- Выбираем поля first_name, last_name и salary из таблицы employees с псевдонимом e
FROM employees e                             -- Из таблицы employees используем псевдоним e для удобства
WHERE e.department_id = 80                   -- Фильтруем записи, выбираем только тех сотрудников, которые работают в отделе с ID 80
  AND e.salary > (                           -- И чья зарплата больше максимальной зарплаты среди сотрудников отдела с ID 100
    SELECT MAX(e2.salary)                   -- Подзапрос для нахождения максимальной зарплаты в отделе с ID 100
    FROM employees e2                        -- Из таблицы employees используем псевдоним e2 для удобства
    WHERE e2.department_id = 100             -- Фильтруем записи, выбираем только тех сотрудников, которые работают в отделе с ID 100);





Вопрос №24
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL запрос, возвращающий название города сотрудника, чей идентификатор равен 105.
 

Ответ:
SELECT l.city
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
WHERE e.employee_id = 105;





Вопрос №25
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL запрос для вывода информации о текущей работе для сотрудников, которые ранее работали ИТ-программистами (IT_PROG).
 

Ответ:
SELECT e.employee_id,
       e.first_name,
       e.last_name,
       e.job_id,
       j.job_title
FROM employees e
JOIN job_history jh ON e.employee_id = jh.employee_id
JOIN jobs j ON e.job_id = j.job_id
WHERE jh.job_id = 'IT_PROG';



Вопрос №26
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL запрос, возвращающий имя, фамилию, номер и название отдела для всех сотрудников, работающих в отделах 80 или 40. 
 

Ответ:
SELECT e.first_name, e.last_name, e.employee_id, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.department_id IN (80, 40);



Вопрос №27
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL-запрос, возвращающий имена всех сотрудников, включая имя их руководителя (менеджера). 
 

Ответ:
SELECT e.first_name AS employee_first_name,
       e.last_name AS employee_last_name,
       m.first_name AS manager_first_name,
       m.last_name AS manager_last_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;




Вопрос №28
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL-запрос для вывода списка отделов, в которых более пяти сотрудников имеют комиссионный процент (commission_pct).
 

Ответ:
SELECT d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.commission_pct IS NOT NULL
GROUP BY d.department_name
HAVING COUNT(e.employee_id) > 5;




Вопрос №29
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL-запрос, возвращающий года, когда в компанию были приняты более 10 сотрудников.
 

Ответ:
SELECT
    TO_CHAR(hire_date, 'YYYY') AS hire_year,
    COUNT(*) AS num_hires
FROM
    employees
GROUP BY
    TO_CHAR(hire_date, 'YYYY')
HAVING
    COUNT(*) > 10;




Вопрос №30
Решите следующую задачу, используя диаграмму, приведенную на рис.1
a) Напишите SQL-запрос для вывода списка сотрудников, имеющих оклад больше оклада своего руководителя (менеджера).
 

Ответ:
SELECT e.first_name, e.last_name, e.salary
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id
WHERE e.salary > m.salary;

