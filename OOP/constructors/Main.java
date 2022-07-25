public class Main{
	int x; // setting atribute

	// Creating the constuctor
	public Main(){
		x = 5; // setting the initial varible 
	}
	public static void main(String[] args){
		Main myObject = new Main(); // create an instance of Main 
																// causing the contructor to run
																//
		// print out the value of x
		System.out.println(myObject.x);
		
	}
}
