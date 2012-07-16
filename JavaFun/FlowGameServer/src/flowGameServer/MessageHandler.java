package flowGameServer;

import java.util.*;

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
	public void handleMsg(byte [] bytesIn, String username) {
		switch (Globals.getMsgUserIDFromArray(bytesIn)) {
		case Globals.CONNECT_TYPE:
			handleConnect(new ConnectMsg(bytesIn), username);
			break;
		case Globals.GET_PLAYERS_MSG:
			handleGetPlayers(new GetPlayersMsg(bytesIn), username);
			break;
		default:
			break;
				
		}
	}
	
	private void handleConnect(ConnectMsg msg, String username) {
		ConnectResp response = new ConnectResp();
		UserObject user = new UserObject(username, msg.getPlayerType());
		user.name = msg.getName();
		userMap.put(msg.getName(), user);
		response.setName(msg.getName());
		response.setStatus(Globals.SUCCESS);
		server.sendMessage(response, username);
	}
	private void handleGetPlayers(GetPlayersMsg msg, String username) {
		int playerType = msg.getType();
		Set<String> keys = userMap.keySet();
		Iterator<String> e =  keys.iterator(); 
		List<String> NameList = new ArrayList<String>();
		while(e.hasNext()) {
			String key = e.next();
			UserObject user =  userMap.get(key);
			if (user.playerType == playerType) {
				NameList.add(user.name);
			}
			
		}
		GetPlayersResp response = new GetPlayersResp();
		response.setPlayerList(NameList.toArray(new String[NameList.size()]), playerType);
		response.setStatus(Globals.SUCCESS);
		server.sendMessage(response, username);
		
	}
}
