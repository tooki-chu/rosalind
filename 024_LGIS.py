'''
ROSALIND - Bioinformatics Stronghold
Problem: Longest Increasing Subsequence
'''

def inc_sub(perm):
    # array to store the index of last integer in subsequences of diff lengths
    # only stores the minimum value for each specific length
    temp = [0] * n

    # array to store the preceding integer for each element in permutation
    prev = [-1] * n

    # variable to store the current longest subsequence length
    l = 0

    for i in range(1, n):
        # if the integer is larger than the last integer in the current longest substring
        if perm[i] > perm[temp[l]]:
            # store the index for this integer in the next index i.e. temp[l+1]
            temp[l+1] = i
            # store the index of the preceding integer in prev
            prev[i] = temp[l]
            # update the current longest subsequence length
            l += 1

        # else    
        # if the integer is smaller than the integer whose index is stored at temp[0]
        elif perm[i] < perm[temp[0]]:
            # update index to store the smallest integer so far
            temp[0] = i

        # else
        # do a binary search to find ceiling of perm[i]
        # possible since values in temp are sorted in increasing order
        else:
            # initialise variables for binary search through temp array
            lower = 0
            upper = l

            while upper - lower > 1:
                mid = (upper + lower) // 2

                # if the value at [i] is much larger and needs another iteration of binary search    
                if perm[i] > perm[temp[mid]]:
                    lower = mid

                # if value at [i] is much smaller and needs another iteration of binary search    
                elif perm[i] < perm[temp[mid]]:    
                    upper = mid

                else:
                    break

            # replace the index stored at index of upper      
            temp[upper] = i
            # store the index for preceding integer in prev array
            prev[i] = temp[upper-1]


    idx = temp[l] # last integer in longest increasing subsequence

    results = [] # empty array to store integers in subsequence

    # print out the longest increasing subsequence
    for k in range(l+1):
        results.append(perm[idx])
        idx = prev[idx]
        
    return(results[::-1])


def dec_sub(perm):
    # array to store the index of last integer in subsequences of diff lengths
    # only stores the minimum value for each specific length
    temp = [0] * n

    # array to store the preceding integer for each element in permutation
    prev = [-1] * n

    # variable to store the current longest subsequence length
    l = 0

    for i in range(1, n):
        # if the integer is smaller than the last integer in the current longest substring
        if perm[i] < perm[temp[l]]:
            # store the index for this integer in the next index i.e. temp[l+1]
            temp[l+1] = i
            # store the index of the preceding integer in prev
            prev[i] = temp[l]
            # update the current longest subsequence length
            l += 1

        # else    
        # if the integer is smaller than the integer whose index is stored at temp[0]
        elif perm[i] > perm[temp[0]]:
            # update index to store the smallest integer so far
            temp[0] = i

        # else
        # do a binary search to find ceiling of perm[i]
        # possible since values in temp are sorted in increasing order
        else:
            # initialise variables for binary search through temp array
            lower = 0
            upper = l

            while upper - lower > 1:
                mid = (upper + lower) // 2

                # if the value at [i] is much smaller and needs another iteration of binary search    
                if perm[i] < perm[temp[mid]]:
                    lower = mid

                # if value at [i] is much larger and needs another iteration of binary search    
                elif perm[i] > perm[temp[mid]]:    
                    upper = mid

                else:
                    break

            # replace the index stored at index of upper      
            temp[upper] = i
            # store the index for preceding integer in prev array
            prev[i] = temp[upper-1]


    idx = temp[l] # last integer in longest increasing subsequence

    results = [] # empty array to store integers in subsequence

    # print out the longest increasing subsequence
    for k in range(l+1):
        results.append(perm[idx])
        idx = prev[idx]
        
    return(results[::-1])


def main():
    with open("datasets/rosalind_lgis.txt", "r") as f:
        n = int(f.readline())
        
        p = f.read().split()
        perm = [int(i) for i in p]
        
        LIS = inc_sub(perm)
        LDS = dec_sub(perm)
        
        print(*LIS)
        print(*LDS)


if __name__ == '__main__':
    main()