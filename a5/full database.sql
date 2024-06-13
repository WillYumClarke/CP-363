CREATE TABLE Student(
	StudentId CHAR(9) PRIMARY KEY,
	StudentForename CHAR(50) NOT NULL,
	StudentSurname CHAR(50) NOT NULL,
	AcademicProbation BOOL,
	GPA DECIMAL REFERENCES Enrollment(GPA) ON DELETE CASCADE,
	Address VARCHAR(255),
	Age INT NOT NULL,
	Program CHAR(20),
	PreviousEducation VARCHAR(255),
	Birthdate DATE,
	CHECK (Age >=17)
);

CREATE TABLE Prof(
	ProfId CHAR(9) PRIMARY KEY,
	ProfSurmane CHAR(50),
	ProfForemane CHAR(50),
	ProfEducation LONGTEXT,
	DepartmentCode CHAR(4) REFERENCES Department(DepartmentCode)
);

CREATE TABLE Room(
	RoomCode CHAR (5) PRIMARY KEY,
	BuildingCode CHAR(5),
	NumSeats int
);

CREATE TABLE Course(
	CourseCode CHAR(10) PRIMARY KEY,
	CourseName CHAR(20),
	ClassDates DATETIME,
	DepartmentCode CHAR(4) NOT NULL REFERENCES Department(DepartmentCode)
);

CREATE TABLE Section(
	SectionId INT PRIMARY KEY,
	CourseCode CHAR(10) NOT NULL REFERENCES Course(CourseCode),
	ProfId CHAR(9) REFERENCES Prof(ProfId)
);	

CREATE TABLE Enrollment(
	StudentId CHAR(9) REFERENCES Student(StudentId),
	SectionId INT REFERENCES Section(SectionId),
	GPA DECIMAL,
	PRIMARY KEY (StudentId, SectionId)
	);