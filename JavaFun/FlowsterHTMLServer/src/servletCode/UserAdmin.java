package servletCode;

import java.io.IOException;
import java.io.PrintWriter;
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
	DatabaseHandler db;
	public void init() throws ServletException {
		db = (DatabaseHandler)this.getServletContext().getAttribute("db");
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
			HttpSession session = request.getSession();
			session.setAttribute( "token", token );
			session.setAttribute("userName", userName);
			request.setAttribute("message",map.get("message"));
		    RequestDispatcher view = request.getRequestDispatcher("main.jsp");
		    view.forward(request, response);
		}
		
	}
	final static boolean isValid(String value) {
		return Pattern.matches("[a-zA-Z0-9]+", value);
	}
}
