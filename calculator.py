    CREATE OR REPLACE FUNCTION calculadora(num1 DOUBLE, num2 DOUBLE, operacao STRING)
    RETURNS DOUBLE
    LANGUAGE SQL
    RETURN
    CASE
        WHEN operacao = '+' THEN num1 + num2
        WHEN operacao = '-' THEN num1 - num2
        WHEN operacao = '*' THEN num1 * num2
        WHEN operacao = '/' THEN num1 / num2
        ELSE NULL
    END;