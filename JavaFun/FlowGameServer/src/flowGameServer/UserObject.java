package flowGameServer;

import java.util.HashMap;

import messageObjects.Globals;


/**
 * Need to figure out a way to load these from a SQL db or a XML File so that user can become
 * Perpetual
 * This file contains data stored about a user.
 * @author halfpeaw
 *
 */
public class UserObject {
	public String name = "Empty";
	public int playerType = Globals.IS_HUMAN;
	public boolean isConnected = false;
	private HashMap<Integer, String> gameList = new HashMap<Integer, String>();
	public UserObject(String name, int playerType) {
		this.playerType = playerType;
		this.name = name;
		this.isConnected = true;
	}
	public String retrieveGame(int gameId) {
		return gameList.get(gameId);
	}
	public void addGame(int gameId, String gameName) {
		gameList.put(gameId, gameName);
	}
	
	
}
