import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Day01 {
    public static void main(String[] args) {
        String filename = "src/input.txt";
        Day01 solution = new Day01();
        List data = solution.readFile(filename);
        solution.solution01(data);
        solution.solution2(data);
    }

    List readFile(String filename) {
        List<Integer> data = new ArrayList<Integer>();
        try {
            Scanner sc = new Scanner(new BufferedInputStream(new FileInputStream(new File(filename))));
            while (sc.hasNextInt()) {
               int tmp = sc.nextInt();
               data.add(tmp);
            }
        } catch(FileNotFoundException e) {
            e.printStackTrace();
        } 
        return data;
    }
    
    long solution01(List<?> data) {
    	@SuppressWarnings("unchecked")
		ArrayList<Integer> items = (ArrayList<Integer>)data;
    	long ret = 0;
    	for (Integer val : items) {
    		ret += (long)Math.floor(val / 3.0);
    	}
    	ret -= 2 * items.size();
    	System.out.println(ret);
    	return ret;
    }
    
    long solution2(List<?> data) {
    	@SuppressWarnings("unchecked")
		ArrayList<Integer> items = (ArrayList<Integer>)data;
    	long ret = 0;
    	for (Integer val : items) {
    		long a = 0;
    		while (val > 0) {
    			val = (int)Math.floor(val / 3.0) - 2;
    			if (val > 0) {
    				a += val; 
    			}
    		}
    		// System.out.println(a);
    		ret += a;
    	}
    	System.out.println(ret);
    	return ret;
    }
}