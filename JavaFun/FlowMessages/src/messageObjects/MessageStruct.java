package messageObjects;

/**
 * TODO Put here a description of what this class does.
 *
 * @author halfpeaw.
 *         Created Jul 13, 2012.
 */
public abstract class MessageStruct {
	protected String msgName = "MessageStruct";
	protected byte [] messageArray = new byte[8];
	protected int messageType = 0;
	protected int messageLen = 0;
	public int messageID = 0;
	public int messageCRC = 0;
	protected int userID;
	//We don't make these private so that Globals can have a built in function that
	//Allows it to extract the message type from an byte array
	final static int TYPE_OFFSET = 0;
	final static int TYPE_LEN = 2;
	private final static int MSGLEN_OFFSET = 2;
	private final static int MSGLEN_LEN = 2;
	private final static int USER_OFFSET = 4;
	private final static int USERID_LEN = 4;
	//From End
	private final static int CRC_OFFSET = 2;
	private final static int CRC_LEN = 2;
	//From End
	private final static int MSGID_OFFSET = 4;
	private final static int MSGID_LEN = 2;
	
			
	/**
	 * TODO Put here a description of what this constructor does.
	 *
	 */
	public MessageStruct() {
	}

	public MessageStruct(byte[] byteIn) {
		this.messageArray = byteIn;
	}
	
	public final byte[] getBytes() {
		return this.messageArray;
	}
	public final int getMsgType() {
		return Globals.getValue(TYPE_OFFSET, TYPE_LEN, this.messageArray);
	}
	public final int getMsgLen() {
		return Globals.getValue(MSGLEN_OFFSET, MSGLEN_LEN, this.messageArray);
	}
	public final int getMsgUserId() {
		return Globals.getValue(USER_OFFSET, USERID_LEN, this.messageArray);
	}
	public boolean buildIntArray(int msgId) {
		setDefaultFields(msgId);
		return true;
	}
	public void setDefaultFields(int msgId) {
		Globals.setValue(TYPE_OFFSET, TYPE_LEN, this.messageType, this.messageArray);
		Globals.setValue(MSGLEN_OFFSET, MSGLEN_LEN, this.messageLen, this.messageArray);
		Globals.setValue(USER_OFFSET, USERID_LEN, this.userID, this.messageArray);
		Globals.setValue(this.messageLen-MSGID_OFFSET, MSGID_LEN, msgId, this.messageArray);
		//TODO write CRC Function
		Globals.setValue(this.messageLen-CRC_OFFSET, CRC_LEN, this.messageCRC, this.messageArray);

	}
	
	@Override
	public String toString() {
		return this.msgName;
	}
	
	
	
	
}
