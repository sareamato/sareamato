/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author saraamato
 */
public class Homework1 {

    public static void main(String args[]) {
        // TODO code application logic here
         int number,i,j, count, step = 0; 
         long time, time2; 
         
		
	//upper limit	
	for(i = 10000; i <= 100000; i+= 10000)
        {  
            count = 0;
            step++;
            
           
            time = System.nanoTime();
            //lower limit to upper limit
            for(number = 2; number <= i; number++)
            {
                boolean isPrime = true;
                //testing each number
                for (j = 2; j < number ; j++)
                {
                  	if (number % j == 0)
		    	{
                            isPrime = false;
                            
		      }}
                
                        if (isPrime)
                        { 
                            count++;
                            
                        }}
                        
                
                
                        
                        
              
                       
                  
                    
		    	
		    
            time2 = System.nanoTime();
    
            
        
            System.out.println("Step" + step);
            System.out.println("There are: " + count + " prime numbers");
            System.out.println("Time in nanoseconds: " + (time2 - time));
		    	
        
            }}}
/// I adapted the following code for help with my Boolean logic 
/// Title: Into to Java Programming, 6E - PrimeNumber.java
/// Author: NYU 
/// Date: Fall 2006
/// Code Version:22
/// Availability: https://cs.nyu.edu/courses/fall06/V22.0101-003/html/PrimeNumber.html 
                 
		     
    

          