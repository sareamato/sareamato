import java.io.*;
import java.net.*;
import java.util.Date;
import java.security.cert.CertificateFactory;
import java.security.cert.X509Certificate;
import java.security.interfaces.RSAPublicKey;
import javax.crypto.*;

/**
 *
 * @author saraamato
 */
public class Clientx509 {
    public static void main(String[] args) throws Exception 
	{
            ///I used the same sources as I listed in Serverx509
		String host = "127.0.0.1";
		int port = 7999;
		Socket s = new Socket(host, port);
     
		ObjectOutputStream output = new ObjectOutputStream(s.getOutputStream());
                InputStream is = new FileInputStream("Sara.cert");
                // https://docs.oracle.com/javase/7/docs/technotes/guides/security/certpath/CertPathProgGuide.html
                CertificateFactory cf = CertificateFactory.getInstance("X.509");
                X509Certificate cert = (X509Certificate)cf.generateCertificate(is);
                is.close();

                String cfr = cert.toString();
                // string containing cert
                System.out.println("Content of the certificate received:");
                System.out.println(cfr);
             //Checking the date
                Date date = cert.getNotAfter();
                if(date.after(new Date())){
                    System.out.println("Current certificate");}
                else{     
                    System.out.println("Expired Certificate");}
                //I got the following check validity information from this source
                // https://www.programcreek.com/java-api-examples/?class=java.security.cert.X509Certificate&method=checkValidity
                try{
                   cert.checkValidity();
                   System.out.println("The certificate is valid.");}  
                catch (Exception e){
                   System.out.println(e);}

                //Now prooceed to exchange confidential messages

                String conf_message = "The quick brown fox jumps over the lazy dog.";
                RSAPublicKey server = (RSAPublicKey) cert.getPublicKey();
                        Cipher c = Cipher.getInstance("RSA/ECB/PKCS1Padding");
                        c.init(Cipher.ENCRYPT_MODE, server);
                        byte[] text = c.doFinal(conf_message.getBytes());
                        output.writeObject(text);
                        output.flush();
                        output.close();
                        s.close();
                        is.close();
                }



}
    
