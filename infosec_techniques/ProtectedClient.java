import java.io.*;
import java.net.*;
import java.security.*;
import java.util.Date;

public class ProtectedClient
{
	public void sendAuthentication(String user, String password, OutputStream outStream) throws IOException, NoSuchAlgorithmException 
	{
		DataOutputStream out = new DataOutputStream(outStream);

		// IMPLEMENT THIS FUNCTION.

		Date date = new Date();
		long time1 = date.getTime();
		long time2 = date.getTime();
		
		double random1 = Math.random();
		double random2 = Math.random();
		
		
		byte[] res1 = Protection.makeDigest(user, password, time1, random1);
		byte[] res2 = Protection.makeDigest(res1, time2, random2);
		
		out.writeUTF(user); 

		out.writeLong(time1);
		out.writeDouble(random1);

		out.writeLong(time2);
		out.writeDouble(random2);

		out.writeInt(res1.length); 
		out.write(res2);
		

		out.flush();
	}

	public static void main(String[] args) throws Exception 
	{
		String host = "127.0.0.1";
		//local
		int port = 7999;
		String user = "George";
		String password = "abc123";
		Socket s = new Socket(host, port);

		ProtectedClient client = new ProtectedClient();
		client.sendAuthentication(user, password, s.getOutputStream());

		s.close();
	}
}