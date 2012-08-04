<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>New User Page</title>
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
<form method = "POST" action = "NewUser.do" name = "updateUser" id="updateUser" >
	Enter Login<br>
	User Name&nbsp;<input type="text" size=30 name="userName" id="userName" ><br>
	Password&nbsp;<input type="text" size=20 name="password" id="password"><br>
	Retype Password&nbsp;<input type="text" size=20 name="passwordRetype" id = "passwordRetype" ><br>
	Email&nbsp;<input type="text" size=20 name="email" id = "email"><br>
	Retype Email&nbsp;<input type="text" size=20 name="emailRetype" id = "emailRetype"><br>
	First Name&nbsp;<input type="text" size=20 name="fName" id = "fName"><br>
	Last Name&nbsp;<input type="text" size=20 name="lName" id = "lName"><br>
  <INPUT type="submit" value="Submit">
</form>
</body>
</html>