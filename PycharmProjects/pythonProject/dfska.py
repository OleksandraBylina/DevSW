def goyda(n):
    def dfs(start, path):
        if len(path) > 1:
            result.append(path[:])
        for i in range(len(n)):
            if not path or n[i] >= 