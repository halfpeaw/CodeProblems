package model;

import java.sql.DriverManager;
import java.sql.SQLException;

import java.sql.Connection;

public class DatabaseConnection {
	
	private static Connection con = null;
	private DatabaseConnection(String db_user, String db_password) throws SQLException, ClassNotFoundException {
		
	}
	
	public static Connection initialize(String db_user, String db_password) {
		if (con == null) {
			synchronized (DatabaseConnection.class) {
				if (con == null) {
					try {
						Class.forName("com.mysql.jdbc.Driver");
						con = DriverManager.getConnection("jdbc:mysql://localhost:3306/flowsterdb",db_user,db_password);
						return con;
					} catch (Exception e) {
						e.printStackTrace();
					}
					
				}
			}
			
		}
		return con;
	}
	public static Connection getInstance() {
		return con;
	}
}
