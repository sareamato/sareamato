import java.io.*;
import java.net.*;
import java.security.*;

public class ProtectedServer
{
	public boolean authenticate(InputStream inStream) throws IOException, NoSuchAlgorithmException 
	{
		DataInputStream in = new DataInputStream(inStream);
		

		// IMPLEMENT THIS FUNCTION.
		boolean success = true;
		String user = in.readUTF();
		String password = lookupPassword(user);
		
		long time_a = in.readLong();
		double random_a = in.readDouble();
		long time_b = in.readLong();
		double random_b = in.readDouble();
		
		

		int length = in.readInt();
		byte[] received = new byte [length];
		
		in.readFully(received);
		
		
		
		byte[] res_a = Protection.makeDigest(user, password, time_a, random_a);
		byte[] res_b= Protection.makeDigest(res_a, time_b, random_b);
		
		success =  MessageDigest.isEqual(received, res_b);
		return success;
	
		//if (MessageDigest.isEqual(res_a, res_b))
			//return true;
		//else
			//return false;
		
	}

	protected String lookupPassword(String user) { return "abc123"; }

	public static void main(String[] args) throws Exception 
	{
		int port = 7999;
		ServerSocket s = new ServerSocket(port);
		Socket client = s.accept();

		ProtectedServer server = new ProtectedServer();

		if (server.authenticate(client.getInputStream()))
		  System.out.println("Client logged in.");
		else
		  System.out.println("Client failed to log in.");

		s.close();
	}
}