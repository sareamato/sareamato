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
public class Sender {
    public static void main(String[] args) throws Exception 
	{
		///from cipher client
                 String message = "The quick brown fox jumps over the lazy dog.";
		String host = "127.0.0.1";
		int port = 7999;
		Socket s = new Socket(host, port);
                ///get user input for type of key
                ///If 1: receiver public, if 2: sender private
                 System.out.println("Select how you want the message sent");
                 System.out.println("1: Confidential");
                //2 is also confidential
                 System.out.println("2: Integrity & Authentication");
                 Scanner type = new Scanner(System.in);
                
                //Also send to receiver
                 int type_selected = type.nextInt();
		type.close();
		ObjectOutputStream obj = new ObjectOutputStream(s.getOutputStream());
		obj.writeInt(type_selected);
                
                
                ///https://docs.oracle.com/javase/tutorial/security/apisign/step2.html
                ///generate the RSA public key
                 int m = 1024;
                 SecureRandom random1 = new SecureRandom();
		KeyPairGenerator keyGenerator = KeyPairGenerator.getInstance("RSA");
		keyGenerator.initialize(m, random1);
		KeyPair keys = keyGenerator.generateKeyPair();
		RSAPublicKey s_public_key = (RSAPublicKey) keys.getPublic();
                //Also private
		RSAPrivateKey s_private_key  = (RSAPrivateKey) keys.getPrivate();
                
                // -Store it in a file - from cipher.
		
		File KeyFile = new File("Sender_Key.txt");
		ObjectOutputStream output = new ObjectOutputStream(new FileOutputStream(KeyFile));
		output.writeObject(s_public_key);
                ///get receiver public key
		ObjectInputStream input = new ObjectInputStream(new FileInputStream("Receiver_Key.txt"));
		RSAPublicKey r_public_key = (RSAPublicKey)input.readObject();
                
                //encryption - same except with RSA
                Cipher c = Cipher.getInstance("RSA/ECB/PKCS1Padding");
                 
                //Confidential, use receivers public key - doesn't prove sender identity
                if (type_selected == 1){
                    c.init(Cipher.ENCRYPT_MODE, r_public_key);
                    byte[] text = c.doFinal(message.getBytes());
                    obj.writeObject(text);
                }
                // CIA
                if (type_selected == 2){
                    c.init(Cipher.ENCRYPT_MODE, s_private_key);
                    byte[] text = c.doFinal(message.getBytes());
                    obj.writeObject(text);
                }
		obj.flush();
		obj.close();
		s.close();
		System.exit(0);
        }
}
