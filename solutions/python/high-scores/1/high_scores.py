class HighScores:
    """
    A class to manage a list of game scores, providing methods to retrieve
    the latest score, the highest score, and the top three highest scores.
    
    Attributes:
        scores (list): A list of integers representing the game scores.
    """
    
    def __init__(self, scores):
        """
        Initializes the HighScores instance with a list of scores.
        
        Args:
            scores (list): A list of integer scores.
        """
        self.scores = scores  # Store the provided list of scores

    def latest(self):
        """
        Returns the most recent score from the list.
        
        Returns:
            int: The last score in the scores list.
        """
        # Access the last element of the list
        return self.scores[-1]

    def personal_best(self):
        """
        Returns the highest score from the list.
        
        Uses Python's built-in max() function to find the maximum value.
        
        Returns:
            int: The highest score from the scores list.
        """
        # Return the maximum score using max() function
        return max(self.scores)

    def personal_top_three(self):
        """
        Returns the three highest scores in descending order.
        
        Sorts the list in descending order and slices the first three elements.
        
        Returns:
            list: A list containing the top three highest scores, sorted from highest to lowest.
        """
        # Sort the scores in descending order and return the top three
        return sorted(self.scores, reverse=True)[:3]
        