-- View 1: Student enrollment details
CREATE OR REPLACE VIEW student_enrollment_view AS
SELECT
    s.student_id,
    s.name AS student_name,
    s.email,
    d.name AS department,
    c.name AS course,
    e.grade
FROM students s
LEFT JOIN departments d ON d.department_id = s.department_id
JOIN enrollments e ON e.student_id = s.student_id
JOIN courses c ON c.course_id = e.course_id;

-- View 2: Course performance summary
CREATE OR REPLACE VIEW course_performance_view AS
SELECT
    c.course_id,
    c.name AS course_name,
    COUNT(e.enrollment_id) AS total_enrollments,
    ROUND(AVG(e.grade), 2) AS average_grade
FROM courses c
LEFT JOIN enrollments e ON e.course_id = c.course_id
GROUP BY c.course_id, c.name;
