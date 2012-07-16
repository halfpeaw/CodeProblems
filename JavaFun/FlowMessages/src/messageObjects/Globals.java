package messageObjects;

/**
 * TODO Put here a description of what this class does.
 *
 * @author halfpeaw.
 *         Created Jul 13, 2012.
 */
public class Globals {
	public final static int CONNECT_TYPE = 0x0001;
	public final static int CONNECT_RESP = 0x0002;
	public final static int DISCONNECT = 0x0003;
	public final static int GET_PLAYERS_MSG = 0x0004;
	public final static int GET_PLAYERS_RESP = 0x0005;

	//Status Code
	public final static int COMMAND_MSG = 0x0000;
	public final static int USERNAME_IN_USE = 0x0001;
	public final static int UNKNOWN_FAILURE = 0x0002;
	//I'm so used to this being 3 from work I am just going with it.
	public final static int SUCCESS = 0x0003;
	
	
	public final static int IS_HUMAN = 0x00;
	public final static int IS_AI = 0xFF;
	/**
	 * 
	 * Sets the value of val in to byteIn
	 *
	 * @param offset
	 * @param count - #Bytes
	 * @param val
	 * @param byteIn
	 * @return True if successful, false if fail
	 */
	public static final boolean setValue(int offset, int count, int val, byte[] byteIn) {
		if (offset+count > byteIn.length) {
			return false;
		}
		byte a,b,c,d;
		a = (byte) (val >> 24);
		b = (byte) (val >> 16);
		c = (byte) (val >> 8);
		d = (byte) (val >> 0);
		switch (count) {
		case 4:
			byteIn[offset] = a;
			byteIn[offset+1] = b;
			byteIn[offset+2] = c;
			byteIn[offset+3] = d;
			break;
		case 3:
			byteIn[offset] = b;
			byteIn[offset+1] = c;
			byteIn[offset+2] = d;
			break;
		case 2:
			byteIn[offset] = c;
			byteIn[offset+1] = d;
			break;
		case 1:
			byteIn[offset] = d;
			break;
		default:
			break;
		}
		return true;
	}
	
	/**
	 * 
	 * returns an int based on an offset and the size of what we are returning
	 * From the ByteIn array
	 *
	 * @param offset
	 * @param count - #Bytes
	 * @param byteIn
	 * @return
	 */
	@SuppressWarnings("javadoc")
	public static final int getValue(int offset, int count, byte[] byteIn) {
		int number = 0;
		switch(count) {
			case 4:
				number = (byteIn[offset]&0xff) << 24 | (byteIn[offset+1]&0xff) << 16 
					| (byteIn[offset+2]&0xff) << 8 | (byteIn[offset+3]&0xff);
				break;
			case 3:
				number = (byteIn[offset]&0xff) << 16 
				| (byteIn[offset+1]&0xff) << 8 | (byteIn[offset+2]&0xff);
				break;
			case 2:
				number = (byteIn[offset]&0xff) << 8 | (byteIn[offset+1]&0xff);
				break;
			case 1:
				number = (byteIn[offset]&0xff);
				break;
			default:
				break;
		}
		return number;
	}
	
	/**
	 * 
	 * This method takes a string and will populate the messageArray with its contents
	 *
	 * @param offset - Where to start
	 * @param length - Max Size Input Should Be
	 * @param word - The input string
	 * @return True if success, false if string violates bounds
	 */
	public static final boolean fillArrayString(int offset, int length, String word, byte[] byteIn) {
		if (offset + length > byteIn.length) {
			System.out.println("Word: " + word);
			System.out.println("Size: " + offset + length + " versus "
					+ byteIn.length + " is too great");
			return false;
		}
		for (int i = 0; i < length && i < word.length(); i++ ) {
			byteIn[offset+i] = (byte)word.charAt(i);
		}
		return true;
	}
	
	/**
	 * 
	 * Read a string out of the byteIn array, based on a given length
	 *
	 * @param offset
	 * @param length
	 * @param byteIn
	 * @return empty if length + offset are greater than byteIn length
	 */
	public static final String readArrayString(int offset, int length, byte[] byteIn) {
		String result = "";
		if (offset+length > byteIn.length) {
			System.out.println("Read Array");
			System.out.println("Size: " + offset + length + " versus "
					+ byteIn.length + " is too great");
			return "";
		}
		for (int i = offset; i <offset+length; i++) {
			if (byteIn[i] != 0) {
				result += (char)byteIn[i];
			} else {
				return result;
			}
		}
		return result;
	}
	
	public final static int getMsgUserIDFromArray(byte[] byteIn) {
		return Globals.getValue(MessageStruct.TYPE_OFFSET, MessageStruct.TYPE_LEN, byteIn);
	}
}
