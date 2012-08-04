<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Main Page</title>
</head>
<body>
<%
String message = (String)request.getAttribute("message");
if (message != null) {
	out.print(message + "<br>");
} else {
	out.print("No Status<br>");
}

%>
<% if (true) {%>
<form method = "POST" action = "UserAdmin.do">
	Enter Login<br>
	User Name&nbsp;<input type="text" size=30 name="userName"><br>
	Password&nbsp;<input type="text" size=20 name="password"><br>
  <INPUT type="submit" value="Login">
  <A Href="./newUser.jsp">Create Login</A>
</form>
<% } else { %>
<br> You are already logged in
<% } %>

</body>
</html>