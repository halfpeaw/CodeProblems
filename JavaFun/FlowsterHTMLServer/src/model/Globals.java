package model;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

import javax.servlet.http.HttpServletRequest;

public class Globals {
	//Status Code
	public final static int COMMAND_MSG = 0x0000;
	public final static int SUCCESS = 0x0001;
	public final static int UNKNOWN_FAILURE = 0x0002;
	public final static int USERNAME_IN_USE = 0x0003;
	public final static int BAD_PASSWORD = 0x0004;
	public final static int BAD_USERNAME = 0x0005;
	public final static int BAD_FIELDS = 0x0006;
	public final static int BAD_TOKEN = 0x0007;
	public final static int NO_RESULT_SQL = 0x0008;
	public final static int TOKEN_EXPIRED = 0x0009;
	public final static int BAD_GAME_ID = 0x0010;
	
	
	
	
	public final static String getMessage(String messageType) {
		try {
			return getMessage(Integer.parseInt(messageType));	
		} catch (Exception e) {
			return ("Status number format not expected: " + messageType);	
		}
	}
	
	public final static void setAllRequestAttr(HttpServletRequest request, HashMap<String,String> map) 
	{
		Set<String> keys = map.keySet();
		Iterator<String>iter = keys.iterator();
		while(iter.hasNext()) {
			String key = iter.next();
			request.setAttribute(key, map.get(key));
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
			message = "User name not found!";
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
		case BAD_TOKEN:
			message = "Bad Token provided";
			break;
		case TOKEN_EXPIRED:
			message = "Token has expired";
			break;
		case BAD_GAME_ID:
			message = "The Game ID was not present in the DB";
			break;
		default:
			message = "Status code not found: " + messageType;
			break;
		}
		return message;
	}
}
