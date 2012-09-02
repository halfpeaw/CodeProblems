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

import model.GameHandler;
import model.Globals;

@WebServlet("/GetBoard.do")
public class GetGameBoard extends HttpServlet{
	public void init() throws ServletException {
		
	}
	
	public void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		response.setContentType("text/html");
		HttpSession session = request.getSession();
		String token = (String) session.getAttribute("token");
		String userName = (String) session.getAttribute("userName");
		int seq =  Integer.parseInt(request.getParameter("Sequence"));
		int gameID = Integer.parseInt(request.getParameter("GameID"));
		HashMap<String, String> map = 
				GameHandler.getInstance().getBoard(userName, token, gameID, seq);
		if (Integer.parseInt(map.get("status")) == Globals.SUCCESS) {
			request.setAttribute("message",Globals.getMessage(map.get("status")));
			request.setAttribute("board", map.get("Board"));
			request.setAttribute("boardSize",map.get("BoardSize"));
		} else {
			request.setAttribute("message",Globals.getMessage(map.get("status")));
		}
		RequestDispatcher view = request.getRequestDispatcher("GetGameBoard.jsp");
		view.forward(request, response);
	}
}
