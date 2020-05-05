/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.util.Iterator;
import java.util.Set;

/**
 *
 * @author thor
 */
public class DogKennelController {
	int choice =0;

	public void runProgram() {
		UI ui = new UI();
		Dog dog = new Dog();
		//HashMap<String,String> dogParams = new HashMap<>();
		RegisterDogUI regDog =  new RegisterDogUI(ui, dog);
		//RegisterDogUI regDog =  new RegisterDogUI(ui, dogParams);
		regDog.getDogParams();
		// TODO: brug dog-klassens set-metoder til at lave det færdige hundeobjekt
		// Som parameter til setterne bruges hashmappets nøgler
		System.out.println(dog);

	}
	
}
