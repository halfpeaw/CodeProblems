package flowGUIClient;

import java.net.*;
import java.io.*;
import messageObjects.*;

/**
 * TODO Put here a description of what this class does.
 *
 * @author halfpeaw.
 *         Created Jul 12, 2012.
 */
public class ClientConnection implements Runnable {
	private Socket gameSocket = null;
	private OutputStream out = null;
	private InputStream in = null;
	private MainGUI parent;
	private int count = 1;
	public boolean isConected = false;
	
	public ClientConnection(final MainGUI parent) {
		this.parent = parent;
	}
	public boolean sendMessage(MessageStruct msg) {
		System.out.println("Sending: " + msg.toString());
		count++;
		msg.buildIntArray(count);
		if (msg.getMsgType() == 0) {
			System.out.println("Message Not Configured properly: " + msg.toString());
			return false;
		}
		if (out == null || in == null || gameSocket == null) {
			System.out.println("No Socket to send on");
			return false;
		}
		
		byte [] bytesIn = msg.getBytes();
		String outString = "";
        for (int i = 0; i < bytesIn.length; i++) {
        	outString += Integer.toHexString(bytesIn[i]) + " ";
        }
        System.out.println(outString);
		try {
			out.write(bytesIn);
		} catch (Exception e) {
			e.printStackTrace();
			return false;
		}
		return true;
	}
	public void receiveMessage(byte[] bytesIn) {
		int msgId = Globals.getMsgUserIDFromArray(bytesIn);
		switch(msgId) {
			case Globals.CONNECT_RESP:
				parent.connectPanel.receiveResponse(new ConnectResp(bytesIn));
				break;
			case Globals.DISCONNECT:
				System.out.println("Received Disconnect Message");
				try {
					gameSocket.close();
					this.out.close();
					this.in.close();
					this.out = null;
					this.in = null;
					this.gameSocket = null;
				} catch (Exception e) {
					e.printStackTrace();
				}
				this.isConected = false;
			case Globals.GET_PLAYERS_RESP:
				parent.createGamePanel.receiveResponse(new GetPlayersResp(bytesIn));
				break;
			default:
				System.out.println("Message Type: " + msgId + " not recongized");
		}
	}

	public void sendConnect(ConnectMsg connect) {
		// TODO Auto-generated method stub
		if (out != null || in != null || gameSocket != null) {
			System.out.println("Already connected to the server");
			return;
		}
		System.out.println("Sending Connect Message");
		try {
	    	gameSocket = new Socket(connect.getHostName(), connect.getPort());
	        out = gameSocket.getOutputStream();
	        in = gameSocket.getInputStream();
	    } catch (UnknownHostException e1) {
	        System.err.println("Don't know about host: localhost.");
	        //System.exit(1);
	    } catch (IOException e2) {
	        System.err.println("Couldn't get I/O for "
	                           + "the connection to: localhost.");
	        //System.exit(1);
	    }
		new Thread(this).start();
		sendMessage(connect);
	}
	@Override
	public void run() {
		byte[] bytesIn = new byte[1504];
		int len = 0;
		try {
			this.isConected = true;
			while ((len = in.read(bytesIn)) != -1) {
				String outString = "";
	            for (int i = 0; i < len; i++) {
	            	outString += Integer.toHexString(bytesIn[i]) + " ";
	            }
	            System.out.println(outString);
	            receiveMessage(bytesIn);
	            //bytesIn = new byte[1504];
			}
			this.isConected = false;
			out.close();
			in.close();
			gameSocket.close();
			gameSocket = null;
			out = null;
			in = null;
			
		} catch (IOException exception) {
			// TODO Auto-generated catch-block stub.
			exception.printStackTrace();
		}
		System.out.println("Exiting Thread");
	}

}
