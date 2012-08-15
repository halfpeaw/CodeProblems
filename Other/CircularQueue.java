
public class CircularQueue {
	private int[] queue = null;
	private int header = 0;
	private int tail = 0;
	private int quantity = 0;
	public CircularQueue()  {
		
	}
	/**
	 * 
	 * @param size is the size of our array must be greater than 0
	 * @return true if success else false
	 */
	public synchronized boolean initialize(int size) {
		if (size <=0) {
			System.out.println("Size of queue must be greater than 0");
			return false;
		}
		this.queue = new int[size];
		this.header = 0;
		this.tail = 0;
		this.quantity = 0;
		return true;
	}
	/**
	 * 
	 * @param val is the value we are storing in our queue
	 * @return false if fail to enqueue other return true
	 */
	public synchronized boolean enqueue(int val) {
		if (queue == null || queue.length <= 0) {
			System.out.println("Queue not properly instatiated");
			return false;
		}
		if (this.quantity >= queue.length) {
			System.out.println("too many elements");
			return false;
		}
		if (this.tail >= queue.length) {
			this.tail = 0;
		}
		this.queue[this.tail] = val;
		this.tail +=1;
		this.quantity++;
		
		return true;
	}
	/**
	 * 
	 * @return -1 if error or the resulting dequeued item
	 * There does pose the problem if the user wants to enqueue the value -1 so
	 * we could maybe throw an exception instead up to the design
	 */
	public synchronized int dequeue() {
		if (queue == null || queue.length <= 0) {
			System.out.println("Queue not properly instatiated");
			return -1;
		}
		if (this.quantity <= 0) {
			System.out.println("too few elements");
			return -1;
		}
		if (this.header >= queue.length) {
			this.header = 0;
		}
		int result = this.queue[this.header];
		this.queue[this.header] = 0;
		this.header +=1;
		this.quantity--;
		return result;
	}
	/**
	 * function used for debugging note it will display 0 if the spot of an array isn't filled
	 */
	public synchronized void printQueue() {
		String result = "";
		if (queue != null && queue.length > 0) {
			for (int i = 0; i < queue.length; i++) {
				result += queue[i] + " ";
			}
			System.out.println(result);
		} else {
			System.out.println("Queue is null or empty");
		}
	}
}
