package messageObjects;

public class CreateGameMsg extends MessageStruct {
	private int playerCount;
	private int gameBoardSize;
	private String[] playerList;
	private String gameName = "";
	
	private final static int FIX_LEN = 16  + GAME_NAME_SIZE;
	private final static int GAME_NAME_OFFSET = 8;
	private final static int GAME_SIZE_BOARD_OFFSET = 42;
	private final static int GAME_SIZE_BOARD_SIZE = 1;
	private final static int NUM_PLAYER_OFFSET = 43;
	private final static int NUM_PLAYER_SIZE = 1;
	private final static int PLAYER_NAME_OFFSET = 44;
	
	
	public CreateGameMsg() {
		this.msgName = "ConnectResp";
		// TODO Auto-generated constructor stub
		this.messageType = Globals.CREATE_GAME_MSG;
	}

	public CreateGameMsg(byte[] byteIn) {
		super(byteIn);
		this.msgName = "ConnectResp";
		this.gameName = Globals.readArrayString(GAME_NAME_OFFSET, GAME_NAME_SIZE, this.messageArray);
		this.gameBoardSize = Globals.getValue(GAME_SIZE_BOARD_OFFSET, GAME_SIZE_BOARD_SIZE, this.messageArray);
		this.playerCount = Globals.getValue(NUM_PLAYER_OFFSET, NUM_PLAYER_SIZE, this.messageArray);
		this.playerList = new String[this.playerCount];
		for (int i = 0; i < this.playerCount; i++) {
			this.playerList[i] = Globals.readArrayString(PLAYER_NAME_OFFSET*(i+1), PLAYER_NAME_SIZE, this.messageArray);
		}
	}
	@Override
	public boolean buildIntArray(int msgId) {
		this.messageArray = new byte[FIX_LEN+PLAYER_NAME_SIZE*this.playerCount];
		Globals.fillArrayString(GAME_NAME_OFFSET, GAME_NAME_SIZE, this.gameName, this.messageArray);
		Globals.setValue(NUM_PLAYER_OFFSET, NUM_PLAYER_SIZE, this.playerCount, this.messageArray);
		Globals.setValue(GAME_SIZE_BOARD_OFFSET, GAME_SIZE_BOARD_SIZE, this.gameBoardSize, this.messageArray);
		for (int i = 0; i < this.playerCount; i++) {
			Globals.fillArrayString(PLAYER_NAME_OFFSET*(i+1), PLAYER_NAME_SIZE, this.playerList[i], this.messageArray);
		}
		super.buildIntArray(msgId);
		return true;
	}
	public void setPlayerList(String[] players) {
		this.playerList = players;
		this.playerCount = players.length;
	}
	public String[] getPlayerList() {
		return this.playerList;
	}
	public void setGameBoardSize(int gameBoardSize) {
		this.gameBoardSize = gameBoardSize;
	}
	public int getGameBoardSize() {
		return this.gameBoardSize;
	}
	public void setGameName(String name) {
		this.gameName = name;
	}
	public String getGameName() {
		return this.gameName;
	}
	

}
