import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

/**
 *
 * @author saraamato
 */

public class MessageDig {
    public static void main(String[] args){
        try{
        
            Scanner myObj = new Scanner(System.in);  // Create a Scanner object
            System.out.println("Enter message to be hashed");

            String message = myObj.nextLine(); 

            MessageDigest mdMD5 = MessageDigest.getInstance("MD5");
            MessageDigest mdSHA = MessageDigest.getInstance("SHA");
            byte[] MD5Hash = mdMD5.digest(message.getBytes());
            byte[] SHAHash = mdSHA.digest(message.getBytes());
            StringBuilder md5 = new StringBuilder();
            StringBuilder sha = new StringBuilder();
            
            for(int i=0; i< MD5Hash.length ;i++)
            {
                md5.append(Integer.toString((MD5Hash[i] & 0xff) + 0x100, 16).substring(1));
            }
            
            for(int i=0; i< SHAHash.length ;i++)
            {
                sha.append(Integer.toString((SHAHash[i] & 0xff) + 0x100, 16).substring(1));
            }
            //Get complete hashed password in hex format
            String result_md5 = md5.toString();
            String result_sha = sha.toString();
            System.out.println("MD5: ");
            System.out.println(result_md5);
            System.out.println("SHA: ");
            System.out.println(result_sha);
        } 
        
        catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
            
        }
        
    
        

}
}