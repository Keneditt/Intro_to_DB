-- Get full description of books table
SELECT 
    COLUMN_NAME AS 'Field',
    COLUMN_TYPE AS 'Type',
    IF(IS_NULLABLE = 'NO', 'NO', 'YES') AS 'Null',
    COLUMN_KEY AS 'Key',
    COLUMN_DEFAULT AS 'Default',
    EXTRA AS 'Extra'
FROM INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = 'alx_book_store'
    AND TABLE_NAME = 'books'
ORDER BY ORDINAL_POSITION;