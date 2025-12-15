DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    department_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_student_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    department_id INT NOT NULL,
    CONSTRAINT fk_course_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    grade NUMERIC CHECK (grade >= 0 AND grade <= 100),
    CONSTRAINT fk_enrollment_student
        FOREIGN KEY (student_id)
        REFERENCES students(student_id),
    CONSTRAINT fk_enrollment_course
        FOREIGN KEY (course_id)
        REFERENCES courses(course_id),
    CONSTRAINT unique_enrollment UNIQUE (student_id, course_id)
);
