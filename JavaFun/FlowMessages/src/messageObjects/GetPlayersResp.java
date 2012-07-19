/**
 * 
 */
package messageObjects;


/**
 * @author halfpeaw
 *
 */
public class GetPlayersResp extends MessageStruct {
	private String [] playerList = {};
	private int playerCount = 0;
	private int playerType = Globals.IS_HUMAN;
	private final static int PCOUNT_OFFSET = 14;
	private final static int PCOUNT_LEN = 2;
	private final static int TYPE_OFFSET = 13;
	private final static int TYPE_LEN = 1;
	private final static int NAME_OFFSET = 16;
	//Name size declared in globals
	//This number is adjusted based on the playerCount
	private final static int FIX_LEN = 20;		
	/**
	 * 
	 */
	public GetPlayersResp() {
		this.msgName = "GetPlayerResp";
		this.messageType = Globals.GET_PLAYERS_RESP;
	}

	
	/**
	 * @param byteIn
	 */
	public GetPlayersResp(byte[] byteIn) {
		super(byteIn);
		this.msgName = "GetPlayerResp";
		this.playerType = Globals.getValue(TYPE_OFFSET, TYPE_LEN, this.messageArray);
		this.playerCount = Globals.getValue(PCOUNT_OFFSET, PCOUNT_LEN, this.messageArray);
		this.playerList = new String[playerCount];
		for (int i = 0; i < this.playerCount; i++) {
			this.playerList[i] = Globals.readArrayString(NAME_OFFSET*(i+1), PLAYER_NAME_SIZE, this.messageArray);
		}
		
		// TODO Auto-generated constructor stub
	}
	
	@Override
	public boolean buildIntArray(int msgId) {
		this.messageArray = new byte[FIX_LEN + this.playerCount*PLAYER_NAME_SIZE];
		Globals.setValue(PCOUNT_OFFSET, PCOUNT_LEN, this.playerCount, this.messageArray);
		Globals.setValue(TYPE_OFFSET, TYPE_LEN, this.playerType, this.messageArray);
		for (int i = 0; i < this.playerCount; i++) {
			Globals.fillArrayString(NAME_OFFSET*(i+1),PLAYER_NAME_SIZE , this.playerList[i], this.messageArray);
		}
		super.buildIntArray(msgId);
		return true;
	}
	
	public void setPlayerList(String[] playerList, int playerType) {
		this.playerList = playerList;
		this.playerCount = this.playerList.length;
		this.playerType = playerType;

	}
	public String[] getPlayerList() {
		return this.playerList;
	}
	public int getPlayerType() {
		return this.playerType;
	}

}
