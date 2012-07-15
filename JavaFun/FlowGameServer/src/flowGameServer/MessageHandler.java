package flowGameServer;

import java.util.HashMap;

import flowGameServer.GameServer.ClientThread;
import messageObjects.*;

/**
 * This Class is responsible for handling the flow of messages.
 * @author halfpeaw
 *
 */
public class MessageHandler {
	GameServer server;
	HashMap<String, UserObject> userMap = new HashMap<String, UserObject>();
	HashMap<Integer, GameObject> gameMap = new HashMap<Integer, GameObject>();
	public MessageHandler(GameServer server) {
		this.server = server;
	}
	public void handleMsg(byte [] bytesIn, String name) {
		switch (Globals.getMsgUserIDFromArray(bytesIn)) {
		case Globals.CONNECT_TYPE:
			handleConnect(new ConnectMsg(bytesIn), name);
			break;
		default:
			break;
				
		}
	}
	
	private void handleConnect(ConnectMsg msg, String name) {
		ConnectResp response = new ConnectResp();
		UserObject user = new UserObject(name);
		user.name = msg.getName();
		userMap.put(msg.getName(), user);
		response.setName(msg.getName());
		response.setStatus(Globals.SUCCESS);
		server.sendMessage(response, name);
	}
}
