package servletCode;

import java.io.IOException;
import java.util.HashMap;
import java.util.regex.Pattern;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import model.DatabaseHandler;
import model.Globals;


@WebServlet("/UserAdmin.do")
public class UserAdmin extends HttpServlet {
	/**
	 * 
	 */
	private static final long serialVersionUID = 8079262787703412186L;
	DatabaseHandler db;
	public void init() throws ServletException {
		db = (DatabaseHandler)this.getServletContext().getAttribute("db");
		db.userLogin("halfpeaw", "password");
	}
	public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		response.setContentType("text/html");
		String userName = request.getParameter("userName");
		String password = request.getParameter("password");
		if(!isValid(password)) {
			request.setAttribute("message","Bad Password");
		    RequestDispatcher view = request.getRequestDispatcher("main.jsp");
		    view.forward(request, response);
		} else if(!isValid(userName)) {
			request.setAttribute("message","Bad UserName");
		    RequestDispatcher view = request.getRequestDispatcher("main.jsp");
		    view.forward(request, response);
		} else {
			
			HashMap<String, String> map = db.userLogin(userName, password);
			String token = map.get("token");
			String status = map.get("status");
			if (!status.equals(""+Globals.SUCCESS)) {
				request.setAttribute("message",map.get("message"));
				RequestDispatcher view = request.getRequestDispatcher("main.jsp");
			    view.forward(request, response);
			} else {
				HttpSession session = request.getSession();
				session.setAttribute("token", token );
				session.setAttribute("userName", userName);
				response.sendRedirect("main.jsp");
			}
		}
		
	}
	/**
	 * Handles the log off
	 */
	public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		HttpSession session = request.getSession();
		String token = (String) session.getAttribute("token");
		String userName = (String) session.getAttribute("userName");
		session.invalidate();
		int status =  db.userLogOff(userName, token);
		request.setAttribute("message",Globals.getMessage(status));
		response.sendRedirect("main.jsp");
	}
	final static boolean isValid(String value) {
		return Pattern.matches("[a-zA-Z0-9]+", value);
	}
}
