package minecraft_interface;

import java.awt.Robot;
import java.awt.AWTException;
import java.awt.Toolkit;
import java.awt.datatransfer.StringSelection;
import java.awt.datatransfer.Clipboard;
import java.io.IOException;
import java.awt.event.KeyEvent;

public class AutoTyper{
	private Robot robot;
	private Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
	
	public AutoTyper() throws IOException, AWTException{
		System.out.println("Constructing...");
		robot = new Robot();
		robot.setAutoDelay(40);
		System.out.println("Construction Complete");
	}
	
	public void typeString(String string) throws IOException, AWTException{
		System.out.println("Typing Command: " + string);
		StringSelection stringSelection = new StringSelection(string);
		clipboard.setContents(stringSelection, stringSelection);
		
		robot.keyPress(KeyEvent.VK_SLASH);
		robot.keyRelease(KeyEvent.VK_SLASH);
		robot.keyPress(KeyEvent.VK_CONTROL);
		robot.keyPress(KeyEvent.VK_V);
		robot.keyRelease(KeyEvent.VK_V);
		robot.keyRelease(KeyEvent.VK_CONTROL);
		robot.keyPress(KeyEvent.VK_ENTER);
		robot.keyRelease(KeyEvent.VK_ENTER);
	}
	
	public void exit(){
		System.out.println("Shutting Down AutoTyper...");
		System.exit(0);
	}
}
		
	

