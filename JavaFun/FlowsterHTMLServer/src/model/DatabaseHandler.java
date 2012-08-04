package model;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.*;
import java.util.Date;
import java.util.HashMap;
import java.util.Random;
import java.util.regex.Pattern;


public class DatabaseHandler {
	private Connection con;
	Random randGenerator = new Random();
	//activeUsers uses UserName as a key and then a userInfo private class
	private HashMap<String,UserInfo> activeUsers = new HashMap<String,UserInfo>() ; 
	public DatabaseHandler(String db_user, String db_password) {
		//Instantiate DB Connection Here
		try {
			Class.forName("com.mysql.jdbc.Driver");
			con = DriverManager.getConnection("jdbc:mysql://localhost:3306/flowsterdb",db_user,db_password);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	public String getMessage() {
		return "I am a database handler!";
	}
	//todo: add hash function for password and field validation
	/**
	 * Validates username and password and creates a token
	 * @param userName
	 * @param password
	 * @return HashMap contains keys 'status', 'token' and 'message'
	 */
	public HashMap<String,String> userLogin(String userName, String password) {
		String token = "FFFFFFFFAB";
		String status = ""+Globals.UNKNOWN_FAILURE;
		String message = "No Message";
		HashMap<String, String> result = new HashMap<String, String>();
		
		if (!isValid(userName) || !isValid(password)) {
			result.put("token", token);
			result.put("status", ""+Globals.BAD_FIELDS);
			result.put("message", "User Name or Password has bad characters");
			return result;
		}
		try {
			PreparedStatement statement = con.prepareStatement("SELECT u.`Password` FROM flowsterdb.users u where UserName = '"+ userName+"'");
			ResultSet resultSQL = statement.executeQuery();
			if (resultSQL.first() ) {
				if (resultSQL.getString("Password").equals(password)) {
					status = ""+Globals.SUCCESS;
					token = hashFunction(userName + randGenerator.nextInt(10000));
					activeUsers.put(userName, new UserInfo(token));
				} else {
					status = ""+Globals.BAD_PASSWORD;
				}
			} else {
				status = "" +Globals.BAD_USERNAME;
			}
		
		} catch (SQLException e) {
			status = "" + Globals.UNKNOWN_FAILURE;
			e.printStackTrace();
		}
		message = Globals.getMessage(status);
		result.put("token", token);
		result.put("status", status);
		result.put("message", message);
		return result;
	}
	/**
	 * This function inserts a user record in to the flowster database
	 * Note: Does not automatically log a user in that has to be called via the
	 * userLogin function
	 * 
	 * @param userName
	 * @param password
	 * @param email
	 * @param fName
	 * @param lName
	 * @return
	 */
	public int updateUser(String userName, String password, 
			String email, String fName, String lName) {
		int status = Globals.BAD_FIELDS;
		final String userQuery = "SELECT UserName FROM flowsterdb.users u " +
				"WHERE u.`UserName`='"+userName+"'";
		final String insertQuery = "INSERT INTO flowsterdb.users" +
				"(UserName, Password, FirstName, LastName, Email) " +
				"	VALUES('"+userName+"', '"+password+"', '"
				+fName+"', '"+lName+"', '"+email+"')";
		password = hashFunction(password);
		PreparedStatement statement;
		ResultSet resultSQL;
		if (!isValid(userName) || !isValid(password) || !isValid(email) 
				|| isValid(fName) || isValid(lName)) {
			return Globals.BAD_FIELDS;
		}
		
		try {
			statement = con.prepareStatement(userQuery);
			resultSQL = statement.executeQuery();
			if (resultSQL.first() ) {
				return Globals.USERNAME_IN_USE;
			}
			statement = con.prepareStatement(insertQuery);
			resultSQL = statement.executeQuery();
			status = Globals.SUCCESS;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return Globals.UNKNOWN_FAILURE;
		}
		return status;
	}
	final static boolean isValid(String value) {
		return Pattern.matches("[a-zA-Z0-9.-_@+?]+", value);
	}
	
	final static String hashFunction(String encryptString) {
		MessageDigest messageDigest;
		String encryptedString = "1234567890";
		try {
			messageDigest = MessageDigest.getInstance("SHA-256");
			messageDigest.update(encryptString.getBytes());
			encryptedString = new String(messageDigest.digest());
		} catch (NoSuchAlgorithmException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return encryptedString;
		
	}
	/*
	 * This class contains information about active users.
	 * Much of this information could be stored within a session but
	 * wanted to allow for code to be adapted for stand alone app.
	 */
	private class UserInfo {
		public String token = "EMPTY";
		public Date expiry = null;
		public UserInfo(String token) {
			this.token = token;
		}
	}
		
}
