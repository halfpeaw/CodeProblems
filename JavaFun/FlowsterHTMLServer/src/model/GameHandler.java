package model;

import java.sql.*;
import java.util.HashMap;

public class GameHandler {
	static Connection con = null;
	private static GameHandler db = null;
	
	private GameHandler() {
		con = DatabaseConnection.getInstance();
	}
	
	public static GameHandler getInstance() {
		if (db == null) {
			synchronized (UserHandler.class) {
				if (db == null) {
					db = new GameHandler();					
				}
			}
		} 
		return db;
		
	}
	
	public HashMap<String, String> getBoard(String userName, String token, int gameID, int seq) {
		HashMap<String,String> resultMap = new HashMap<String,String>();
		resultMap.put("status", ""+Globals.UNKNOWN_FAILURE);
		String queryString;
		if (seq == 0) {
			queryString = "SELECT GameID, Board, BoardSize, max(Sequence) FROM flowsterdb.boards " +
					"where GameID = '"+ gameID +"' and Sequence=" +
					"(Select max(Sequence) from flowsterdb.boards where GameID='"+gameID+"')"; 
		} else {
			queryString = "SELECT Board, BoardSize FROM flowsterdb.boards " +
					"WHERE GameID = '" + gameID + "' and Sequence = '" + seq + "'";
		}
		PreparedStatement statement;
		
		try {
			statement = con.prepareStatement(queryString);
			ResultSet resultSQL = statement.executeQuery();
			if (resultSQL.first() ) {
				resultMap.put("status", ""+Globals.SUCCESS);
				resultMap.put("message", "Received GameBoard for : " + gameID);
				resultMap.put("Board", resultSQL.getString("Board"));
				resultMap.put("BoardSize", resultSQL.getString("BoardSize"));
			} else {
				resultMap.put("status", ""+Globals.BAD_GAME_ID);
				resultMap.put("message", Globals.getMessage(Globals.BAD_GAME_ID) + "Or possible bad sequence");
			}
		} catch (SQLException e) {
			resultMap.put("status", ""+Globals.UNKNOWN_FAILURE);
			resultMap.put("message", e.getMessage());
			e.printStackTrace();
		}
		return resultMap;
	}
	
	//Assume comma delim boards only containing numbers
	final static int[][] convertBoardToArray(String board, int columns, int rows) {
		String [] tokens = board.split(",");
		if (tokens.length != columns*rows) {
			System.out.println("Expected Size does not match size of board: " + tokens.length);
			return new int[0][0];
		}
		try {
			int[][] result = new int[rows][columns];
			for (int y = 0; y < rows; y++) {
				for (int x = 0; x < columns; x++) {
					result[y][x] = Integer.parseInt(tokens[y*rows+x]);
				}
			}
		} catch (NumberFormatException e) {
			System.out.println(e.getMessage());
			return new int[0][0];
		}
		return null;
	}
	static public void setMove(int gameId, String userName, String token, int x, int y) {
		validDateUser(userName, token);
	}
	static private int validDateUser(String userName, String token) {
		return UserHandler.getInstance().validateUser(userName, token);
	}
}
