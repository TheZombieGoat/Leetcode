//Given an integer array nums, find the subarray with the largest sum, and return its sum.



int maxSubArray(int arr[], int narr)
{
    if(narr > 1){
        int i;
        int j = 0;
        int *p = (int*)malloc(sizeof(int)*narr);
        int sum = 0;
        bool pos = false;
        for(i = 0; i < narr; i++){
            if(arr[i] > 0){
                sum = arr[i];
                p[j] = sum;
                j++;
                pos = true;
            }
            while(sum > 0 && i < narr-1){
                i++;
                sum += arr[i];
                p[j] = sum;
                j++;
            }
            sum = 0;
        }
        if(!pos){
            int g = arr[0];
            for (int f = 1; f < narr; f++){
                 if(arr[f] > g)
                    g = arr[f];
            }
                return g;
        }    
        int k = 0;
        int x = p[k];
        for (k = 1; k < j; k++)
        {
            if(p[k] > x)
            x = p[k];
        }
        free(p);
        return x;
    }else
        return arr[0];
}

