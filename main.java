package minesweeper;

import java.util.Random;
import java.util.ArrayList;

//Cell driver
public class main 
{
	
	public static boolean[][] createBombs()
	{
		boolean[][] b = new boolean[16][16];
		
		for(int i=0; i<16; i++)
		{
			for(int j=0; j<16; j++)
			{
				b[i][j] = false;
			}
		}
		
		ArrayList<Integer> a = new ArrayList<Integer>();
		int num = 0;
		OUTER_LOOP:
		while(num<40)
		{
			int rand = (int)(Math.random() * 256);
			
			for(int k = 0; k<a.size(); k++)
			{
				if(rand == a.get(k))
				continue OUTER_LOOP;
			}
			a.add(rand);
			num++;
		}
		
		for(int h = 0; h<a.size(); h++)
		{
			b[(int)((a.get(h))/16)][(int)((a.get(h))%16)] = true;
		}
		
		return b;
		
	}
	
	public static void printBombs()
	{
		boolean[][] bom = createBombs();
		for(int i=0; i<16; i++)
		{
			for(int j=0; j<16; j++)
			{
				if(bom[i][j] == true)
				{
					System.out.print(Boolean.toString(bom[i][j]) + "  ");
				}
				else
				{
					System.out.print(Boolean.toString(bom[i][j]) + " ");
				}
			}
			System.out.println();
		}
	}
	
	public static Cell[][] makeBoard()
	{
		Cell[][] board = new Cell[16][16];
		
		for(int i=0; i<16; i++)
		{
			for(int j=0; j<16; j++)
			{
				board[i][j] = new Cell();
			}
		}
		
		boolean[][] bombs = createBombs();
		
		for(int i=0; i<16; i++)
		{
			for(int j=0; j<16; j++)
			{
				if(bombs[i][j] == true)
				{
					board[i][j].setBomb(true);
				}
			}
		}
		
		for(int i=0; i<16; i++)
		{
			for(int j=0; j<16; j++)
			{
				if(bombs[i][j] == true)
				{
					if(i == 0 && j == 0)
					{
						board[i+1][j].setVal(board[i+1][j].getVal()+1);
						board[i+1][j+1].setVal(board[i+1][j+1].getVal()+1);
						board[i][j+1].setVal(board[i][j+1].getVal()+1);
					}
					else if(i == 0 && j == 15)
					{
						board[i+1][j].setVal(board[i+1][j].getVal()+1);
						board[i+1][j-1].setVal(board[i+1][j-1].getVal()+1);
						board[i][j-1].setVal(board[i][j-1].getVal()+1);
					}
					else if(i == 15 && j == 0)
					{
						board[i-1][j].setVal(board[i-1][j].getVal()+1);
						board[i-1][j+1].setVal(board[i-1][j+1].getVal()+1);
						board[i][j+1].setVal(board[i][j+1].getVal()+1);
					}
					else if(i == 15 && j == 15)
					{
						board[i-1][j].setVal(board[i-1][j].getVal()+1);
						board[i-1][j-1].setVal(board[i-1][j-1].getVal()+1);
						board[i][j-1].setVal(board[i][j-1].getVal()+1);
					}
					else if(i == 0)
					{
						
					}
					else if(i == 15)
					{
						
					}
					else if(j == 0)
					{
						
					}
					else if(j == 15)
					{
						
					}
					else
					{
						
					}
				}
			}
		}
		
		return board;
	}
	
	public static void  displayBoard(Cell[][] b)
	{
		for(int i=0; i<16; i++)
		{
			for(int j=0; j<16; j++)
			{
				System.out.print(b[i][j].getSymbol());
			}
			System.out.println();
		}
	}
	
	public static void main(String[] args) 
	{
		
		printBombs();
		displayBoard(makeBoard());

	}

}
