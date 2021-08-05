import java.io.*;
import java.net.*;
import java.security.*;
import javax.crypto.*;

public class CipherClient
{
	public static void main(String[] args) throws Exception 
	{
		String message = "The quick brown fox jumps over the lazy dog.";
		String host = "127.0.0.1";
		int port = 7999;
		Socket s = new Socket(host, port);

		// YOU NEED TO DO THESE STEPS:
		// -Generate a DES key.
		//https://docs.oracle.com/javase/7/docs/api/javax/crypto/KeyGenerator.html
		KeyGenerator key_client = KeyGenerator.getInstance("DES");
		SecureRandom random = new SecureRandom();
		key_client.init(random);
		Key key_final = key_client.generateKey();


		// -Store it in a file.
		File KeyFile = new File("Client_Key.txt");
		ObjectOutputStream obj = new ObjectOutputStream(new FileOutputStream(KeyFile));
		obj.writeObject(key_final);
		ObjectOutputStream output = new ObjectOutputStream(s.getOutputStream());
		output.writeObject(key_final);


		output.flush();
	
		// -Use the key to encrypt the message above and send it over socket s to the server.	
		//same as server
		Cipher c = Cipher.getInstance("DES/ECB/PKCS5Padding");
	    	CipherOutputStream Output_c = new CipherOutputStream(s.getOutputStream(), c);
		c.init(Cipher.ENCRYPT_MODE, key_final);

		byte encrypted[] = message.getBytes();
		//If you want to see the encrypted message, uncomment the next line
		System.out.println(encrypted);
		Output_c.write(encrypted);
	    	Output_c.close();
		s.close();
	   	obj.close();
	}
}