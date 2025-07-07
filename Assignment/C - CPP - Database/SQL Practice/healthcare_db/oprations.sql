drop view patient_age_group_view;

CREATE VIEW patient_age_group_view_by_gender AS
SELECT
  CASE 
    WHEN FLOOR(DATEDIFF(CURDATE(), date_of_birth) / 365) BETWEEN 0 AND 10 THEN '0-10'
    WHEN FLOOR(DATEDIFF(CURDATE(), date_of_birth) / 365) BETWEEN 11 AND 20 THEN '11-20'
    WHEN FLOOR(DATEDIFF(CURDATE(), date_of_birth) / 365) BETWEEN 21 AND 30 THEN '21-30'
    WHEN FLOOR(DATEDIFF(CURDATE(), date_of_birth) / 365) BETWEEN 31 AND 40 THEN '31-40'
    WHEN FLOOR(DATEDIFF(CURDATE(), date_of_birth) / 365) BETWEEN 41 AND 50 THEN '41-50'
    WHEN FLOOR(DATEDIFF(CURDATE(), date_of_birth) / 365) BETWEEN 51 AND 60 THEN '51-60'
    ELSE '61+'
  END AS age_group,
  gender
FROM patients;

SELECT age_group, gender, COUNT(*) AS total_patients
FROM patient_age_group_view_by_gender
GROUP BY age_group, gender
ORDER BY age_group, gender;



CREATE VIEW patient_age_group_view AS
SELECT
  CASE 
    WHEN FLOOR(DATEDIFF(CURDATE(), date_of_birth) / 365) BETWEEN 0 AND 10 THEN '0-10'
    WHEN FLOOR(DATEDIFF(CURDATE(), date_of_birth) / 365) BETWEEN 11 AND 20 THEN '11-20'
    WHEN FLOOR(DATEDIFF(CURDATE(), date_of_birth) / 365) BETWEEN 21 AND 30 THEN '21-30'
    WHEN FLOOR(DATEDIFF(CURDATE(), date_of_birth) / 365) BETWEEN 31 AND 40 THEN '31-40'
    WHEN FLOOR(DATEDIFF(CURDATE(), date_of_birth) / 365) BETWEEN 41 AND 50 THEN '41-50'
    WHEN FLOOR(DATEDIFF(CURDATE(), date_of_birth) / 365) BETWEEN 51 AND 60 THEN '51-60'
    ELSE '61+' 
  END AS age_group,
  COUNT(*) AS total_patients
FROM patients
GROUP BY age_group
ORDER BY age_group;

UPDATE patient_visits
SET bed_occupied = 1
WHERE bed_occupied = 0
ORDER BY RAND()
LIMIT 2300;

-- Make occupancy for some departments higher (~80-90%)
UPDATE patient_visits
SET bed_occupied = 1
WHERE department_id IN (
    SELECT dept_id FROM departments
    WHERE dept_id IN (50,9,60)
)
AND bed_occupied = 0
ORDER BY RAND()
LIMIT 1000;

-- Make occupancy for some departments lower (~40-50%)
UPDATE patient_visits
SET bed_occupied = 0
WHERE department_id IN (
    SELECT dept_id FROM departments
    WHERE dept_id IN (139,93,23)
)
AND bed_occupied = 1
ORDER BY RAND()
LIMIT 1000;
