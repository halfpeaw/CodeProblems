package flowGUIClient;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.*;

import messageGUI.*;


/**
 * TODO Put here a description of what this class does.
 *
 * @author halfpeaw.
 *         Created Jul 10, 2012.
 */
public class BuildGUI extends JFrame implements MouseListener, MouseMotionListener, ActionListener {
	private JPanel gameBoardPanel;
	private boolean playerOneTurn = true;
	private Dimension boardSize = new Dimension(640, 640);
	private Dimension messageSize = new Dimension(300, 640);
	private JMenuBar menuBar = new JMenuBar();
	private JMenu menu = new JMenu("File");
	private JPanel msgPanel = new JPanel();
		
	/**
	 * TODO Put here a description of this field.
	 */
	JLayeredPane layeredPane;
	/**
	 * TODO This constructor is build the panel used for displaying out problems.
	 *
	 */
	public BuildGUI() {
		super("My Frame");
		MsgGUIBase connectPanel = new ConnectMsgGUI();
		JPanel bigPanel = new JPanel();
		//bigPanel.setLayout(new GridLayout(1,2));
		bigPanel.setSize(new Dimension(640,740));
		this.menuBar.add(this.menu);
		JMenuItem menuItem = new JMenuItem("Reset");
		menuItem.addActionListener(this);
		this.menu.add(menuItem);
		this.setJMenuBar(this.menuBar);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.layeredPane = new JLayeredPane();
		//getContentPane().add(this.layeredPane);
		//gamePanel.add(this.layeredPane);
	  	this.layeredPane.setPreferredSize(this.boardSize);
	  	this.layeredPane.addMouseListener(this);
	  	this.layeredPane.addMouseMotionListener(this);
	  	this.gameBoardPanel = new JPanel();
	  	this.layeredPane.add(this.gameBoardPanel, JLayeredPane.DEFAULT_LAYER);
	  	bigPanel.add(this.layeredPane);
	  	//this.msgPanel.setPreferredSize(this.messageSize);
	  	//this.msgPanel.add(new JButton("Push me"));
	  	bigPanel.add(new JButton("Send"));
	  	bigPanel.add(connectPanel);
	  	this.newBoard();
	  	this.add(bigPanel);
	  	this.pack();
		this.setResizable(true);
		this.setLocationRelativeTo( null );
	  	this.setVisible(true);
	}
	/**
	 * We separate this from the constructor so we can easily instantiate the board
	 * 
	 *
	 */
	private void newBoard() {
		this.gameBoardPanel.removeAll();
	  	this.gameBoardPanel.setLayout( new GridLayout(8, 8) );
	  	this.gameBoardPanel.setPreferredSize(this.boardSize);
	  	this.gameBoardPanel.setBounds(0,0,this.boardSize.width,this.boardSize.height);
	  	for (int i = 0; i < GameInfo.SIZE*GameInfo.SIZE; i++) {
	  		int column = i % GameInfo.SIZE;
	  		int row = i / GameInfo.SIZE;
	  		if ((row % 2 == 0 && column % 2 == 0) || (row % 2 == 1 && column % 2 == 1))
	  			this.gameBoardPanel.add(new ImagePanel("./resources/Black_Empty.gif", row, column));
	  		else
	  			this.gameBoardPanel.add(new ImagePanel("./resources/Red_Empty.gif", row, column));
	  	}
	  	this.validate();
		this.repaint();
	}
	
	
	


	@Override
	public void mouseDragged(MouseEvent arg0) {
		// TODO Auto-generated method stub.
		
	}


	@Override
	public void mouseMoved(MouseEvent arg0) {
		// TODO Auto-generated method stub.
		
	}


	@Override
	public void mouseClicked(MouseEvent arg0) {
		// TODO Auto-generated method stub.
		
	}


	@Override
	public void mouseEntered(MouseEvent arg0) {
		// TODO Auto-generated method stub.
		
	}


	@Override
	public void mouseExited(MouseEvent arg0) {
		// TODO Auto-generated method stub.
		
	}
	/**
	 * 
	 * Set the GUI Piece used by outside methods only.
	 *
	 * @param row - Remember range 0 .. GameInfo.SIZE
	 * @param column Remember range 0 .. GameInfo.SIZE
	 * @param color based off of static fields in GameInfo
	 */
	public void setGUIPiece(int row, int column, int color) {
		ImagePanel panel = (ImagePanel)this.gameBoardPanel.getComponent(row*GameInfo.SIZE+column);
		if (color == GameInfo.IS_GREEN) {
			panel.add(new JLabel( new ImageIcon("./resources/Green.gif") ));
		} else if (color == GameInfo.IS_BLUE) {
			panel.add(new JLabel( new ImageIcon("./resources/Blue.gif") ));
		} else {
			System.out.println("Bad color provided");
		}
		this.validate();
		this.repaint();
	}
	/***
	 * This function will handle setting pieces on the board from the user.
	 * It will change when an AI component is added.
	 */
	@Override
	public void mousePressed(MouseEvent e) {
	  Component c =  this.gameBoardPanel.findComponentAt(e.getX(), e.getY());
	  if (c instanceof ImagePanel) {
		  System.out.println(e.getX() + "," + e.getY());
		  ImagePanel panel = ((ImagePanel)c);
		  //Alternate between setting the Green Piece versus the Blue Piece
		  int result = 0;
		  if (this.playerOneTurn) {
			  panel.add(new JLabel( new ImageIcon("./resources/Green.gif") ));
			  //result = this.engine.setBoardPiece(panel.row, panel.column, GameInfo.IS_GREEN);
		  } else {
			  panel.add(new JLabel( new ImageIcon("./resources/Blue.gif") ));
			  //result = this.engine.setBoardPiece(panel.row, panel.column, GameInfo.IS_BLUE);
		  }
		  if (result != GameInfo.IS_EMPTY) {
			  System.out.println("We have a winner! " + result);
		  }
		  this.playerOneTurn = !this.playerOneTurn;
		  this.validate();
		  this.repaint();
		  return;
	  } else {
		  System.out.println("Space already in use");
	  }
		
	}


	@Override
	public void mouseReleased(MouseEvent arg0) {
		// TODO Auto-generated method stub.
		
	}
	
	private class ImagePanel extends JPanel {
		private BufferedImage image;
		public int row = 0;
		public int column = 0;
		
	    public ImagePanel(String path, int row, int column) {
	       this.row = row;
	       this.column = column;
	    	try {                
	          this.image = ImageIO.read(new File(path));
	          this.setLayout(new BorderLayout());
	       } catch (IOException ex) {
	            ex.printStackTrace();
	            
	       }
	    }

	    @Override
	    public void paintComponent(Graphics g) {
	        g.drawImage(this.image, 0, 0, null); // see javadoc for more info on the parameters

	    }
	}

	/**
	 * Tied to the menu need to make this generic
	 */
	@Override
	public void actionPerformed(ActionEvent e) {
		this.newBoard();	
	}
}
