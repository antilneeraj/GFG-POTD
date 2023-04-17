class JobComparator:
    def compare(self, j1, j2):
        return j2.profit - j1.profit

class Solution:
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, arr, n):
        # Your code here
        arr.sort(key=lambda x: x.profit, reverse=True)

        res = 0
        tot_job = 0
        slot = [False] * n  # track of free time slots - all false now

        # itr for all jobs.
        for i in range(n):
            # linear search [deadline to 0] - explained in dry run
            for j in range(arr[i].deadline - 1, -1, -1):
                # if free slot found - add the profits, tot_job++, mark slot filled
                if not slot[j]:
                    res += arr[i].profit
                    tot_job += 1
                    slot[j] = True
                    break

        ans = [tot_job, res]
        return ans
