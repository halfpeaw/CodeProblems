<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<script type="text/javascript">
function validateForm()
{
var newpass1=document.forms["updatePassword"]["NewPassword"].value;
var newpass2=document.forms["updatePassword"]["passwordRetype"].value;
if (newpass1!=newpass2)
  {
  alert("Passwords must match");
  return false;
  }
}
</script>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Update Password</title>
</head>
<body>

<%
String message = (String)request.getAttribute("message");
if (message != null) {
	out.print(message + "<br>");
}
%>


<!--form method = "POST" action = "UpdatePassword.do" name = "updatePassword" id="updateUser" -->
<form method = "POST" action = "UpdatePassword.do" onsubmit="return validateForm()" name = "updatePassword" id="updateUser" >
	Update Password<br>
	User Name: <%=(String)session.getAttribute("userName") %><br>
	Old Password&nbsp;<input type="text" size=20 name="OldPassword" id="password"><br>
	New Password&nbsp;<input type="text" size=20 name="NewPassword" id="password"><br>
	Retype Password&nbsp;<input type="text" size=20 name="passwordRetype" id = "passwordRetype" ><br>
  <INPUT type="submit" value="Submit">
</form>
</body>
</html>