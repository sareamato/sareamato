import java.io.*;
import java.net.*;
import java.security.*;
import javax.crypto.*;

/**
 *
 * @author saraamato
 */
public class Serverx509 {
    public static void main(String[] args) throws Exception 
	{   
                //I used the following sources for Server and Client x509
		//https://docs.oracle.com/javase/8/docs/api/javax/security/cert/X509Certificate.html
                //https://docs.oracle.com/javase/7/docs/technotes/guides/security/certpath/CertPathProgGuide.html
		// https://stackoverflow.com/questions/11383898/how-to-create-a-x509-certificate-using-java
                String alias="Sara";
                String password="Samato";
		
             
                int port = 7999;
		ServerSocket s = new ServerSocket(port);
		Socket client = s.accept();
		ObjectInputStream input = new ObjectInputStream(client.getInputStream());
	    
		// instantiate a KeyStore with type JKS
                KeyStore ks = KeyStore.getInstance("JKS");
                // load the contents of the KeyStore
                ks.load(new FileInputStream(".keystore"), password.toCharArray());
                PrivateKey server = (PrivateKey)ks.getKey(alias, password.toCharArray());
       
        
                //Decrypt server final key
                Cipher c = Cipher.getInstance("RSA/ECB/PKCS1Padding");
                byte[] input_b = (byte[]) input.readObject();
		c.init(Cipher.DECRYPT_MODE, server);
		byte[] text = c.doFinal(input_b);
                String finaltext;
                finaltext = new String(text);
		System.out.println("Confidential Message: ");
                System.out.println(finaltext);
		s.close();
	}
    
}
