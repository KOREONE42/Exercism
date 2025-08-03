class School:
    def __init__(self):
        """
        Initializes a new School instance.

        - _grades: Dictionary mapping grade numbers to sets of student names.
        - _student_lookup: Dictionary mapping student names to their assigned grade.
        - _added_results: List tracking whether each student was successfully added.
        """
        self._grades = {}
        self._student_lookup = {}
        self._added_results = []

    def add_student(self, name, grade):
        """
        Adds a student to the specified grade if they haven't already been added.

        Args:
            name (str): The student's name.
            grade (int): The grade number.

        Returns:
            None. The result (True/False) of the attempt is tracked in self._added_results.
        """
        # Check if the student has already been added (to any grade)
        if name in self._student_lookup:
            self._added_results.append(False)
            return

        # Add the student to the appropriate grade
        if grade not in self._grades:
            self._grades[grade] = set()
        self._grades[grade].add(name)

        # Record student in lookup to prevent future duplicates
        self._student_lookup[name] = grade

        # Record successful addition
        self._added_results.append(True)

    def roster(self):
        """
        Returns a sorted list of all students in the school, ordered by grade then name.

        Returns:
            list[str]: List of student names sorted by grade and name.
        """
        all_students = []

        # Sort grades numerically and students alphabetically within each grade
        for grade in sorted(self._grades):
            all_students.extend(sorted(self._grades[grade]))

        return all_students

    def grade(self, grade_number):
        """
        Returns a sorted list of students in the specified grade.

        Args:
            grade_number (int): The grade to query.

        Returns:
            list[str]: Sorted list of student names in that grade. Empty if grade not present.
        """
        if grade_number not in self._grades:
            return []
        return sorted(self._grades[grade_number])

    def added(self):
        """
        Returns the history of student addition attempts.

        Returns:
            list[bool]: List indicating success (True) or failure (False) of each add_student call.
        """
        return self._added_results
