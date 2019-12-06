
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Day02 {
	public static void main(String[] args) {
		String filename = "src/input.txt";
        Day02 worker = new Day02();
        ArrayList<Integer> data = worker.readFile(filename);
        int res = -2;
        //res = worker.solution1(data, 12, 2);
        res = worker.solution2(data);
		System.out.println(res);
	}
	ArrayList<Integer> readFile(String filename) {
        ArrayList<Integer> data = new ArrayList<>();
        try {
            BufferedReader bufferedReader = new BufferedReader(new FileReader(filename));
            String line = null;
            while ((line=bufferedReader.readLine()) != null) {
                String[] tmp = line.split(",");
                for (String val : tmp) {
                    data.add(Integer.parseInt(val));
                }
            }
            
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        // System.out.println(data.size());
        return data;
	}
	int solution1(ArrayList<Integer> data, int n, int v)  {
        if (data.size() < 4) return -1;
        data.set(1, n);
        data.set(2, v);
        for (int i = 0; i < data.size(); i += 4) {
            switch (data.get(i)) {
            case 1:
                data.set(data.get(i+3), data.get(data.get(i+1)) + data.get(data.get(i+2)));
                break;
            case 2:
                data.set(data.get(i+3), data.get(data.get(i+1)) * data.get(data.get(i+2)));
                break;
            case 99:
                return data.get(0);
            default:
                // 宕机也算停止
                return data.get(0);
            }
        }		
        return data.get(0);
    }
    int solution2(ArrayList<Integer> data) {
        for (int i = 0; i < 100; ++i) {
            for (int j = 0; j < 100; ++j) {
                ArrayList<Integer> data_ = new ArrayList<Integer>(data);
                solution1(data_, i, j);
                if (data_.get(0) == 19690720) {
                    return i * 100 + j;
                }
            }
        }
        return -1;
    }
	
}
