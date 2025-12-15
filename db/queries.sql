-- 1. Total students
SELECT COUNT(*) AS total_students
FROM students;

-- 2. Students per department
SELECT
    d.name AS department,
    COUNT(s.student_id) AS student_count
FROM departments d
LEFT JOIN students s ON s.department_id = d.department_id
GROUP BY d.name
ORDER BY student_count DESC;

-- 3. Average grade per course
SELECT
    c.name AS course,
    ROUND(AVG(e.grade), 2) AS avg_grade
FROM courses c
JOIN enrollments e ON e.course_id = c.course_id
GROUP BY c.name
ORDER BY avg_grade DESC;

-- 4. Student enrollment report (JOIN-heavy)
SELECT
    s.name AS student_name,
    s.email,
    c.name AS course_name,
    e.grade
FROM students s
JOIN enrollments e ON e.student_id = s.student_id
JOIN courses c ON c.course_id = e.course_id
ORDER BY s.name;

-- 5. Detect students enrolled in multiple courses
SELECT
    student_id,
    COUNT(course_id) AS course_count
FROM enrollments
GROUP BY student_id
HAVING COUNT(course_id) > 1;

-- 6. Detect invalid grades (should be empty due to constraints)
SELECT *
FROM enrollments
WHERE grade < 0 OR grade > 100;

-- 7. Courses with no enrollments
SELECT
    c.course_id,
    c.name
FROM courses c
LEFT JOIN enrollments e ON e.course_id = c.course_id
WHERE e.enrollment_id IS NULL;
