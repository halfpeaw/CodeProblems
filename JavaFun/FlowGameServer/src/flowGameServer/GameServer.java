package flowGameServer;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.Writer;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Arrays;
import java.util.Date;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Random;
import java.util.Set;

import messageObjects.*;



/**
 * TODO Put here a description of what this class does.
 *
 * @author halfpeaw.
 *         Created Jul 12, 2012.
 */
public class GameServer {
	/**
	 * Constructor for the game server
	 *
	 */
	public HashMap<String, ClientThread> hmap = new HashMap<String, ClientThread>();
	public MessageHandler handler = new MessageHandler(this);
	public GameServer() {
		
		//We need a try-catch because lots of errors can be thrown
		try {
			hmap.clear();
            ServerSocket serverSocket = new ServerSocket(1231);
            System.out.println("Server started at: " + new Date());
            //Loop that runs server functions
            while(true) {
                //Wait for a client to connect
                Socket socket = serverSocket.accept();
                //Create a new custom thread to handle the connection
                ClientThread cT = new ClientThread(this,socket);
                 
                //Start the thread!
                new Thread(cT).start();
                 
            }
        } catch(IOException exception) {
            System.out.println("Error: " + exception);
        }
	}
	/*
	 * userId is the destination Id affiliated with the client.  
	 * Debating if userId can be removed as an argument and just passed via the message
	 */
	public void sendMessage(MessageStruct msg, String name) {
    	msg.buildIntArray(1);
		(hmap.get(name)).sendMessage(msg.getBytes());
    }
	public void receiveMessage(byte[] bytesIn, String name) {
		handler.handleMsg(bytesIn, name);
	}
	public void removeSocket(String name) {
		hmap.remove(name);
	}
 
    /**
     * Here we create the ClientThread inner class and have it implement Runnable
     * This means that it can be used as a thread
     * 
     * @author halfpeaw.
     *         Created Jul 12, 2012.
     */
    class ClientThread implements Runnable
    {
        Socket threadSocket;
         /**
         * This constructor will be passed the socket
         *
         * @param socket
         */
        OutputStream output = null;
        GameServer server = null;
        InputStream input = null;
        String name = "Empty";
        public ClientThread(GameServer server, Socket socket)
        {
            //Here we set the socket to a local variable so we can use it later
            this.threadSocket = socket;
            this.server = server;
        }
         
        public void run()
        {
            //All this should look familiar
            try {
                //Create the streams
            	Writer out;
            	output = this.threadSocket.getOutputStream();
                input = this.threadSocket.getInputStream();
                 
                //Tell the client that he/she has connected
                byte [] bytesIn = new byte[100];
                while (true) {
                    //This will wait until a line of text has been sent
                    int len = input.read(bytesIn);
                    String outString = "";
                    for (int i = 0; i < len; i++) {
                    	outString += Integer.toHexString(bytesIn[i]) + " ";
                    }
                    System.out.println(outString);
                    if (Globals.CONNECT_TYPE == Globals.getMsgUserIDFromArray(bytesIn)) {
                    	ConnectMsg msg = new ConnectMsg(bytesIn);
                    	
                    	this.name = msg.getName();
                    	if (!server.hmap.containsKey(this.name)) {
                    		server.hmap.put(this.name, this);
                    	} else {
                    		//Send a bad response
                    		/*Set<String> keys = server.hmap.keySet();
                    		Iterator<String> e =  keys.iterator(); 
                    		while(e.hasNext()) {
                    			System.out.println("! " + e.next());
                    		}*/
                    		DisconnectMsg discMsg = new DisconnectMsg();
                    		discMsg.buildIntArray(0);
                    		output.write(discMsg.getBytes());
                    		System.out.println("Duplicate Name: " + this.name);
                    		return;
                    	}
                    }
                    receiveMessage(Arrays.copyOfRange(bytesIn, 0, len), this.name);
                }
            } catch(IOException exception) {
                System.out.println("Error: " + exception);
            }
            server.removeSocket(this.name);
            
        }
        public boolean sendMessage(byte[] bytesOut) {
        	try {
				this.output.write(bytesOut);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				return false;
			}
        	return true;
        }
    } //End Classthread
}
