package com.sample.org.utils;

import java.util.ArrayList;

public class MyThreads {

	private static ArrayList<CustomThread> list = null;
	
    public static ArrayList<CustomThread> getList() {
    	if(list==null){
            synchronized(MyThreads.class){
                if(list==null){
                  list =new ArrayList<CustomThread>();
                }
            }
        }
        return list;
	}
	
	private static MyThreads instance=null;
    public static MyThreads getInstance(){
        if(instance==null){
            synchronized(MyThreads.class){
                if(instance==null){
                    instance=new MyThreads();
                }
            }
        }
        return instance;
    }
    private MyThreads(){}
}
