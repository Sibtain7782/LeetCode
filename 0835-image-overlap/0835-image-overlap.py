class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        max_overlap = 0

        # Shift img1 by (dr, dc)
        for dr in range(-(n - 1), n):
            for dc in range(-(n - 1), n):
                overlap = 0

                for i in range(n):
                    for j in range(n):
                        # Original position in img1
                        x = i - dr
                        y = j - dc

                        # Check if shifted img1 position is valid
                        if 0 <= x < n and 0 <= y < n:
                            if img1[x][y] == 1 and img2[i][j] == 1:
                                overlap += 1

                max_overlap = max(max_overlap, overlap)

        return max_overlap