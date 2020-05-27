#include<cstdio>
#include<string>
using namespace std;

bool compare(char a, char b){
    printf("? %c %c\n",a,b);
    fflush(stdout);
    char ans;
    scanf(" %c",&ans);
    if(ans=='<'){
        return true;
    }
    else{
        return false;
    }
}

void merge(string arr,int l, int m , int r){
    int i,j,k;
    int n1=m-l+1;
    int n2=r-m;
    //temp arrays
    int L[n1],R[n2];
    for(i=0;i<n1;i++)
        L[i]=arr[l+i];
    for(j=0;j<n2;j++)
        R[j]=arr[l+m+j];
    i=0;j=0;k=l;
    while(i<n1,j<n2){
        //change later
        if (compare(L[i],R[j])){
            arr[k]=L[i];
            i++;
            }else{
            arr[k]=R[j];
            j++;}
        k++;}
    while(i<n1){
        arr[k]=L[i];
        i++;
        k++;
    }
    while(j<n2){
        arr[k]=L[j];
        i++;
        k++;
    }
    
}

void merge_sort(string arr,int l, int r){
    if(l<r){
        int m = l+(r-l)/2;
        merge_sort(arr,l,m);
        merge_sort(arr,m+1,r);
        
        merge(arr,l,m,r);
    }
}


int main(void){
    int N,Q,i,j;
    scanf("%d%d",&N,&Q);
    string s;
    int k;
    for (k=0;k<N;k++){
        s[k]=(char)('A'+k);
    }
    merge_sort(s,0,--N);
    printf("! %s\n",s.c_str());
    fflush(stdout);
    return 0;
}

/*
int insert_sort(string *a){
    int length= int(sizeof(a)/sizeof(a[0]));
    if length ==
    return 0;
}
*/


