package servletCode;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import model.UserHandler;
import model.Globals;

@WebServlet("/UpdatePassword.do")
public class UserUpdatePassword extends HttpServlet {
	/**
	 * 
	 */
	private static final long serialVersionUID = -8467508978746498421L;
	UserHandler userDB;
	public void init() throws ServletException {
		userDB = UserHandler.getInstance();
	}
	
	public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		HttpSession session = request.getSession();
		String token = (String) session.getAttribute("token");
		String userName = (String) session.getAttribute("userName");
		int status = userDB.updatePassword(
				userName,
				token, 
				request.getParameter("OldPassword"),
				request.getParameter("NewPassword"));
		if (status == Globals.SUCCESS) {
			response.sendRedirect("main.jsp");
		} else {
			request.setAttribute("message",Globals.getMessage(status));
			RequestDispatcher view = request.getRequestDispatcher("UpdatePassword.jsp");
		    view.forward(request, response);
		}
	}
}
