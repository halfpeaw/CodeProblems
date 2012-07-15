package messageGUI;

import javax.swing.*;

import flowGUIClient.MainGUI;

import messageObjects.ConnectMsg;
import messageObjects.ConnectResp;
import messageObjects.Globals;
import messageObjects.MessageStruct;

import java.awt.GridBagConstraints;
import java.awt.Insets;
import java.awt.Font;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.GridBagLayout;

/**
 * TODO Put here a description of what this class does.
 *
 * @author halfpeaw.
 *         Created Jul 14, 2012.
 */
public class ConnectMsgGUI extends MsgGUIBase {
	private static final long serialVersionUID = Globals.CONNECT_TYPE;
	ConnectMsg connect = new ConnectMsg();
	private JTextField nameTextField;
	private JTextField portTextField;
	private JTextField ipTextField;
	private JTextField statusTextField;
	public ConnectMsgGUI(MainGUI mainGUI) {
		super(mainGUI);
		GridBagLayout gridBagLayout = (GridBagLayout) getLayout();
		gridBagLayout.columnWeights = new double[]{0.0, 1.0};

		JLabel label = new JLabel(connect.toString());
		label.setFont(new Font("Tahoma", Font.BOLD, 14));
		GridBagConstraints gbc_label = new GridBagConstraints();
		gbc_label.gridwidth = 2;
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
		ipTextField.setText("localhost");
		GridBagConstraints gbc_ipTextField = new GridBagConstraints();
		gbc_ipTextField.fill = GridBagConstraints.HORIZONTAL;
		gbc_ipTextField.anchor = GridBagConstraints.NORTH;
		gbc_ipTextField.insets = new Insets(0, 0, 5, 80);
		gbc_ipTextField.gridx = 1;
		gbc_ipTextField.gridy = 2;
		add(ipTextField, gbc_ipTextField);
		ipTextField.setColumns(10);
		
		JLabel lblPort = new JLabel("Port");
		GridBagConstraints gbc_lblPort = new GridBagConstraints();
		gbc_lblPort.anchor = GridBagConstraints.EAST;
		gbc_lblPort.insets = new Insets(0, 0, 5, 5);
		gbc_lblPort.gridx = 0;
		gbc_lblPort.gridy = 3;
		add(lblPort, gbc_lblPort);
		
		portTextField = new JTextField();
		portTextField.setText("1231");
		GridBagConstraints gbc_portTextField = new GridBagConstraints();
		gbc_portTextField.fill = GridBagConstraints.HORIZONTAL;
		gbc_portTextField.anchor = GridBagConstraints.NORTH;
		gbc_portTextField.insets = new Insets(0, 0, 5, 80);
		gbc_portTextField.gridx = 1;
		gbc_portTextField.gridy = 3;
		add(portTextField, gbc_portTextField);
		portTextField.setColumns(10);
		
		JLabel lblName = new JLabel("Name");
		GridBagConstraints gbc_lblName = new GridBagConstraints();
		gbc_lblName.anchor = GridBagConstraints.EAST;
		gbc_lblName.fill = GridBagConstraints.VERTICAL;
		gbc_lblName.insets = new Insets(0, 0, 5, 5);
		gbc_lblName.gridx = 0;
		gbc_lblName.gridy = 4;
		add(lblName, gbc_lblName);
		
		nameTextField = new JTextField();
		nameTextField.setText("halfpeaw");
		GridBagConstraints gbc_nameTextField = new GridBagConstraints();
		gbc_nameTextField.insets = new Insets(0, 0, 5, 80);
		gbc_nameTextField.fill = GridBagConstraints.HORIZONTAL;
		gbc_nameTextField.gridx = 1;
		gbc_nameTextField.gridy = 4;
		add(nameTextField, gbc_nameTextField);
		nameTextField.setColumns(10);
		
		JLabel lblStatus = new JLabel("Status: ");
		GridBagConstraints gbc_lblStatus = new GridBagConstraints();
		gbc_lblStatus.insets = new Insets(0, 0, 5, 5);
		gbc_lblStatus.anchor = GridBagConstraints.EAST;
		gbc_lblStatus.gridx = 0;
		gbc_lblStatus.gridy = 5;
		add(lblStatus, gbc_lblStatus);
		
		statusTextField = new JTextField();
		statusTextField.setEditable(false);
		GridBagConstraints gbc_statusTextField = new GridBagConstraints();
		gbc_statusTextField.insets = new Insets(0, 0, 5, 80);
		gbc_statusTextField.fill = GridBagConstraints.HORIZONTAL;
		gbc_statusTextField.gridx = 1;
		gbc_statusTextField.gridy = 5;
		add(statusTextField, gbc_statusTextField);
		statusTextField.setColumns(10);
		
		JButton btnSend = new JButton("Send");
		btnSend.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				sendConnectMSG();
			}
		});
		GridBagConstraints gbc_btnSend = new GridBagConstraints();
		gbc_btnSend.anchor = GridBagConstraints.EAST;
		gbc_btnSend.insets = new Insets(0, 0, 0, 5);
		gbc_btnSend.gridx = 1;
		gbc_btnSend.gridy = 6;
		add(btnSend, gbc_btnSend);
	}
	private void sendConnectMSG() {
		connect.setName(this.nameTextField.getText());
		connect.setHostName(this.ipTextField.getText());
		try {
			connect.setPort(Integer.parseInt(this.portTextField.getText()));
		} catch (NumberFormatException e) {
			e.printStackTrace();
		}
		mainGUI.clientSocket.sendConnect(connect);
	}
	/**
	 * Receives the connection response and populates the GUI with the received user id
	 */
	public void receiveResponse(MessageStruct response) {
		if (response.getMsgType() == Globals.CONNECT_RESP) {
			statusTextField.setText(""+(response.getStatus()));
			this.mainGUI.gameInfo.userId = response.getStatus();
		} else {
			System.out.println("Something went wrong...");
		}
		
	}
}
