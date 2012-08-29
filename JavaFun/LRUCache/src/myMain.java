
public class myMain {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		LRUCache cache = LRUCache.getInstance();
		cache.addItem("1","Dog");
		cache.addItem("2","Cat");
		cache.addItem("3","Pig");
		cache.addItem("4","Bird");
		System.out.println(cache.getItem("1"));
		cache.addItem("1","Dog");
		System.out.println(cache.getItem("1"));
		cache.addItem("5","Mouse");
		System.out.println(cache.getItem("1"));
		cache.addItem("6","Tiger");
		System.out.println(cache.getItem("1"));
	}

}
