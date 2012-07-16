/**
 * 
 */
package messageObjects;

/**
 * @author halfpeaw
 *
 */
public class GetPlayersMsg extends MessageStruct {
	private final static int MSG_LEN = 12;
	private int playerType;
	private int TYPE_OFFSET = 11;
	private int TYPE_LEN = 1;
	public GetPlayersMsg() {
		this.msgName = "GetPlayersMsg";
		this.messageType = Globals.GET_PLAYERS_MSG;
		this.messageLen = MSG_LEN;
		
	}
	public GetPlayersMsg(byte[] bytesIn) {
		super(bytesIn);
		this.msgName = "GetPlayersMsg";
		this.playerType = Globals.getValue(TYPE_OFFSET, TYPE_LEN, this.messageArray);
	}
	public boolean buildIntArray(int msgId) {
		Globals.setValue(TYPE_OFFSET, TYPE_LEN, this.playerType, this.messageArray);
		super.buildIntArray(msgId);
		return true;
	}
	public void setType(int type) {
		if (type != Globals.IS_AI && type != Globals.IS_HUMAN) {
			System.out.println("Inappropriate type set, setting to human");
			this.playerType = Globals.IS_HUMAN;
			return;
		}
		this.playerType = type;
	}
	public int getType() {
		return this.playerType;
	}
	
}
