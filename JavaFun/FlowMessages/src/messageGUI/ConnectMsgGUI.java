package messageGUI;

import javax.swing.*;

import messageObjects.ConnectMsg;

import java.awt.Dimension;
import java.awt.GridBagLayout;
import java.awt.GridBagConstraints;
import java.awt.Insets;
import java.awt.Font;

/**
 * TODO Put here a description of what this class does.
 *
 * @author halfpeaw.
 *         Created Jul 14, 2012.
 */
public class ConnectMsgGUI extends MsgGUIBase {
	ConnectMsg connect = new ConnectMsg();
	private JTextField nameTextField;
	private JTextField portTextField;
	private JTextField ipTextField;
	public ConnectMsgGUI() {
		//this.setPreferredSize(new Dimension(300,620));
		GridBagLayout gridBagLayout = new GridBagLayout();
		setLayout(gridBagLayout);
		JLabel label = new JLabel(connect.toString());
		label.setFont(new Font("Tahoma", Font.BOLD, 14));
		GridBagConstraints gbc_label = new GridBagConstraints();
		gbc_label.gridwidth = 3;
		gbc_label.insets = new Insets(0, 0, 5, 0);
		gbc_label.gridx = 0;
		gbc_label.gridy = 1;
		this.add(label, gbc_label);
		
		JLabel lblIpAddress = new JLabel("IP Address");
		GridBagConstraints gbc_lblIpAddress = new GridBagConstraints();
		gbc_lblIpAddress.insets = new Insets(0, 0, 5, 5);
		gbc_lblIpAddress.gridx = 0;
		gbc_lblIpAddress.gridy = 2;
		add(lblIpAddress, gbc_lblIpAddress);
		
		ipTextField = new JTextField();
		GridBagConstraints gbc_ipTextField = new GridBagConstraints();
		gbc_ipTextField.fill = GridBagConstraints.HORIZONTAL;
		gbc_ipTextField.gridwidth = 2;
		gbc_ipTextField.anchor = GridBagConstraints.NORTH;
		gbc_ipTextField.insets = new Insets(0, 0, 5, 0);
		gbc_ipTextField.gridx = 1;
		gbc_ipTextField.gridy = 2;
		add(ipTextField, gbc_ipTextField);
		ipTextField.setColumns(10);
		
		JLabel lblPort = new JLabel("Port");
		GridBagConstraints gbc_lblPort = new GridBagConstraints();
		gbc_lblPort.insets = new Insets(0, 0, 5, 5);
		gbc_lblPort.gridx = 0;
		gbc_lblPort.gridy = 3;
		add(lblPort, gbc_lblPort);
		
		portTextField = new JTextField();
		GridBagConstraints gbc_portTextField = new GridBagConstraints();
		gbc_portTextField.fill = GridBagConstraints.HORIZONTAL;
		gbc_portTextField.gridwidth = 2;
		gbc_portTextField.anchor = GridBagConstraints.NORTH;
		gbc_portTextField.insets = new Insets(0, 0, 5, 0);
		gbc_portTextField.gridx = 1;
		gbc_portTextField.gridy = 3;
		add(portTextField, gbc_portTextField);
		portTextField.setColumns(10);
		
		JLabel lblName = new JLabel("Name");
		GridBagConstraints gbc_lblName = new GridBagConstraints();
		gbc_lblName.fill = GridBagConstraints.VERTICAL;
		gbc_lblName.insets = new Insets(0, 0, 0, 5);
		gbc_lblName.gridx = 0;
		gbc_lblName.gridy = 4;
		add(lblName, gbc_lblName);
		
		nameTextField = new JTextField();
		GridBagConstraints gbc_nameTextField = new GridBagConstraints();
		gbc_nameTextField.gridwidth = 2;
		gbc_nameTextField.fill = GridBagConstraints.HORIZONTAL;
		gbc_nameTextField.insets = new Insets(0, 0, 0, 5);
		gbc_nameTextField.gridx = 1;
		gbc_nameTextField.gridy = 4;
		add(nameTextField, gbc_nameTextField);
		nameTextField.setColumns(10);
	}
	protected byte[] getMessageData() {
		connect.setName(this.nameTextField.getText());
		connect.setHostName(this.ipTextField.getText());
		try {
			connect.setPort(Integer.parseInt(this.portTextField.getText()));
		} catch (NumberFormatException e) {
			e.printStackTrace();
			return new byte[0];
		}
		return this.connect.getBytes();
	}
	
}
