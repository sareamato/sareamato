import javax.crypto.Cipher;
import java.io.*;
import java.net.*;
import java.security.*;
import java.util.Scanner;
import java.security.interfaces.RSAPrivateKey;
import java.security.interfaces.RSAPublicKey;


/**
 *
 * @author saraamato
 */

public class Receiver {
    
    public static void main(String[] args) throws Exception 
	{
		
		///https://docs.oracle.com/javase/tutorial/security/apisign/step2.html
                ///generate the receiver RSA public key
                 int m = 1024;
                 SecureRandom random2 = new SecureRandom();
		KeyPairGenerator keyGenerator = KeyPairGenerator.getInstance("RSA");
		keyGenerator.initialize(m, random2);
		KeyPair keys = keyGenerator.generateKeyPair();
		RSAPublicKey r_public_key = (RSAPublicKey) keys.getPublic();

                //Also private
		RSAPrivateKey r_private_key  = (RSAPrivateKey) keys.getPrivate();
                
                // -Store it in a file - from cipher.
		File KeyFile = new File("Receiver_Key.txt");
		ObjectOutputStream output = new ObjectOutputStream(new FileOutputStream(KeyFile));
		output.writeObject(r_public_key);

		///from cipher server 
		int port = 7999;
		ServerSocket server = new ServerSocket(port);
		Socket s = server.accept();


                ///get type of key from sender
                 ObjectInputStream obj2 = new ObjectInputStream(s.getInputStream());
		int type_selected = obj2.readInt();
                
                
                ///get sender public key
		ObjectInputStream obj3 = new ObjectInputStream(new FileInputStream("Sender_Key.txt"));
		RSAPublicKey s_public_key = (RSAPublicKey)obj3.readObject();
		obj3.close();
                
                //encryption - same except with RSA
                Cipher c = Cipher.getInstance("RSA/ECB/PKCS1Padding");
                 
                //decrypt using private key
                if (type_selected == 1){
                        byte[] text = (byte[]) obj2.readObject();
		  	c.init(Cipher.DECRYPT_MODE, r_private_key);
			byte[] textbytes = c.doFinal(text);
			String finaltext = new String(textbytes);
			System.out.println("Message received: " + finaltext);
                }
                // CIA, we know that it comes from receiver because it uses her private key
                if (type_selected == 2){
                        byte[] text = (byte[]) obj2.readObject();
                        c.init(Cipher.DECRYPT_MODE, s_public_key);
                         byte[] textbytes = c.doFinal(text);
			String finaltext = new String(textbytes);
			System.out.println("Message received: " + finaltext);
                }
                 obj2.close();
		System.exit(0);
                
        }
}

    

