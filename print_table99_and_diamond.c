#include<stdio.h>
int table99(void);
int diamond(int n, char c);
int main(void)
{
  printf("yo\n");
  diamond(5,'*');
  table99();
  return 0;
}

int diamond(int n, char c)
{
    if(n%2==0)
    {
        printf("N should be odd number only!\n");
        return -1;
    }
    int i,j,k,m;
    int bn=n/2;
    int bi,bj;
    for (i=1;i<=n;i+=2)
    {
        for(bi=bn;bi>0;bi--)
        {
            printf("  ");
        }
        for(j=1;j<=i;j++)
        {
            printf("%c ",c);
        }
        printf("\n");
        bn-=1;
    }
    bn=1;
    for (k=n-2;k>=1;k-=2)
    {
        for(bj=bn;bj>0;bj--)
        {
            printf("  ");
        }
        for(m=k;m>=1;m--)
        {
            printf("%c ",c);
        }
        printf("\n");
        bn+=1;
    }
    return 0;
}

int table99(void)
{
    int i,j;
    for(i=1;i<=9;i++)
    {
        for(j=1;j<=i;j++)
        {
            printf("%d " ,i*j);
        }
        printf("\n");
    }
    return 0;
}
/*
Notes on the print table99:
To print out such table, it is neccessary to use a two layer loop,
Outer layer-- i counting from 1 to 9 while the inner layer print the multiplication
from 1 up until i
*/
/*
N needs to be odd number
The main take away for the print diamond problem is that:
focusing on the whitespace in front of the characters everyline.
You should start first with a vertical montain like this:
+
+++
+++++
Then consider how to make it look like:
+
+++
+++++
+++
+
hint: use two loops(one below the other)
After this, realize that the space in front every solid diamond lines are ((n-1)/2)--
so we can easily draw the upper part of the diamond
  +
 +++
+++++
The rest is easy to follow.
It is worth noticing that (a big aha for me) for diamonds with spaces between the characters, just
see those spaces can be bundled with the character as a basic unit. So goes for the white spaces before
every line.
*/