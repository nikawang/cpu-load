package com.sample.org.utils;
import java.util.Properties;

public class ReadFileUtils {
	
	private static Properties config = new Properties();
	static{
		try {
			config.load(ReadFileUtils.class.getClassLoader().getResourceAsStream("app.properties"));
		} catch (Exception e) {
			e.printStackTrace();
			throw new ExceptionInInitializerError(e);
		}
	}

	public static Properties getConfig(){
			return config;
	}
	
	
}	
