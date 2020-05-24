package minecraft_interface;

import py4j.GatewayServer;
import java.awt.AWTException;
import java.io.IOException;

public class AutoTyperEntryPoint{
	private AutoTyper autotyper;
	
	public AutoTyperEntryPoint() throws IOException, AWTException{
		autotyper = new AutoTyper();
	}
	
	public AutoTyper getAutoTyper(){
		return autotyper;
	}
	
	public static void main(String[] args) throws IOException, AWTException{
		System.out.println("Starting AutoTyper...");
        GatewayServer gatewayServer = new GatewayServer(new AutoTyperEntryPoint());
        gatewayServer.start();
		System.out.println("Gateway Established");
		System.out.println("AutoTyper is Ready");
    }
}
		
	

