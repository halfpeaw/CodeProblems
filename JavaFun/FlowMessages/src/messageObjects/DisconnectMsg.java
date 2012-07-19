/**
 * 
 */
package messageObjects;

/**
 * @author halfpeaw
 *
 */
public class DisconnectMsg extends MessageStruct {
	private final static int MSG_LEN = 12;
	public DisconnectMsg() {
		this.msgName = "Disconnect";
		this.messageType = Globals.DISCONNECT;
		
	}
	public DisconnectMsg(byte[] bytesIn) {
		super(bytesIn);
		this.msgName = "Disconnect";
	}
}
