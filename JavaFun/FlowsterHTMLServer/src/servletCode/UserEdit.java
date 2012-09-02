package servletCode;

import java.io.IOException;
import java.util.HashMap;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import model.UserHandler;
import model.Globals;

@WebServlet("/EditProfile.do")
public class UserEdit extends HttpServlet {

	/**
	 * 
	 */
	private static final long serialVersionUID = 474307569077169710L;
	UserHandler userDB;
	public void init() throws ServletException {
		userDB = UserHandler.getInstance();
	}
	
	public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		HttpSession session = request.getSession();
		String token = (String) session.getAttribute("token");
		String userName = (String) session.getAttribute("userName");
		int status = userDB.updateUserInfo(
				userName,
				token, 
				request.getParameter("FirstName"),
				request.getParameter("LastName"),
				request.getParameter("Email"));
		if (status == Globals.SUCCESS) {
			response.sendRedirect("main.jsp");
		} else {
			request.setAttribute("message",Globals.getMessage(status));
			RequestDispatcher view = request.getRequestDispatcher("EditUser.jsp");
		    view.forward(request, response);
		}
	}
	public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		HttpSession session = request.getSession();
		String token = (String) session.getAttribute("token");
		String userName = (String) session.getAttribute("userName");
		HashMap<String, String> map = userDB.getUserInformation(userName, token);
		//request.setAttribute("message", "1234567");
		Globals.setAllRequestAttr(request, map);
		RequestDispatcher view = request.getRequestDispatcher("EditUser.jsp");
	    view.forward(request, response);
		//response.sendRedirect("main.jsp");
	}
}

