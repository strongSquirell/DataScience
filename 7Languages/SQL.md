### Create database
```
CREATE DATABASE IF NOT EXISTS article;
```

### Create table
```
CREATE TABLE `table1` (`user_id` INT(5) NOT NULL AUTO_INCREMENT, `username` VARCHAR(50), PRIMARY KEY(`user_id`), INDEX(`username`));
CREATE TABLE `table2` (`phone_id` INT(5) NOT NULL AUTO_INCREMENT, `user_id` INT(5) NOT NULL, phone_number INT(10) NOT NULL, PRIMARY KEY (`phone_id`), INDEX(`user_id`, `phone_number`));
CREATE TABLE `table3` (`room_id` INT(5) NOT NULL AUTO_INCREMENT, `phone_id` INT(5) NOT NULL, `room_number` INT(4) NOT NULL, PRIMARY KEY(`room_id`), INDEX(`phone_id`, `room_number`));
```

Additional commands
```
SHOW TABLES
INSERT INTO table1 (username) VALUE ('foo'); 
UPDATE table2 SET user_id='2', phone_number='200' WHERE phone_id='1';
DELETE FROM table1 WHERE user_id = 1; 
RENAME TABLE table1 TO nya; 
ALTER TABLE table1 CHANGE user_id id INT; 
ALTER TABLE table2 MODIFY phone_number VARCHAR(100) NOT NULL; 
ALTER TABLE table3 ADD abra  DATE; 
DESCRIBE table1; 
```

### SELECT
```
SELECT * FROM table1; 
SELECT username FROM table1 ORDER BY username DESC;
SELECT phone_id, user_id FROM table2 WHERE phone_number=200 LIMIT 1, 3;
```

### JOIN
INNER JOIN (CROSS JOIN)  
LEFT/RIGHT JOIN  
```
SELECT table3.room_number FROM table1 INNER JOIN table2 USING(user_id) INNER JOIN table3 USING(phone_id) WHERE table1.username = 'qux'; 
SELECT table3.room_number FROM table1 INNER JOIN table2 ON table1.user_id = table2.user_id INNER JOIN table3 ON table2.phone_id = table3.phone_id WHERE table1.username = 'qux';
SELECT * FROM nomenclature AS t1 JOIN nomenclature AS t2 LEFT JOIN nomenclature AS t3 ON t1.id = t3.id AND t2.id = t1.id;
```

### Nested SELECT
```
SELECT * FROM table1 WHERE id NOT IN (SELECT id FROM table2);
SELECT * FROM table1 WHERE NOT EXISTS (SELECT id FROM table2
         WHERE table1.id=table2.id);
SELECT a.name FROM (SELECT name FROM agentinformation) a
```