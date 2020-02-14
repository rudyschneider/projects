package minesweeper;

//single minesweeper cell
public class Cell 
{

	public int row, col, val; //position and number
	public boolean bomb = false; //if 
	public String symbol = "U"; //Display symbol
	
	public Cell()
	{
	}
	
	//getters and setters
	public void setRow(int newrow)
	{
		row = newrow;
	}
	
	public int getRow()
	{
		return row;
	}
	
	public void setCol(int newcol)
	{
		row = newcol;
	}
	
	public int getCol()
	{
		return col;
	}
	
	public void setVal(int newval)
	{
		val = newval;
	}
	
	public int getVal()
	{
		return val;
	}
	
	public void setBomb(boolean x)
	{
		bomb = x;
	}
	
	public boolean getBomb()
	{
		return bomb;
	}
	
	public void setSymbol(String newsymbol)
	{
		symbol = newsymbol;
	}
	
	public String getSymbol()
	{
		return symbol;
	}

}


