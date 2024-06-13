CREATE TABLE Enrollment(
	EnrollmentId INT NOT NULL,
	StudentId INT,
	PRIMARY KEY (EnrollmentId),
	FOReign KEY(StudentId) REFERENCES Students(StudentId)
	);