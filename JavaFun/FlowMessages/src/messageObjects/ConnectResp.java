package messageObjects;

/**
 * This is a Connection Response.  Identical to the ConnectionCommand except that is has a UserID
 *
 * @author halfpeaw.
 *         Created Jul 13, 2012.
 */
public class ConnectResp extends MessageStruct  {
	private final static int MSG_LEN = 24;
	private final static int NAME_OFFSET = 8;
	private final static int NAME_SIZE = 16;
	private String name = "Halfpeaw";

	public ConnectResp() {
		this.msgName = "ConnectResp";
		this.messageLen = MSG_LEN;
		this.messageType = Globals.CONNECT_RESP;
		this.messageArray = new byte[this.messageLen];
	}
	public ConnectResp(byte[]bytesIn) {
		super(bytesIn);
		this.msgName = "ConnectResp";
		this.name = Globals.readArrayString(NAME_OFFSET,NAME_SIZE,this.messageArray);
	}
	
	@Override
	public boolean buildIntArray(int msgId) {
		this.messageArray = new byte[MSG_LEN];
		Globals.fillArrayString(NAME_OFFSET, NAME_SIZE, this.name, this.messageArray);
		super.buildIntArray(msgId);
		return true;
	}

	/*
	 * List of Getters and Setters for Connect
	 *
	 */
	public void setName(String name) {
		if (name.length() > NAME_SIZE) {
			System.out.println("Name has a " + NAME_SIZE + " char max");
		}
		this.name = name;
		
	}
	public String getName() {
		return this.name;
	}
}
