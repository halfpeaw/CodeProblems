package servletCode;

import java.io.IOException;
import java.util.regex.Pattern;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import model.UserHandler;
import model.Globals;
@WebServlet("/NewUser.do")
public class NewUser extends HttpServlet {

	private static final long serialVersionUID = 5421480031916081028L;
	UserHandler userDB;
	public void init() throws ServletException {
		userDB = UserHandler.getInstance();
	}
	
	public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		response.setContentType("text/html");
		String userName = request.getParameter("userName");
		String password = request.getParameter("password");
		String email = request.getParameter("email");
		String fName = request.getParameter("fName");
		String lName = request.getParameter("lName");
	    
		
		String status = userDB.addUser(userName, password, email, fName, lName);
		if (status == ""+Globals.SUCCESS) {
		    RequestDispatcher view = request.getRequestDispatcher("UserAdmin.do");
		    view.forward(request, response);
		} else {
			request.setAttribute("message",Globals.getMessage(status));
		    RequestDispatcher view = request.getRequestDispatcher("NewUser.jsp");
		    view.forward(request, response);
		}
			
	}
	final static boolean isValid(String value) {
		return Pattern.matches("[a-zA-Z0-9.-_@+?]+", value);
	}

}
