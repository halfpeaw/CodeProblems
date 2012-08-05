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
boolean loggedIn = false;
String message = (String)request.getAttribute("message");
if (message != null) {
	out.print(message + "<br>");
} 
if (session.isNew() ) {
	out.print("No Session Available");
} else if ((String)session.getAttribute("userName") == null) {
	
	out.print("Not logged in");
} else {
	out.print("Welcome: " + (String)session.getAttribute("userName"));
	loggedIn = true;
}
%>
<% if (!loggedIn) {%>
<form method = "POST" action = "UserAdmin.do">
	Enter Login<br>
	User Name&nbsp;<input type="text" size=30 name="userName"><br>
	Password&nbsp;<input type="text" size=20 name="password"><br>
  <INPUT type="submit" value="Login">
  <A Href="./NewUser.jsp">Create Login</A>
</form>
<% } else { %>
<br>
<A Href="./EditProfile.do">Edit Profile</A><br>
<A Href="./UpdatePassword.jsp">Update Password</A><br>
<A Href="./UserAdmin.do">Log Off</A><br>

<% } %>
</body>
</html>