import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

ALL_KEYS = (1 << 26) - 1

def key_to_state(key):
    return 1 << (ord(key) - ord('a'))  # 'a' -> 1, 'b' -> 2, ..., 'z' -> 2^25

def main():
    with open(sys.argv[1]) as f:
        grid = f.read().strip().splitlines()

    H, W = len(grid), len(grid[0])
    sr, sc = next((r, c) for r in range(H) for c in range(W) if grid[r][c] == '@')
    grid = [list(row) for row in grid]
    grid[sr - 1][sc - 1] = grid[sr - 1][sc + 1] = grid[sr + 1][sc - 1] = grid[sr + 1][sc + 1] = '@'
    grid[sr - 1][sc] = grid[sr][sc - 1] = grid[sr][sc] = grid[sr][sc + 1] = grid[sr + 1][sc] = '#'

    starts = [(sr - 1, sc - 1), (sr - 1, sc + 1), (sr + 1, sc - 1), (sr + 1, sc + 1)]
    graph = defaultdict(list)  # graph[src] = [(dst, distance, req_mask), ...]

    keys = {}
    for r in range(H):
        for c in range(W):
            cell = grid[r][c]
            if 'a' <= cell <= 'z':
                keys[cell] = (r, c)

    def build_graph(start, sr, sc):
        q = deque([(sr, sc, 0, 0)])
        visited = {(sr, sc)}

        while q:
            r, c, d, m = q.popleft()
            cell = grid[r][c]

            if 'a' <= cell <= 'z' and (r, c) != (sr, sc):
                graph[start].append((cell, d, m))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    nm = m
                    if 'A' <= grid[nr][nc] <= 'Z':
                        nm |= key_to_state(grid[nr][nc].lower())
                    q.append((nr, nc, d + 1, nm))

    # Build edges from the 4 robot start positions
    for i, (sr, sc) in enumerate(starts):
        build_graph(str(i), sr, sc)

    # Build edges from every key location
    for k, (kr, kc) in keys.items():
        build_graph(k, kr, kc)

    # Dijkstra over the state space
    start_pos = ('0', '1', '2', '3')
    pq = [(0, start_pos, 0)]  # (distance, (pos1, pos2, pos3, pos4), keys)
    best = defaultdict(lambda: float('inf'))  # (positions, keys) -> distance
    best[(start_pos, 0)] = 0

    while pq:
        d, p, m = heappop(pq)

        if m == ALL_KEYS:
            print(d)
            return

        if best[(p, m)] < d:
            continue

        for i in range(4):
            for dst, dist, req in graph[p[i]]:
                bit = key_to_state(dst)
                if m & bit or req & ~m:
                    continue

                nm = m | bit
                np = p[:i] + (dst,) + p[i+1:]
                nd = d + dist

                if nd < best[(np, nm)]:
                    best[(np, nm)] = nd
                    heappush(pq, (nd, np, nm))

if __name__ == '__main__':
    main()
