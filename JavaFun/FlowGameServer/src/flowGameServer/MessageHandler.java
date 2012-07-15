package flowGameServer;

import messageObjects.*;

/**
 * This Class is responsible for handling the flow of messages.
 * @author halfpeaw
 *
 */
public class MessageHandler {
	GameServer server;
	public MessageHandler(GameServer server) {
		this.server = server;
	}
	public void handleMsg(byte [] bytesIn, int userId) {
		switch (Globals.getMsgUserIDFromArray(bytesIn)) {
		case Globals.CONNECT_TYPE:
			handleConnect(new ConnectMsg(bytesIn), userId);
			break;
		default:
			break;
				
		}
	}
	
	private void handleConnect(ConnectMsg msg, int userId) {
		ConnectResp response = new ConnectResp();
		response.setName(msg.getName());
		response.setUserID(userId);
		server.sendMessage(response, userId);
	}
}
