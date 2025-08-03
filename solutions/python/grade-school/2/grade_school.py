class School:
    def __init__(self):
        """
        Initialize a new School instance.

        Attributes:
            _grades (dict[int, set[str]]): Maps each grade number to a set of student names.
            _student_lookup (dict[str, int]): Maps student names to the grade they were added to.
            _added_results (list[bool]): Tracks success (True) or failure (False) for each add_student call.
        """
        self._grades = {}
        self._student_lookup = {}
        self._added_results = []

    def add_student(self, name, grade):
        """
        Attempt to add a student to a specific grade.

        A student can only be added once across all grades. Duplicate additions are ignored.

        Args:
            name (str): The student's name (must be unique in the school).
            grade (int): The grade the student should be added to.

        Side Effects:
            Updates the roster and student lookup if addition is successful.
            Appends True or False to _added_results indicating success or failure.
        """
        if name in self._student_lookup:
            # Student has already been added
            self._added_results.append(False)
            return

        # Initialize the grade bucket if it doesn't exist
        if grade not in self._grades:
            self._grades[grade] = set()

        # Add student to the grade and record success
        self._grades[grade].add(name)
        self._student_lookup[name] = grade
        self._added_results.append(True)

    def roster(self):
        """
        Get the full roster of students, sorted by grade then by name.

        Returns:
            list[str]: A list of all students in the school, sorted first by grade (ascending)
                       and then alphabetically by name within each grade.
        """
        full_roster = []

        # Iterate through each grade in sorted order
        for grade in sorted(self._grades.keys()):
            # Sort the names alphabetically within the grade
            full_roster.extend(sorted(self._grades[grade]))

        return full_roster

    def grade(self, grade_number):
        """
        Retrieve the list of students in a specific grade.

        Args:
            grade_number (int): The grade to look up.

        Returns:
            list[str]: A sorted list of student names in the given grade.
                       Returns an empty list if the grade has no students.
        """
        if grade_number not in self._grades:
            return []

        return sorted(self._grades[grade_number])

    def added(self):
        """
        Retrieve the log of all student addition attempts.

        Returns:
            list[bool]: List of booleans where each element indicates whether a corresponding
                        add_student call was successful (True) or rejected (False).
        """
        return self._added_results
