class Solution:
    def minJumps(self, arr: List[int]) -> int:
        hashmap = defaultdict(list)
        for i, num in enumerate(arr):
            hashmap[num].append(i)
        visited = set([0])
        queue = deque([(0, 0)])
        while queue:
            curr, step = queue.popleft()
            if curr == len(arr) - 1:
                return step
            if curr + 1 not in visited:
                queue.append((curr + 1, step + 1))
                visited.add((curr + 1))
            if curr > 0 and curr - 1 not in visited:
                queue.append((curr - 1, step + 1))
                visited.add((curr - 1))
            for index in hashmap[arr[curr]]:
                if index not in visited:
                    queue.append((index, step + 1))
                    visited.add((index))
            del hashmap[arr[curr]]