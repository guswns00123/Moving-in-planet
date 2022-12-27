public class Trap {
	private int row;
	private int col;
	private Cell occupying;
	private String name;

	public Trap(int row, int col) {
		this.row = row;
		this.col = col;
		this.occupying = null;
		this.name = "Trap";
	}

	public void setOccupying(Cell cell) {
		this.occupying = cell;
	}

	public boolean interactWith(Object comer) {
		this.occupying.removeOccupant();
		if (comer instanceof Goblin) {
			System.out.printf("\033[1;31;43mA goblin entered a trap at (%d, %d)and died.\033[0;0m%n", this.row, this.col);
			((Goblin)comer).setActive(false);
			return false;
		} else if (comer instanceof Player) {
			System.out.printf("\033[1;31;43mYou entered a trap at (%d, %d)! HP - 1.\033[0;0m%n", this.row, this.col);
			((Player)comer).setHp(((Player)comer).getHp() - 1);
			((Player)comer).setOxygen(((Player)comer).getOxygen() - 1);
			return true;
		} else {
			return false;
		}
	}

	public String display() {
		return "\033[2;97m ";
	}
	
	public Cell getOccupying() {
		return this.occupying;
	}
	
	public String getName() {
		return this.name;
	}
}