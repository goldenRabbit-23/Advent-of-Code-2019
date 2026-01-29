import sys
from collections import defaultdict, deque

ALL_KEYS = (1 << 26) - 1

def key_to_state(key):
    return 1 << (ord(key) - ord('a'))  # 'a' -> 1, 'b' -> 2, ..., 'z' -> 2^25

def main():
    with open(sys.argv[1]) as f:
        grid = f.read().strip().splitlines()

    H, W = len(grid), len(grid[0])
    sr, sc = next((r, c) for r in range(H) for c in range(W) if grid[r][c] == '@')
    dist = defaultdict(lambda: float('inf'))  # (row, col, keys) -> distance
    dist[(sr, sc, 0)] = 0
    q = deque([(sr, sc, 0)])

    while q:
        r, c, keys = q.popleft()
        d = dist[(r, c, keys)]

        if keys == ALL_KEYS:
            print(d)
            return

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < H and 0 <= nc < W):
                continue

            cell = grid[nr][nc]
            if cell == '#':
                continue

            new_keys = keys
            if 'a' <= cell <= 'z':
                new_keys |= key_to_state(cell)
            elif 'A' <= cell <= 'Z':
                if not (keys & key_to_state(cell.lower())):
                    continue

            if dist[(nr, nc, new_keys)] > d + 1:
                dist[(nr, nc, new_keys)] = d + 1
                q.append((nr, nc, new_keys))

if __name__ == '__main__':
    main()
