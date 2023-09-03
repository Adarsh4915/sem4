#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define size 1000000
int binarysearch(int a[], int low , int high , int key)
{
if(high>=low)
{
int mid=(low+high)/2;
if(a[mid]==key)
return mid;
else if(a[mid]>key)
return binarysearch(a,low,mid-1,key);
else
return binarysearch(a,mid+1,high,key);
}
return -1;
}
int main()
{
int a[size],key,i,n,result;
printf("enter the n value: \n");
scanf("%d",&n);
printf("considering the elements in the sorted order\n");
for(i=0;i<n;i++)
{
a[i]=i+4;
}
for(i=0;i<n;i++)
{
printf("%d\t",a[i]);
}
printf("\nenter the key element:");
scanf("%d",&key);
double timespent;
clock_t begin=clock();
result=binarysearch(a,0,n-1,key);
(result==-1)?printf("the element is not present in the array\n"):printf("the element is present at index %d",result);
clock_t end=clock();
timespent=(double)(end-begin)/CLOCKS_PER_SEC;
printf("\n the time taken is %f sec \n",timespent);
return 0;
}