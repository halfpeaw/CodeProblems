package messageObjects;

/**
 * This is a Connection Response.  Identical to the ConnectionCommand except that is has a UserID
 *
 * @author halfpeaw.
 *         Created Jul 13, 2012.
 */
public class ConnectResp extends MessageStruct  {
	private final static int MSG_LEN = 32;
	private final static int USER_ID_OFFSET = 4;
	private final static int USER_ID_SIZE = 4;
	private final static int NAME_LEN_OFFSET = 10;
	private final static int NAME_LEN_SIZE = 2;
	private final static int NAME_OFFSET = 12;
	private final static int NAME_SIZE = 16;
	private String name = "Halfpeaw";
	private int nameLen = this.name.length();

	public ConnectResp() {
		this.msgName = "ConnectResp";
		this.userID = 532;
		this.messageLen = MSG_LEN;
		this.messageType = Globals.CONNECT_RESP;
		this.messageArray = new byte[this.messageLen];
	}
	public ConnectResp(byte[]bytesIn) {
		this.msgName = "ConnectResp";
		this.messageArray = bytesIn;
		this.messageLen = this.getMsgLen();
		this.messageType = this.getMsgType();
		this.userID = this.getMsgUserId();
		this.nameLen = Globals.getValue(NAME_LEN_OFFSET, NAME_LEN_SIZE, this.messageArray);
		this.name = Globals.readArrayString(NAME_OFFSET,this.nameLen,this.messageArray);
	}
	
	@Override
	public boolean buildIntArray(int msgId) {
		this.messageArray = new byte[MSG_LEN];
		this.nameLen = this.name.length();
		Globals.setValue(USER_ID_OFFSET, USER_ID_SIZE, this.userID, this.messageArray);
		Globals.setValue(NAME_LEN_OFFSET, NAME_LEN_SIZE, this.nameLen, this.messageArray);
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
		this.nameLen = name.length();
		
	}
	public String getName() {
		return this.name;
	}
	public int getUserID() {
		return this.userID;
	}
	public void setUserID(int userID) {
		this.userID = userID;
	}
}
