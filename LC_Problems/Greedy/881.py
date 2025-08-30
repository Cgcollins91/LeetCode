class Solution:
       def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()                 # ascending
        i, j = 0, len(people) - 1     # lightest, heaviest
        boats = 0

        while i <= j:
            # Put the heaviest person on a boat; try to pair with lightest if possible
            # If heaviest can't pair with lightest, they won't be able to pair with anyone, 
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            boats += 1

        return boats