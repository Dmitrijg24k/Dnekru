USE ELSCDnevnik;
SELECT * FROM Students;
SELECT LOCATE('А', FullName) FROM Students;
SELECT LEFT(FullName, 3) FROM Students;
SELECT SUBSTRING(FullName, 3, 4) FROM Students;
SELECT REVERSE(FullName) FROM Students;
SELECT LOWER(FullName) FROM Students;
-----------
SELECT ABS(Cabinets) FROM Classes;
SELECT ROUND(Cabinets, 2) FROM Classes;
SELECT FLOOR(Cabinets) FROM Classes;
SELECT SQRT(Cabinets) FROM Classes;
SELECT COS(Floor) FROM Classes;
----------------
SELECT CURDATE();
SELECT CURTIME();
SELECT DAY(ReceiptDate) FROM Students;
SELECT MONTH(ReceiptDate) FROM Students;
SELECT YEAR(ReceiptDate) FROM Students;
SELECT MONTHNAME(ReceiptDate) FROM Students;

