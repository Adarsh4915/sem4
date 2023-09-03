#include<stdio.h>
#include<stdlib.h>
#include<time.h>
double count=0;
void insertionsort(int *num , int n)
{
int i,t,j,flag=0;
for(i=0;i<n;i++)
{
t=*(num+i);
for(j=i-1; j>=0; j--)
{
if(*(num+j)>t)
{
count++;
*(num+j+1)=*(num+j);
flag=1;
}
else
break;
}
if(flag)
{
*(num+j+1)=t;
}
}
}
int main()
{
int n,*a,i,t;
clock_t start ,end;
double time;
printf("enter the size of array\t");
scanf("%d",&n);
a=(int*)malloc(n*sizeof(int));
printf("enter elements\n");
for(i=0;i<n;i++)
{
*(a+i)=rand()%100+1;
}
start=clock();
insertionsort(a,n);
end=clock();
printf("sorted array is\n");
for(i=0;i<n;i++)
{
printf("%d\t",*(a+i));
}
time+=(double)(end-start)/CLOCKS_PER_SEC;
printf("time taken is %lf",time);
printf("no of comparisons made is %lf\t",count);
return 0;
}
