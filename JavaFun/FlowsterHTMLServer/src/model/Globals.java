package model;

public class Globals {
	//Status Code
	public final static int COMMAND_MSG = 0x0000;
	public final static int SUCCESS = 0x0001;
	public final static int UNKNOWN_FAILURE = 0x0002;
	public final static int USERNAME_IN_USE = 0x0003;
	public final static int BAD_PASSWORD = 0x0004;
	public final static int BAD_USERNAME = 0x0005;
	public final static int BAD_FIELDS = 0x0006;
	
	
	
	public final static String getMessage(String messageType) {
		try {
			return getMessage(Integer.parseInt(messageType));	
		} catch (Exception e) {
			return ("Status number format not expected: " + messageType);	
		}
	}
	public final static String getMessage(int messageType) {
		String message = "";
		switch (messageType) {
		case SUCCESS:
			message = "Success";
			break;
		case UNKNOWN_FAILURE:
			message = "Unknown Failure Occured";
			break;
		case BAD_USERNAME:
			message = "User name not found";
			break;
		case BAD_PASSWORD:
			message = "Bad Password Found";
			break;
		case USERNAME_IN_USE:
			message = "User Name is already in use";
			break;
		case BAD_FIELDS:
			message = "Bad field provided";
			break;
		default:
			message = "Status code not found: " + messageType;
			break;
		}
		return message;
	}
}
