//Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

#include <stdlib.h>
#include <stdio.h>

int compar(const void *a, const void *b)
{
    return ( *(int*)a - *(int*)b );
}

int* intersect(int* arr, int narr, int* arr2, int narr2, int* n){
    int s = 0;
    int diff = narr - narr2;
    int size = narr;
    if(diff < 0)
        size = narr2;
    int *p = (int*)calloc(size,sizeof(int));
    qsort(arr,narr,sizeof(int),compar);
    qsort(arr2,narr2,sizeof(int),compar);
    int i, j;
    if(narr >= narr2){
        int l = 0;
        int lim = narr;
        for(i = 0; i < narr2; i++){
            for(j = l; j < lim; j++){
                if(arr[j] == arr2[i]){
                    p[s] = arr[j];
                    s++;
                    j++;
                    l = j;
                    break;
                }
                if(arr[j] > arr2[narr2-1]){
                    lim = j;
                }
                    
            }
        }    
    }else if(narr < narr2){
            int l = 0;
            for(i = 0; i < narr; i++){
            for(j = l; j < narr2; j++){
                if(arr[i] == arr2[j]){
                    p[s] = arr[i];
                    s++;
                    j++;
                    l = j;
                    break;
                }
            }
        }    
    }
    *n = s;
    return p;
}