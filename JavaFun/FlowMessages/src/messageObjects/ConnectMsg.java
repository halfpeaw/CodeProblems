package messageObjects;

/**
 * This is the connect class it contains the information the
 * Socket will use to connect to the servers.
 *
 * @author halfpeaw.
 *         Created Jul 13, 2012.
 */
public class ConnectMsg extends MessageStruct {
	private final static int MSG_LEN = 32;
	private final static int NAME_LEN_OFFSET = 10;
	private final static int NAME_LEN_SIZE = 2;
	private final static int NAME_OFFSET = 12;
	private final static int NAME_SIZE = 16;
	private String name = "Name";
	private String hostName ="localhost";
	private int port = 1231;
	private int nameLen = this.name.length();

	public ConnectMsg() {
		this.msgName = "ConnectMsg";
		this.messageLen = MSG_LEN;
		this.messageType = Globals.CONNECT_TYPE;
		this.messageArray = new byte[this.messageLen];
	}
	public ConnectMsg(byte[]bytesIn) {
		this.msgName = "ConnectMsg";
		this.messageArray = bytesIn;
		this.messageLen = MSG_LEN;
		this.messageType = Globals.CONNECT_TYPE;
		this.nameLen = Globals.getValue(NAME_LEN_OFFSET, NAME_LEN_SIZE, this.messageArray);
		this.name = Globals.readArrayString(NAME_OFFSET,this.nameLen,this.messageArray);
	}
	
	@Override
	public byte[] buildIntArray() {
		this.nameLen = this.name.length();
		Globals.setValue(NAME_LEN_OFFSET, NAME_LEN_SIZE, this.nameLen, this.messageArray);
		Globals.fillArrayString(NAME_OFFSET, NAME_SIZE, this.name, this.messageArray);
		return this.messageArray;
	}

	/**
	 * List of Getters and Setters for Connect
	 * @return Returns the port.
	 */
	public int getPort() {
		return this.port;
	}
	public void setPort(int port) {
		this.port = port;
	}

	public String getHostName() {
		return this.hostName;
	}

	public void setHostName(String hostName) {
		this.hostName = hostName;
	}
	public void setName(String name) {
		if (name.length() > NAME_SIZE) {
			System.out.println("Name has a " + NAME_SIZE + " char max");
		}
		this.name = name;
		this.nameLen = name.length();
		
	}
}
