class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # T: O(4 ** n), S: O(n)
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False  # Cannot form four equal sides
        
        side_length = total_length // 4
        matchsticks.sort(reverse=True)  # Sorting helps speed up backtracking
        
        sides = [0] * 4  # Four sides of the square
        
        def backtrack(index):
            if index == len(matchsticks):
                return all(side == side_length for side in sides)  # Check if all sides are equal
            
            for i in range(4):
                if sides[i] + matchsticks[index] <= side_length:
                    sides[i] += matchsticks[index]  # Try placing matchstick in side `i`
                    if backtrack(index + 1):
                        return True  # If solution found, return True
                    sides[i] -= matchsticks[index]  # Undo placement (backtrack)
                
                if sides[i] == 0:  # Optimization: avoid redundant placements
                    break
            
            return False
        
        return backtrack(0)