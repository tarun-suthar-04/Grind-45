USE grind;

INSERT INTO customers (cname, email, city)
VALUES
('Aarav Sharma', 'aarav@example.com', 'Jaipur'),
('Priya Verma', 'priya@example.com', 'Ajmer'),
('Rahul Singh', 'rahul@example.com', 'Delhi'),
('Neha Patel', 'neha@example.com', 'Indore'),
('Vikram Joshi', 'vikram@example.com', 'Kota'),
('Ananya Gupta', 'ananya@example.com', 'Udaipur');

INSERT INTO products (pname, price, stock)
VALUES
('Laptop', 55000.00, 10),
('Mouse', 800.00, 50),
('Keyboard', 1500.00, 30),
('Monitor', 12000.00, 15),
('Headphones', 2500.00, 25),
('Webcam', 3500.00, 20),
('Printer', 9000.00, 8);


INSERT INTO orders (cid, order_date)
VALUES
(1, '2026-10-01'),
(2, '2026-10-02'),
(1, '2026-10-03'),
(3, '2026-10-04'),
(4, '2026-10-05'),
(2, '2026-10-06'),
(5, '2026-10-07'),
(3, '2026-10-08'),
(1, '2026-10-09'),
(4, '2026-10-10');

INSERT INTO order_items (Oid, pid, quantity, unit_price)
VALUES
(1, 1, 1, 55000.00),
(1, 2, 2, 800.00),
(2, 3, 1, 1500.00),
(2, 5, 2, 2500.00),
(3, 4, 1, 12000.00),
(3, 2, 1, 800.00),
(4, 1, 1, 55000.00),
(4, 6, 1, 3500.00),
(5, 5, 1, 2500.00),
(5, 3, 2, 1500.00),
(6, 2, 3, 800.00),
(6, 6, 1, 3500.00),
(7, 4, 2, 12000.00),
(8, 3, 1, 1500.00),
(9, 1, 1, 55000.00);