   
if __name__=="__main__":
    numberOfElements = int(input("Enter the number of elements to be sorted: "))
    input =[]
    for i in range(numberOfElements):
        element = int(input("Enter the element:"))
        input.append(element)
    print("The input array is :", end =" ")
    [print(i, end= " ") for i in input]

	
		HeapSort hs=new HeapSort();
		hs.printArray(a);
		hs.heapSort(a);
		System.out.print("Sorted array is		");
		hs.printArray(a);
	}

	# public void printArray(int a[])
	# {
	# 	int s=a.length;
	# 	for(int i=0;i<s;i++) System.out.print(a[i]+" ");
	# 	System.out.println();
	# }
class HeapSort:

	def heapSort(D):
	{
		max_heapify(D);
		for(int i=a.length-1;i>0;i--)
		{
			int temp=a[i];
			a[i]=a[0];
			a[0]=temp;
			percolateDown(a,0,i);
		}
	}

	def max_heapify(D):
	    input_length =len(D)
        for i in range(int((input_length -2)/2), -1,-1):
		    percolateDown(D,i,input_length);
		
	

	# public int getLeftChild(int i,int m)
	# {
	# 	int n=2*i+1;
	# 	return n<m?n:-1;
	# }

	# public int getRightChild(int i,int m)
	# {
	# 	int n=2*i+2;
	# 	return n<m?n:-1;
	# }

	def percolateDown(D, i, m):
	

		l = 2* i +1
		r= 2*i +2
		data = D[i]
		largest = 0
		if(l!=-1 and D[l]>data):
		
			largest=l;	
		
		else:
		
			largest=i;
		
		if(r!=-1 and D[r] > D[largest]):
		    largest=r
		
		if(largest!=i):
            
            D[largest] = data
		    D[i]=D[largest]
            D[largest] = data
            D[largest]=data			
            percolateDown(D,largest,m)
		
	

