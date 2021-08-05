

Instructions:

I ran all of my programs in terminal (MacOS) .

Message Digest:

javac messagedig.java
Java messagedig

Then just input the word you want hashed

Authentication:

Open two terminal shells

In the first terminal:

javac ProtectedServer.java
java ProtectedServer

In the second terminal:

javac ProtectedClient.java
java ProtectedClient

Signature:

I renamed the functions to EA and EB because I kept messing up the spelling

Open two terminal shells

In the first terminal:

javac ElGamalBob.java
java ElGamalBob

In the second terminal:

javac ElGamalAlice.java
java ElGamalAlice

Encryption:

Open two terminal shells

In the first terminal:

javac CipherServer.java
java CipherServer

In the second terminal:

javac CipherClient.java
java CipherClient

Public-Key System:

Open two terminal shells

In the first terminal:

javac Receiver.java
java Receiver

In the second terminal:

javac Sender.java
java Sender


X509:



Open two terminal shells

In the first terminal:

javac Serverx509.java
java Serverx509

In the second terminal:

javac Clientx509.java
java Clientx509





Discussion:
What are the limitations of using self-signed certificates? 

Self-signed certificates are not very trustworthy. There is no certificate authority (CA) that vets you or makes sure your identity/credentials are legit. Generally, the degree of confidence of an identity relies solely on the CA. In addition, man-in-the-middle attacks can happen more readily.

What are they useful for?

They are useful for providing a public key that begins a certificate chain. They are also useful in testing environments because they do not expire, or in internal usage where trustworthiness is not an issue because they are free and do not involve a 3rd party.
