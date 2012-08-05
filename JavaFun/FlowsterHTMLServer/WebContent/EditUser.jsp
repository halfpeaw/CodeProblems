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
if (message != null) {
	out.print(message + "<br>");
} else {
	out.print("No Status<br>");
}

%>


<form method = "POST" action = "EditProfile.do" name ="updateUser" id="updateUser" >
	Update Login<br>
	User Name: <%=(String)request.getAttribute("UserName") %><br>
	Email&nbsp;<input type="text" size=20 name="Email" id = "Email" value=<%=(String)request.getAttribute("Email") %>><br>
	Retype Email&nbsp;<input type="text" size=20 name="emailRetype" id ="emailRetype" value=<%=(String)request.getAttribute("Email") %>><br>
	First Name&nbsp;<input type="text" size=20 name="FirstName" id = "fName" value=<%=(String)request.getAttribute("FirstName") %>><br>
	Last Name&nbsp;<input type="text" size=20 name="LastName" id = "lName" value=<%=(String)request.getAttribute("LastName") %>><br>
  <INPUT type="submit" value="Submit">
</form>
</body>
</html>