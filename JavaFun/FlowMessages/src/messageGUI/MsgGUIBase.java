package messageGUI;

import java.awt.*;

import javax.swing.*;


/**
 * This class is the base for all the GUI Panels that will link with the
 * Different Message structs
 *
 * @author halfpeaw.
 *         Created Jul 13, 2012.
 */
public abstract class MsgGUIBase extends JPanel {
	public MsgGUIBase() {
		this.setPreferredSize(new Dimension(300,620));
	}
	
	public MsgGUIBase(byte[] byteIn) {
		this.setPreferredSize(new Dimension(300,620));
	}
	/**
	 * 
	 * This method wille extract all the values in the fields of the GUI
	 * use the appropriate MessageStruct to build a message and then return 
	 * that byte array
	 *
	 * @return
	 */
	protected byte[] getMessageData() {
		return new byte[0];
	}
}
