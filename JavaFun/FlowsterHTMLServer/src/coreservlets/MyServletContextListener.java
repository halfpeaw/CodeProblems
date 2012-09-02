package coreservlets;
import javax.servlet.*;

import model.DatabaseConnection;
import model.GameHandler;
import model.UserHandler;

public class MyServletContextListener implements ServletContextListener {

	@Override
	public void contextDestroyed(ServletContextEvent arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void contextInitialized(ServletContextEvent event) {
		// TODO Auto-generated method stub
		
		ServletContext sc = event.getServletContext();
		String db_user = sc.getInitParameter("DB_User");
		String db_password = sc.getInitParameter("DB_Pass");
		
		DatabaseConnection.initialize(db_user, db_password);
		UserHandler userDB= UserHandler.getInstance();
		GameHandler gameDB = GameHandler.getInstance();
		//sc.setAttribute("userDB", userDB);
		
	}

}
