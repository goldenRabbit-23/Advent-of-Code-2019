import sys
from collections import defaultdict, deque

def main():
    with open(sys.argv[1]) as f:
        grid = f.read().splitlines()

    H, W = len(grid), len(grid[0])
    portals = defaultdict(list)

    def is_alpha(r, c):
        return 0 <= r < H and 0 <= c < W and 'A' <= grid[r][c] <= 'Z'

    def is_outer(r, c):
        return r == 2 or r == H - 3 or c == 2 or c == W - 3

    # Scan grid for portal labels
    for r in range(H):
        for c in range(W):
            if grid[r][c] == '.':
                # Check neighbors for letters
                portal_name = None

                # Check Up
                if is_alpha(r-1, c):
                    portal_name = grid[r-2][c] + grid[r-1][c]
                # Check Down
                elif is_alpha(r+1, c):
                    portal_name = grid[r+1][c] + grid[r+2][c]
                # Check Left
                elif is_alpha(r, c-1):
                    portal_name = grid[r][c-2] + grid[r][c-1]
                # Check Right
                elif is_alpha(r, c+1):
                    portal_name = grid[r][c+1] + grid[r][c+2]

                if portal_name:
                    portals[portal_name].append((r, c))

    sr, sc = portals['AA'][0]
    er, ec = portals['ZZ'][0]

    # Map portal connections: (r, c) -> (target_r, target_c)
    warp = {}
    for name, locs in portals.items():
        if name in ('AA', 'ZZ'):
            continue
        warp[locs[0]] = locs[1]
        warp[locs[1]] = locs[0]

    # BFS
    q = deque([(sr, sc, 0, 0)])  # position (r, c), distance d, level l
    visited = {(sr, sc, 0)}  # (r, c, level)

    while q:
        r, c, d, l = q.popleft()

        if (r, c) == (er, ec) and l == 0:
            print(d)
            return

        # Standard moves
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == '.' and (nr, nc, l) not in visited:
                visited.add((nr, nc, l))
                q.append((nr, nc, d + 1, l))

        # Portal move
        if (r, c) in warp:
            wr, wc = warp[(r, c)]

            nl = l
            if is_outer(r, c):  # Outer portal goes UP a level (l - 1)
                nl = l - 1
            else:               # Inner portal goes DOWN a level (l + 1)
                nl = l + 1

            if nl >= 0:  # Any other outer portals at outermost layer are walls
                if (wr, wc, nl) not in visited:
                    visited.add((wr, wc, nl))
                    q.append((wr, wc, d + 1, nl))

if __name__ == '__main__':
    main()
