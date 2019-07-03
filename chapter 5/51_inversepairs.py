# -*- coding:utf-8 -*-
# 数组中的逆序对

# 本题采用的是归并排序的衍生算法


class Solution:
    def InversePairs(self, data):
        # write code here
        def mergeSort(temp,l,r,data):
            if l>=r:
                temp[l]=data[l]
                return 0
            mid=(l+r)/2
            left=mergeSort(data,l,mid,temp)
            right=mergeSort(data,mid+1,r,temp)
              
            count=0
            i,j=l,mid+1
            ind=l
            while i<=mid and j<=r:
                if data[i]>data[j]:
                    temp[ind]=data[j]
                    j+=1
                    count+=mid+1-i
                else:
                    temp[ind]=data[i]
                    i+=1
                ind+=1
            while i<=mid:
                temp[ind]=data[i]
                i+=1
                ind+=1
            while j<=r:
                temp[ind]=data[j]
                j+=1
                ind+=1
            return count+left+right
        return mergeSort(data[:],0,len(data)-1,data)%1000000007