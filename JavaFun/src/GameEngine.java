
/**
 * TODO This class controls the internal functions of the game
 * GUI is independent of this class.  Used by the AI.
 *
 * @author halfpeaw.
 *         Created Jul 11, 2012.
 */
public class GameEngine {
	final static int IS_GREEN = 1;
	final static int IS_BLUE = 2;
	final static int IS_EMPTY = 0;
	final static int SIZE = 8;
	final static int WINLEN = 5;
	private int[][] gameBoard = new int [SIZE][SIZE];	
	
	public GameEngine() {
		
	}
	/**
	 * Set the piece and then check if there is a winner.
	 *
	 * @param row
	 * @param column
	 * @param color
	 * @return
	 */
	public int setBoardPiece(int row, int column, int color) {
		if (color != IS_GREEN && color != IS_BLUE) {
			return IS_EMPTY;
		}
		this.gameBoard[row][column] = color;
		return isGameOver();
	}
	public void clearBoard() {
		this.gameBoard = new int [SIZE][SIZE];
	}
	/**
	 * Analyzes the GameBoard to determine if its in a winning state.  
	 *
	 * @return static value of the winner
	 */
	public int isGameOver() {
		
		for (int row = 0; row < SIZE; row++ ) {
			for (int column = 0; column < SIZE; column++) {
				int lookFor = this.gameBoard[row][column];
				if (lookFor != IS_EMPTY) {
					//Need to check up down and diagonal in all directions
					boolean match = false;
					//Look Right
					if (column <= SIZE-WINLEN) {
						match = true;
						for (int i = 0; i < WINLEN; i++) {
							if (this.gameBoard[row][column+i]!=lookFor) {
								match = false;
								break;
							}
						}
						if (match) return lookFor;						
					}
					//Look Down
					if (row <= SIZE-WINLEN) {
						match = true;
						for (int i = 0; i < WINLEN; i++) {
							if (this.gameBoard[row+i][column]!=lookFor) {
								match = false;
								break;
							}
						}
						if (match) return lookFor;						
					}
					//Look Down Right Diagonal
					if (row <= SIZE-WINLEN && column <= SIZE-WINLEN){
						match = true;
						for (int i = 0; i < WINLEN; i++) {
							if (this.gameBoard[row+i][column+i]!=lookFor) {
								match = false;
								break;
							}
						}
						if (match) return lookFor;						
					}
					//Look Down Left diagonal
					if (row <= SIZE-WINLEN && column >= WINLEN-1){
						match = true;
						for (int i = 0; i < WINLEN; i++) {
							if (this.gameBoard[row+i][column-i]!=lookFor) {
								match = false;
								break;
							}
						}
						if (match) return lookFor;						
					}
				}//If NOT_EMPTY
			} // Column
		} // Row 
		return IS_EMPTY;
	}
}
