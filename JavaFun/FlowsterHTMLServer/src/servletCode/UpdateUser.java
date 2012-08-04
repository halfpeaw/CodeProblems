package servletCode;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;

import model.DatabaseHandler;
@WebServlet("/UpdateUser.do")
public class UpdateUser extends HttpServlet {
	DatabaseHandler db;
	public void init() throws ServletException {
		db = (DatabaseHandler)this.getServletContext().getAttribute("db");
	}

}
