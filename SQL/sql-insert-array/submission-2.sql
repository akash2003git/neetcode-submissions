CREATE TABLE stocks (
  id INTEGER PRIMARY KEY,
  name TEXT,
  transaction_dates DATE[]
);

-- Do not modify above this line --

insert into stocks (id, name, transaction_dates) values 
(1, 'AAPL', array['2007-02-09', '2007-02-10', '2007-02-11']::date[]),
(2, 'GOOG', array['2004-12-15', '2004-12-16']::date[]);





-- Do not modify below this line --
SELECT * FROM stocks;
