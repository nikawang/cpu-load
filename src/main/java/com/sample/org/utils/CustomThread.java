package com.sample.org.utils;

public class CustomThread extends Thread{

	private int ticket=Integer.parseInt(ReadFileUtils.getConfig().get("ticket").toString());
	public CustomThread(){
    }
    public void run(){
    	while(true){
	        while(ticket>0){
//	            System.out.println(ticket--+" is saled by "+Thread.currentThread().getName());
	        	ticket--;
	        }
	        try {
				Thread.sleep(Long.parseLong(ReadFileUtils.getConfig().get("sleep").toString()));
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			System.out.println("sleep over");
	        while(ticket<1000){
//	        	System.out.println(ticket+++" after sleep is saled by "+Thread.currentThread().getName());
	        	ticket++;
	        	if(ticket>1000){
	        		break;
	        	}
	        }
	        try {
				Thread.sleep(Long.parseLong(ReadFileUtils.getConfig().get("sleep").toString()));
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
	     }
    }
	
}
