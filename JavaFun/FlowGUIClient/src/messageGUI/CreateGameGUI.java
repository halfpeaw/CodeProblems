/**
 * 
 */
package messageGUI;

import java.awt.*;

import javax.swing.*;

import messageObjects.GetPlayersMsg;
import messageObjects.GetPlayersResp;
import messageObjects.Globals;
import messageObjects.MessageStruct;

import flowGUIClient.MainGUI;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.ItemListener;
import java.awt.event.ItemEvent;

/**
 * @author halfpeaw
 *
 */
public class CreateGameGUI extends MsgGUIBase {

	private static final long serialVersionUID = 3L;
	private JTextField textField;
	private JTextField txtTestGame;
	private JTextField gameStatusTextField;
	private String[] playerNames;
	DefaultListModel model = new DefaultListModel();
	public JList playerlist;

	/**
	 * @param mainGUI
	 */
	public CreateGameGUI(final MainGUI mainGUI) {
		super(mainGUI);
		GridBagLayout gridBagLayout = (GridBagLayout) getLayout();
		gridBagLayout.rowWeights = new double[]{0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0};
		gridBagLayout.columnWeights = new double[]{0.0, 1.0};
		JLabel label = new JLabel("Create Game");
		label.setFont(new Font("Tahoma", Font.BOLD, 14));
		GridBagConstraints gbc_label = new GridBagConstraints();
		gbc_label.gridwidth = 2;
		gbc_label.insets = new Insets(0, 0, 5, 0);
		gbc_label.gridx = 0;
		gbc_label.gridy = 1;
		this.add(label, gbc_label);
		
		JLabel lblGameName = new JLabel("Game Name:");
		GridBagConstraints gbc_lblGameName = new GridBagConstraints();
		gbc_lblGameName.anchor = GridBagConstraints.EAST;
		gbc_lblGameName.insets = new Insets(0, 0, 5, 5);
		gbc_lblGameName.gridx = 0;
		gbc_lblGameName.gridy = 2;
		add(lblGameName, gbc_lblGameName);
		
		txtTestGame = new JTextField();
		txtTestGame.setText("Test Game");
		GridBagConstraints gbc_txtTestGame = new GridBagConstraints();
		gbc_txtTestGame.fill = GridBagConstraints.HORIZONTAL;
		gbc_txtTestGame.insets = new Insets(0, 0, 5, 0);
		gbc_txtTestGame.gridx = 1;
		gbc_txtTestGame.gridy = 2;
		add(txtTestGame, gbc_txtTestGame);
		txtTestGame.setColumns(10);
		
		JLabel lblNewLabel = new JLabel("#Players: ");
		GridBagConstraints gbc_lblNewLabel = new GridBagConstraints();
		gbc_lblNewLabel.anchor = GridBagConstraints.EAST;
		gbc_lblNewLabel.insets = new Insets(0, 0, 5, 5);
		gbc_lblNewLabel.gridx = 0;
		gbc_lblNewLabel.gridy = 3;
		add(lblNewLabel, gbc_lblNewLabel);
		
		textField = new JTextField();
		textField.setEditable(false);
		textField.setText("2");
		GridBagConstraints gbc_textField = new GridBagConstraints();
		gbc_textField.fill = GridBagConstraints.HORIZONTAL;
		gbc_textField.insets = new Insets(0, 0, 5, 0);
		gbc_textField.gridx = 1;
		gbc_textField.gridy = 3;
		add(textField, gbc_textField);
		textField.setColumns(10);
		
		JLabel lblSelectPlayers = new JLabel("Select Players");
		GridBagConstraints gbc_lblSelectPlayers = new GridBagConstraints();
		gbc_lblSelectPlayers.insets = new Insets(0, 0, 5, 0);
		gbc_lblSelectPlayers.gridx = 1;
		gbc_lblSelectPlayers.gridy = 4;
		add(lblSelectPlayers, gbc_lblSelectPlayers);
		
		String [] options = {"Human","AI"};
		JComboBox comboBox = new JComboBox(options);

		comboBox.addItemListener(new ItemListener() {
			public void itemStateChanged(ItemEvent arg0) {
				GetPlayersMsg msg = new GetPlayersMsg();
				msg.setType(Globals.IS_HUMAN);
				mainGUI.clientSocket.sendMessage(msg);
			}
		});
		GridBagConstraints gbc_comboBox = new GridBagConstraints();
		gbc_comboBox.anchor = GridBagConstraints.NORTH;
		gbc_comboBox.insets = new Insets(0, 0, 5, 0);
		gbc_comboBox.gridx = 1;
		gbc_comboBox.gridy = 5;
		add(comboBox, gbc_comboBox);
		
		playerlist = new JList(model);
		GridBagConstraints gbc_list = new GridBagConstraints();
		gbc_list.insets = new Insets(0, 0, 5, 0);
		gbc_list.fill = GridBagConstraints.BOTH;
		gbc_list.gridx = 1;
		gbc_list.gridy = 6;
		add(playerlist, gbc_list);
		
		JButton btnCreateGame = new JButton("Create Game");
		btnCreateGame.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
			}
		});
		GridBagConstraints gbc_btnCreateGame = new GridBagConstraints();
		gbc_btnCreateGame.insets = new Insets(0, 0, 5, 0);
		gbc_btnCreateGame.gridx = 1;
		gbc_btnCreateGame.gridy = 7;
		add(btnCreateGame, gbc_btnCreateGame);
		
		JLabel lblStatus = new JLabel("Status:");
		GridBagConstraints gbc_lblStatus = new GridBagConstraints();
		gbc_lblStatus.anchor = GridBagConstraints.EAST;
		gbc_lblStatus.insets = new Insets(0, 0, 10, 5);
		gbc_lblStatus.gridx = 0;
		gbc_lblStatus.gridy = 8;
		add(lblStatus, gbc_lblStatus);
		
		gameStatusTextField = new JTextField();
		gameStatusTextField.setEditable(false);
		GridBagConstraints gbc_gameStatusTextField = new GridBagConstraints();
		gbc_gameStatusTextField.insets = new Insets(0, 0, 10, 0);
		gbc_gameStatusTextField.fill = GridBagConstraints.HORIZONTAL;
		gbc_gameStatusTextField.gridx = 1;
		gbc_gameStatusTextField.gridy = 8;
		add(gameStatusTextField, gbc_gameStatusTextField);
		gameStatusTextField.setColumns(10);
		
		//Populate the initial List
		
	}
	public void populateList() {
		if (mainGUI.clientSocket.isConected) {
			GetPlayersMsg msg = new GetPlayersMsg();
			msg.setType(Globals.IS_HUMAN);
			mainGUI.clientSocket.sendMessage(msg);
		} 
	}
	
	public void receiveResponse(MessageStruct response) {
		//Model is a reference variable for populating the JList Playerslist
		model.clear();
		if (response.getMsgType() == Globals.GET_PLAYERS_RESP) {
			this.playerNames = ((GetPlayersResp)response).getPlayerList();
			for (int i = 0; i < this.playerNames.length; i++) {
				model.addElement(this.playerNames[i]);
			}
			
			gameStatusTextField.setText("" +response.getStatus());
		} else {
			System.out.println("Something went wrong...");
			gameStatusTextField.setText("Unexpected Message: " + response.toString());
		}
		
	}


}

