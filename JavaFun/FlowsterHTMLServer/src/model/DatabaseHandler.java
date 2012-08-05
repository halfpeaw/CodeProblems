package model;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.*;
import java.util.Calendar;
import java.util.GregorianCalendar;
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
		userName = userName.trim();
		password = password.trim();
		HashMap<String, String> result = new HashMap<String, String>();
		
		if (!isValid(userName) || !isValid(password)) {
			result.put("token", token);
			result.put("status", ""+Globals.BAD_FIELDS);
			result.put("message", "User Name or Password has bad characters");
			return result;
		}
		try {
			PreparedStatement statement = con.prepareStatement("SELECT Password, Salt FROM flowsterdb.users u where UserName = '"+ userName+"'");
			ResultSet resultSQL = statement.executeQuery();
			if (resultSQL.first() ) {
				password = hashFunction(password+resultSQL.getInt("Salt"));
				if (resultSQL.getString("Password").equals(password)) {
					status = ""+Globals.SUCCESS;
					token = hashFunction(userName + randGenerator.nextInt(10000));
					message = "User Logged in: " + token;
					activeUsers.put(userName, new UserInfo(token));
				} else {
					status = ""+Globals.BAD_PASSWORD;
					message = "Incorrect Password";
				}
			} else {
				status = "" +Globals.BAD_USERNAME;
				message = "User Name not found";
			}
		
		} catch (SQLException e) {
			status = "" + Globals.UNKNOWN_FAILURE;
			message = e.getMessage();
			e.printStackTrace();
		}
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
	public String addUser(String userName, String password, 
			String email, String fName, String lName) {
		int salt = randGenerator.nextInt(10000);
		userName = userName.trim();
		password = password.trim();
		email = email.trim();
		fName = fName.trim();
		lName = lName.trim();
		password = hashFunction(password+salt);
		final String userQuery = "SELECT UserName FROM flowsterdb.users u " +
				"WHERE u.`UserName`='"+userName+"'";
		final String insertQuery = "INSERT INTO flowsterdb.users" +
				"(UserName, Password, FirstName, LastName, Email, Salt) " +
				"	VALUES('"+userName+"', '"+password+"', '"
				+fName+"', '"+lName+"', '"+email+"', "+salt+")";
		PreparedStatement statement;
		ResultSet resultSQL;
		if (!isValid(password)) {
			return "bad passwd: " + password;
		}
		if (!isValid(email)) {
			return "Bad email: " + email;
		}
		if (!isValid(userName)) {
			return "Bad UserName: " + userName;
		}
		if (!isValid(fName)) {
			return "Bad First Name: " + fName;
		}
		if (!isValid(lName)) {
			return "Bad LName: " + lName;
		}
		
		if (!(isValid(userName) && isValid(password) && isValid(email) 
				&& isValid(fName) && isValid(lName))) {
			return ""+Globals.BAD_FIELDS;
		}
		
		try {
			statement = con.prepareStatement(userQuery);
			resultSQL = statement.executeQuery();
			if (resultSQL.first() ) {
				return ""+Globals.USERNAME_IN_USE;
			}
			statement = con.prepareStatement(insertQuery);
			int updateResult = statement.executeUpdate();
			if (updateResult > 0) {
				return ""+Globals.SUCCESS;
			} else {
				return ""+Globals.NO_RESULT_SQL; 	
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return e.getMessage();
			//return ""+Globals.UNKNOWN_FAILURE;
		}
		//return ""+status;
	}
	
	/**
	 * This function will remove a user from the activeUsers hash table
	 * @param userName
	 * @param token
	 * @return
	 */
	public int userLogOff(String userName, String token) {
		int validation = validateUser(userName, token);
		if (validation == Globals.SUCCESS) {
			activeUsers.remove(userName);
			return Globals.SUCCESS;
		} else {
			return validation;
		}
			
	}
	
	public HashMap<String,String> getUserInformation(String userName, String token) {
		HashMap<String,String> resultMap = new HashMap<String,String>();
		int status = validateUser(userName, token);
		// TODO remove debug code
		status = Globals.SUCCESS;
		if (status != Globals.SUCCESS) {
			resultMap.put("status", ""+status);
			resultMap.put("message", Globals.getMessage(status));
			return resultMap;
		}
		String queryString = "SELECT UserName, FirstName, LastName, Email FROM flowsterdb.users " +
				"WHERE UserName = '" + userName + "'";
		PreparedStatement statement;
		try {
			statement = con.prepareStatement(queryString);
			ResultSet resultSQL = statement.executeQuery();
			if (resultSQL.first() ) {
				resultMap.put("status", ""+Globals.SUCCESS);
				resultMap.put("message", "Received user info on: " + userName);
				resultMap.put("UserName", resultSQL.getString("UserName"));
				resultMap.put("FirstName", resultSQL.getString("FirstName"));
				resultMap.put("LastName", resultSQL.getString("LastName"));
				resultMap.put("Email", resultSQL.getString("Email"));
			} else {
				resultMap.put("status", ""+Globals.BAD_USERNAME);
				resultMap.put("message", Globals.getMessage(Globals.BAD_USERNAME) +":" + userName);
			}
		} catch (SQLException e) {
			resultMap.put("status", ""+Globals.UNKNOWN_FAILURE);
			resultMap.put("message", e.getMessage());
			e.printStackTrace();
		}
		
		return resultMap;
	}

	public int updateUserInfo(String userName, String token, String FirstName, String LastName, String Email) {
		int status = validateUser(userName, token);
		// TODO remove debug code
		status = Globals.SUCCESS;
		if (status != Globals.SUCCESS) {
			return status;
		}
		if (!(isValid(FirstName) && isValid(LastName) && isValid(Email))) {
			return Globals.BAD_FIELDS;
		}
		try {
			PreparedStatement statement;
			statement = con.prepareStatement
					("UPDATE flowsterdb.users SET Email='"+Email+"', FirstName='"+FirstName+"', " +
							"LastName='"+LastName+"' WHERE UserName = '"+ userName+"'");
			int updateResult = statement.executeUpdate();
			if (updateResult < 1) {
				status = Globals.NO_RESULT_SQL;
			}
			return Globals.SUCCESS;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return Globals.UNKNOWN_FAILURE;
		}
		//return ""+status;
	}
	
	
	/**
	 * This function will update the password in the database
	 * @param userName
	 * @param token
	 * @param oldPassword
	 * @param newPassword
	 * @return Global Status
	 */
	public int updatePassword(String userName, String token, String oldPassword, String newPassword) {
		int status = validateUser(userName, token);
		// TODO remove debug code
		status = Globals.SUCCESS;
		if (status != Globals.SUCCESS) {
			return status;
		}
		try {
			PreparedStatement statement;
			statement = con.prepareStatement("SELECT Password, Salt FROM flowsterdb.users u where UserName = '"+ userName+"'");
			ResultSet resultSQL = statement.executeQuery();
			if (resultSQL.first() ) {
				oldPassword = hashFunction(oldPassword+resultSQL.getInt("Salt"));
				newPassword = hashFunction(newPassword+resultSQL.getInt("Salt"));
				if (resultSQL.getString("Password").equals(oldPassword)) {
					statement = con.prepareStatement("UPDATE flowsterdb.users SET Password='"+newPassword+"' WHERE UserName = '"+ userName+"'");
					int updateResult = statement.executeUpdate();
					if (updateResult < 1) {
						status = Globals.NO_RESULT_SQL;
					}
				} else {
					status = Globals.BAD_PASSWORD;
				}
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			status = Globals.UNKNOWN_FAILURE;
		}
		return status;
	}

	public int validateUser(String userName, String token) {
		if (activeUsers.get(userName) == null) {
			return Globals.BAD_USERNAME;
		}
		if (!activeUsers.get(userName).expiry.after(new GregorianCalendar())) {
			activeUsers.remove(userName);
			return Globals.TOKEN_EXPIRED;
		
		}
		if (!activeUsers.get(userName).token.equals(token)) {
			return Globals.BAD_TOKEN;
		
		}
		return Globals.SUCCESS;
	}

	private final static boolean isValid(String value) {
		return Pattern.matches("[a-zA-Z0-9.-_@+? ]+", value);
	}
	
	private final static String hashFunction(String encryptString) {
		MessageDigest messageDigest;
		String encryptedString = "1234567890";
		try {
			messageDigest = MessageDigest.getInstance("SHA-256");
			messageDigest.update(encryptString.getBytes());
			BigInteger bigInt = new BigInteger(messageDigest.digest()).abs();
			encryptedString = bigInt.toString(16); // 16 is the radix
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
		public Calendar expiry = null;
		public UserInfo(String token) {
			this.token = token;
			expiry = new GregorianCalendar();
			expiry.add(Calendar.HOUR, 1);
			
		}
	}
		
}
