package com.our.office;

import java.util.Scanner;

public class practice4 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in); //스캐너 먼저 설정
		
		while (true) {
			int a = sc.nextInt(), b = sc.nextInt();
			
			if( a!= 0 && b!= 0) { //a랑 b가 0이아니면 안끝난다  == 같다   != 아니다 
				System.out.println("a+b : "+ (a + b));
			}else {
				break;
			}
			//0 0 두개가 들어오면 while 문이 끝난다
		}
	}
}
