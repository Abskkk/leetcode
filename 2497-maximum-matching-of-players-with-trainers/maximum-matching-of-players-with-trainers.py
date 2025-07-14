class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i, j = 0, 0
        count = 0
        while i < len(players) and j < len(trainers):
            player = players[i]
            trainer = trainers[j]
            if player <= trainer:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count