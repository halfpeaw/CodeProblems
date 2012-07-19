package messageObjects;

public class CreateGameResp extends MessageStruct {
	public CreateGameResp() {
		this.msgName = "CreateGameResp";
		// TODO Auto-generated constructor stub
	}

	public CreateGameResp(byte[] byteIn) {
		super(byteIn);
		this.msgName = "CreateGameResp";
		// TODO Auto-generated constructor stub
	}
}
