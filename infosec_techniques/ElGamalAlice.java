import java.io.*;
import java.net.*;
import java.security.*;
import java.math.BigInteger;

public class ElGamalAlice
{
	private static BigInteger computeY(BigInteger p, BigInteger g, BigInteger d)
	{
		// IMPLEMENT THIS FUNCTION;
		//  modPow(BigInteger exponent, BigInteger m)
		//  d is exponent, p is modulus
		return g.modPow(d, p);
	}

	private static BigInteger computeK(BigInteger p)
	{
		// IMPLEMENT THIS FUNCTION;
		int bits = 1024; //key bit length
		//the '16' determines the probability that p is prime, same as skeleton part
		BigInteger k = new BigInteger(bits, 16, new SecureRandom());

		// if relatively prime, gcd is the greatest common divisor
		// I found this method in BigInteger tutorial 
		// "The java.math.BigInteger.gcd(BigInteger val) returns a BigInteger whose
		// value isthe greatest common divisor of abs(this) and abs(val). It returns 0 if this == 0 && val == 0."
		if (k.gcd(p.subtract(BigInteger.ONE)).equals(BigInteger.ONE) == true)
			return k;
		else
		{
			// if not relatively prime, just run computeK again until k is
			return computeK(p);
		}
	}
	
	private static BigInteger computeA(BigInteger p, BigInteger g, BigInteger k)
	{
		// IMPLEMENT THIS FUNCTION;
		//d is exponent, p is modulus
		return g.modPow(k, p);
	}

	private static BigInteger computeB(	String message, BigInteger d, BigInteger a, BigInteger k, BigInteger p)
	{
		/// IMPLEMENT THIS FUNCTION;
		BigInteger h = k.modInverse(p.subtract(BigInteger.ONE));
		BigInteger p2 = p.subtract(BigInteger.ONE);
		//I need to convert the string to BigInt;
		BigInteger message_b = new BigInteger(message.getBytes());
		//return ( (new BigInteger message_b.subtract(d.multiply(a))).multiply(h).mod(p2));
		BigInteger b = message_b.subtract(d.multiply(a)).multiply(h).mod(p2);
		return b;
	}

	public static void main(String[] args) throws Exception 
	{
		String message = "The quick brown fox jumps over the lazy dog.";

		String host = "127.0.0.1";
		int port = 7999;
		Socket s = new Socket(host, port);
		ObjectOutputStream os = new ObjectOutputStream(s.getOutputStream());

		// You should consult BigInteger class in Java API documentation to find out what it is.
		BigInteger y, g, p; // public key
		BigInteger d; // private key

		int mStrength = 1024; // key bit length
		SecureRandom mSecureRandom = new SecureRandom(); // a cryptographically strong pseudo-random number

		// Create a BigInterger with mStrength bit length that is highly likely to be prime.
		// (The '16' determines the probability that p is prime. Refer to BigInteger documentation.)
		p = new BigInteger(mStrength, 16, mSecureRandom);
		
		// Create a randomly generated BigInteger of length mStrength-1
		g = new BigInteger(mStrength-1, mSecureRandom);
		d = new BigInteger(mStrength-1, mSecureRandom);

		y = computeY(p, g, d);

		// At this point, you have both the public key and the private key. Now compute the signature.

		BigInteger k = computeK(p);
		BigInteger a = computeA(p, g, k);
		BigInteger b = computeB(message, d, a, k, p);

		// send public key
		os.writeObject(y);
		os.writeObject(g);
		os.writeObject(p);

		// send message
		os.writeObject(message);
		
		// send signature
		os.writeObject(a);
		os.writeObject(b);
		
		s.close();
	}
}