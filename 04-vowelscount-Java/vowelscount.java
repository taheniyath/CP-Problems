// # Write the function vowelCount(s), that takes a string s, 
// # and returns the number of vowels in s, ignoring case, 
// # so "A" and "a" are both vowels. The vowels are "a", "e", "i", "o", and "u". 
// # So, for example, ("Abc def!!! a? yzyzyz!") returns 3 (two a's and one e).


class vowelscount {
	public int fun_vowelscount(String s){
		// your code goes here
		int count = 0;
		for(int i=0  ; i<s.length(); i++){
			char x = s.charAt(i);
			if(x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u'){
				count++;
			}
		}
		return count;
	}
	
}