create database lib;
use lib;
CREATE TABLE category (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(30)
);

CREATE TABLE library (
    book_id INT PRIMARY KEY,
    book_name VARCHAR(40),
    category_id INT,
    price INT,
    quantity INT
);

INSERT INTO category VALUES
(1, 'Programming'),
(2, 'Biography'),
(3, 'Science');

INSERT INTO library VALUES
(1, 'Python', 1, 500, 5),
(2, 'Java', 1, 600, 3),
(3, 'Wings', 2, 300, 4),
(4, 'SQL', 1, 400, 6),
(5, 'Physics', 3, 250, 2);

SELECT * FROM library;

SELECT * FROM library WHERE price > 400;

SELECT * FROM library ORDER BY price DESC;

UPDATE library SET price = 450 WHERE book_id = 4;

DELETE FROM library WHERE book_id = 5;

SELECT COUNT(*), SUM(quantity), AVG(price),
       MAX(price), MIN(price)
FROM library;

SELECT category_id, COUNT(*) AS total_books
FROM library
GROUP BY category_id;

SELECT category_id, AVG(price) AS average_price
FROM library
GROUP BY category_id
HAVING AVG(price) > 400;

-- INNER JOIN
SELECT library.book_name, category.category_name, library.price
FROM library
INNER JOIN category
ON library.category_id = category.category_id;

-- LEFT JOIN
SELECT library.book_name, category.category_name
FROM library
LEFT JOIN category
ON library.category_id = category.category_id;

-- RIGHT JOIN
SELECT library.book_name, category.category_name
FROM library
RIGHT JOIN category
ON library.category_id = category.category_id;

-- JOIN + WHERE
SELECT library.book_name, category.category_name, library.price
FROM library
INNER JOIN category
ON library.category_id = category.category_id
WHERE library.price > 400;

-- JOIN + GROUP BY + HAVING
SELECT category.category_name, SUM(library.quantity) AS total_quantity
FROM library
INNER JOIN category
ON library.category_id = category.category_id
GROUP BY category.category_name
HAVING SUM(library.quantity) > 5;

-- JOIN + ORDER BY
SELECT library.book_name, category.category_name, library.price
FROM library
INNER JOIN category
ON library.category_id = category.category_id
ORDER BY library.price DESC;