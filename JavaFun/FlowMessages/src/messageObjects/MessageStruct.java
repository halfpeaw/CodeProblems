package messageObjects;

/**
 * TODO Put here a description of what this class does.
 *
 * @author halfpeaw.
 *         Created Jul 13, 2012.
 */
public abstract class MessageStruct {
	protected String msgName = "MessageStruct";
	protected byte [] messageArray = new byte[12];
	protected int messageType = 0;
	protected int messageLen = 0;
	public int messageID = 0;
	public int messageCRC = 0;
	public int status = 0;
	//We don't make these private so that Globals can have a built in function that
	//Allows it to extract the message type from an byte array
	final static int TYPE_OFFSET = 0;
	final static int TYPE_LEN = 2;
	private final static int MSGLEN_OFFSET = 2;
	private final static int MSGLEN_LEN = 2;
	//From End
	private final static int CRC_OFFSET = 2;
	private final static int CRC_LEN = 2;
	//From End
	private final static int MSGID_OFFSET = 4;
	private final static int MSGID_LEN = 2;
	//All responses will have a status in this location
	final static int STATUS_OFFSET = 6;
	final static int STATUS_LEN = 2;
	
			
	/**
	 * TODO Put here a description of what this constructor does.
	 *
	 */
	public MessageStruct() {
	}

	public MessageStruct(byte[] byteIn) {
		this.messageArray = byteIn;
		getDefaults();
	}
	private void getDefaults() {
		//MessageLen must always be first
		this.messageLen = this.getMsgLen();
		this.messageType = this.getMsgType();
		if (this.messageArray.length < this.messageLen) {
			System.out.println("Something is wrong with the message lenght: " + this.messageLen + " For: " +this.messageType +
					" Array Size: " + this.messageArray.length);
		}
		this.status = Globals.getValue(STATUS_OFFSET, STATUS_LEN, this.messageArray);
		this.messageID = Globals.getValue(this.messageLen-MSGID_OFFSET, MSGID_LEN, this.messageArray);
		this.messageCRC = Globals.getValue(this.messageLen-CRC_OFFSET, CRC_LEN, this.messageArray);
		
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
	public final void setStatus(int status) {
		Globals.setValue(STATUS_OFFSET, STATUS_LEN, status, this.messageArray);
		this.status = status;
		
	}
	public final int getStatus() {
		return Globals.getValue(STATUS_OFFSET, STATUS_LEN, this.messageArray);
	}
	public boolean buildIntArray(int msgId) {
		setDefaultFields(msgId);
		return true;
	}
	public void setDefaultFields(int msgId) {
		Globals.setValue(TYPE_OFFSET, TYPE_LEN, this.messageType, this.messageArray);
		Globals.setValue(MSGLEN_OFFSET, MSGLEN_LEN, this.messageLen, this.messageArray);
		Globals.setValue(STATUS_OFFSET, STATUS_LEN, this.status, this.messageArray);
		Globals.setValue(this.messageLen-MSGID_OFFSET, MSGID_LEN, msgId, this.messageArray);
		//TODO write CRC Function
		Globals.setValue(this.messageLen-CRC_OFFSET, CRC_LEN, this.messageCRC, this.messageArray);

	}
	
	@Override
	public String toString() {
		return this.msgName;
	}
	
	
	
	
}
