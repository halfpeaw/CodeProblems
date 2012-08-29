import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.Map;


public class LRUCache {
	private final static int MAX_ENTRIES = 100;
	private final Map<String,String> cache = Collections.synchronizedMap(new LinkedHashMap<String,String>(MAX_ENTRIES+1, .75F, true)  
	{
		private static final long serialVersionUID = -7243775637652233852L;
		// This method is called just after a new entry has been added
	    public boolean removeEldestEntry(Map.Entry<String, String> eldest) {
	        return size() > MAX_ENTRIES;
	    }
	});
	private final static LRUCache instance = new LRUCache();

	//We'll treat this is a singleton since there really should only be one cache
	//Plus I want to play with singletons
	private LRUCache () {	
	}
	
	static public LRUCache getInstance() {
		return instance;
	}
	public void addItem(String key, String value) {
		cache.put(key, value);
	}
	public String getItem(String key) {
		return cache.get(key);
	}
	
}
