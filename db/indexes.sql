-- Index for student lookups
CREATE INDEX IF NOT EXISTS idx_students_department
ON students(department_id);

-- Index for enrollments joins
CREATE INDEX IF NOT EXISTS idx_enrollments_student
ON enrollments(student_id);

CREATE INDEX IF NOT EXISTS idx_enrollments_course
ON enrollments(course_id);

-- Index for course department filtering
CREATE INDEX IF NOT EXISTS idx_courses_department
ON courses(department_id);