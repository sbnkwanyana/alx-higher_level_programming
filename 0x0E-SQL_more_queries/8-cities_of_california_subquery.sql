-- selects the id and name from city table where the foreign key id matches the ids in the collection of selected Id from the states table
SELECT id, name FROM cities WHERE state_id IN (SELECT id FROM states WHERE name = "California");
