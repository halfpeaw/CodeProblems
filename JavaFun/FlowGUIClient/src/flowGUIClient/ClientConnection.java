package flowGUIClient;

import java.net.*;
import java.io.*;
import messageObjects.ConnectMsg;

/**
 * TODO Put here a description of what this class does.
 *
 * @author halfpeaw.
 *         Created Jul 12, 2012.
 */
public class ClientConnection {
	public ClientConnection() {
		ConnectMsg connect = new ConnectMsg();
		connect.setName("AlexHalfpenny");
		Socket echoSocket = null;
		OutputStream out = null;
		InputStream in = null;
	    try {
	        echoSocket = new Socket(connect.getHostName(), connect.getPort());
	        out = echoSocket.getOutputStream();
	        in = echoSocket.getInputStream();
	    } catch (UnknownHostException e1) {
	        System.err.println("Don't know about host: localhost.");
	        System.exit(1);
	    } catch (IOException e2) {
	        System.err.println("Couldn't get I/O for "
	                           + "the connection to: localhost.");
	        System.exit(1);
	    }
	    
	
		byte[] bytesIn = new byte[100];
		int len = 0;
		try {
			connect.setDefaultFields(1);
			out.write(connect.buildIntArray());
			while ((len = in.read(bytesIn)) != -1) {
				String outString = "";
	            for (int i = 0; i < len; i++) {
	            	outString += Integer.toHexString(bytesIn[i]) + " ";
	            }
	            System.out.println(outString);
			}
			out.close();
			in.close();
			echoSocket.close();
		} catch (IOException exception) {
			// TODO Auto-generated catch-block stub.
			exception.printStackTrace();
		}
		
		
		}
	}
