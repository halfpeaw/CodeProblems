package coreservlets;
import javax.servlet.*;

import model.DatabaseHandler;

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
		
		
		DatabaseHandler db = new DatabaseHandler(db_user, db_password);
		sc.setAttribute("db", db);
		
	}

}
