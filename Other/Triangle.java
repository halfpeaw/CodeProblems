
public class Triangle {

	public static void main(String[] args) {
		System.out.println("Triangle testing");
		//Good Test Cases
		System.out.println(isTriange(2,3,4));
		System.out.println(isTriange(1,2,2));
		System.out.println(isTriange(2,2,2));
		System.out.println(isTriange(2,2,2));
		System.out.println(isTriange(12,14,18));
		System.out.println(isTriange(1000,600,1400));
		//Max Value
		System.out.println(isTriange(Integer.MAX_VALUE,Integer.MAX_VALUE,Integer.MAX_VALUE));
		System.out.println(isTriange(Integer.MAX_VALUE-10,Integer.MAX_VALUE-10,Integer.MAX_VALUE));
		System.out.println(isTriange(Integer.MAX_VALUE-1,Integer.MAX_VALUE-2,Integer.MAX_VALUE));
		
		
		//Bad Test Cases
		System.out.println(isTriange(1,2,3));
		System.out.println(isTriange(2,2,5));
		System.out.println(isTriange(0,2,1));
		System.out.println(isTriange(0,0,1));
		System.out.println(isTriange(0,0,0));
		//Check negative case
		System.out.println(isTriange(-1,2,2));
		System.out.println(isTriange(-1,-1,2));
		System.out.println(isTriange(-1,-1,-1));
		System.out.println(isTriange(Integer.MIN_VALUE,Integer.MIN_VALUE,Integer.MIN_VALUE));
		
		System.out.println("Queue testing");
		CircularQueue queue = new CircularQueue();
		queue.printQueue();
		queue.initialize(3);
		queue.dequeue();
		queue.enqueue(5);
		queue.enqueue(15);
		queue.enqueue(25);
		queue.printQueue();
		queue.dequeue();
		queue.printQueue();
		queue.enqueue(35);
		queue.enqueue(45);
		queue.printQueue();
		queue.dequeue();
		queue.dequeue();
		queue.dequeue();
		queue.enqueue(-1);
		queue.printQueue();
		queue.initialize(3);
		queue.printQueue();
		
		
	}
	
	public final static int SCALENE = 1;
	public final static int ISOSCELES = 2;
	public final static int EQUILATERAL = 3;
	public final static int ERROR = 4;
	/**
	 * Function that determines the kind of triangle based on sides a,b,c
	 * @param a side length of a triangle
	 * @param b side length of a triangle
	 * @param c side length of a triangle
	 * @return return SCALENE, ISOSCELES, EQUILATERAL or ERROR if no conditions match
	 */
	public static int isTriange(int a, int b, int c) {
		if (a <= 0 || b <= 0 || c<=0) {
			return ERROR;
		}
		//Verify all sides are equal
		//Do this check before bounds check to save on useless variable declaration
		if (a == b && b == c) {
			return EQUILATERAL;
		}
		//Need this chunk of code for constraint checking
		int hyp = 0;
		int side1 = 0;
		int side2 = 0;
		//Side 1 and Side 2 are irrelevant as long as they are less than hyp
		if (c > a && c > b) {
			hyp = c;
			side1 = a;
			side2 = b;
		} else if (a > b && a > c) {
			hyp = a;
			side1 = c;
			side2 = b;
		} else {
			hyp = b;
			side1 = c;
			side2 = a;
		}
		//We need to cast to long on the possibility the sum of 
		//side1 and side2 are greater than the max integer value
		if (((long)side1 + (long)side2) <= (long)hyp) {
			return ERROR;
		}
		
		//Already checked for all EQUILATERAL so no worries
		if (a == b || b == c || a == c) {
			return ISOSCELES;
		}
		
		//If all sides aren't equal and 2 sides aren't equal then no side must be equal
		return SCALENE;
	}

}
