package flowGameServer;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.Writer;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Date;
import java.util.HashMap;
import java.util.Random;

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
	public HashMap<Integer, ClientThread> hmap = new HashMap<Integer, ClientThread>();
	public MessageHandler handler = new MessageHandler(this);
	public GameServer() {
		
		//We need a try-catch because lots of errors can be thrown
		try {
			Random randomGenerator = new Random();
            ServerSocket serverSocket = new ServerSocket(1231);
            System.out.println("Server started at: " + new Date());
            //Loop that runs server functions
            while(true) {
                //Wait for a client to connect
                Socket socket = serverSocket.accept();
                int userId =  0;
                do {
                	userId =  randomGenerator.nextInt(32000);
                } while (hmap.containsKey(userId));
                
                System.out.println("User ID: "+userId + " Just Joined");
                //Create a new custom thread to handle the connection
                ClientThread cT = new ClientThread(this,socket, userId);
                hmap.put(userId, cT);
                 
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
	public void sendMessage(MessageStruct msg, int userId) {
    	msg.buildIntArray(1);
		(hmap.get(userId)).sendMessage(msg.getBytes());
    }
	public void receiveMessage(byte[] bytesIn, int userId) {
		handler.handleMsg(bytesIn, userId);
	}
	public void removeSocket(int userId) {
		hmap.remove(userId);
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
        int userId = 0;
        public ClientThread(GameServer server, Socket socket, int userId)
        {
            //Here we set the socket to a local variable so we can use it later
            this.threadSocket = socket;
            this.userId = userId;
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
                    receiveMessage(bytesIn,this.userId);
                }
            } catch(IOException exception) {
                System.out.println("Error: " + exception);
            }
            server.removeSocket(this.userId);
            
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
    }
    
    
}
