class Garden:
    DEFAULT_STUDENTS = [
        "Alice", "Bob", "Charlie", "David", "Eve", "Fred", 
        "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"
    ]

    # Mapping from diagram letter to plant name.
    PLANT_MAP = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets"
    }

    def __init__(self, diagram, students=None):
        # Split the diagram into separate rows.
        self.rows = diagram.splitlines()
        # Use the provided list of students; otherwise, use the default roster.
        if students is None:
            students = Garden.DEFAULT_STUDENTS
        # The teacher assigns cups alphabetically.
        self.students = sorted(students)

    def plants(self, student):
        # Find the student's index based on alphabetical order.
        index = self.students.index(student)
        # Calculate the two positions for the student's cups in each row.
        cup_positions = [2 * index, 2 * index + 1]
        # Gather the plant letters from each row.
        plant_letters = []
        for row in self.rows:
            for pos in cup_positions:
                plant_letters.append(row[pos])
        # Convert letters to full plant names.
        return [Garden.PLANT_MAP[letter] for letter in plant_letters]
