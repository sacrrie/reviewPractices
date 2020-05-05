 //this is the first java program for testing
package com.java.l2.test;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
public class personTest {
	@Test
	public void returnTest(){
		person yan = new person();
		assertEquals("Hello World",yan.returnHello());
	}
	@Test
	public void shouldReturnMarcus(){
		person ps=new person();
	}


}
/* */