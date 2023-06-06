//Given an integer array nums, find the subarray with the largest sum, and return its sum.



int maxSubArray(int arr[], int narr)
{
    int currSum = 0;
    int maxSum = arr[0];
    for(int i = 0; i < narr; i++){
        currSum += arr[i];
        if(currSum > maxSum)
            maxSum = currSum;
        if(currSum < 0)
            currSum = 0;
    }
    return maxSum;
}

