<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
<%
String message = (String)request.getAttribute("message");
String board = (String)request.getAttribute("board");
if (message != null) {
	out.print(message + "<br>");
	out.print(board + "<br>");
} else {
	out.print("No Status<br>");
}

%>
<form method = "POST" action = "GetBoard.do" name = "updateUser" id="updateUser" >
	Enter Game ID<br>
	Game ID&nbsp;<input type="text" size=30 name="GameID" id="GameID" ><br>
	Seq ID&nbsp;<input type="text" size=30 name="Sequence" id="Sequence" value = "0" ><br>
<INPUT type="submit" value="Submit">
</form>
</body>
</html>