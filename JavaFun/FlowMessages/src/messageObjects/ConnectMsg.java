package messageObjects;

/**
 * This is the connect class it contains the information the
 * Socket will use to connect to the servers.
 *
 * @author halfpeaw.
 *         Created Jul 13, 2012.
 */
public class ConnectMsg extends MessageStruct {
	private final static int MSG_LEN = 24;
	private final static int NAME_OFFSET = 8;
	private final static int NAME_SIZE = 16;
	private String name = "Name";
	private String hostName ="localhost";
	private int port = 1231;

	public ConnectMsg() {
		this.msgName = "ConnectMsg";
		this.messageLen = MSG_LEN;
		this.messageType = Globals.CONNECT_TYPE;
		this.messageArray = new byte[this.messageLen];
	}
	public ConnectMsg(byte[]bytesIn) {
		super(bytesIn);
		this.msgName = "ConnectMsg";
		this.messageType = Globals.CONNECT_TYPE;
		this.name = Globals.readArrayString(NAME_OFFSET, NAME_SIZE, this.messageArray);
	}
	
	public boolean buildIntArray(int msgId) {
		Globals.fillArrayString(NAME_OFFSET, NAME_SIZE, this.name, this.messageArray);
		super.buildIntArray(msgId);
		return true;
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
		
	}
	public String getName() {
		return this.name;
	}
}
