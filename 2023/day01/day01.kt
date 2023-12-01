import java.io.File


fun main(vararg args: String) {
    var lines = File(args[0]).useLines { it.toList() }
    var nums = arrayOf("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
		       "zero", "one", "two", "three", "four",
		       "five", "six", "seven", "eight", "nine")

    for (part in 1..2) {
	var answer = 0
	for (line in lines) {
	    var first = 0
	    var firstPos = line.length
	    var last = 0
	    var lastPos = -1
	    var pos: Int
	    
	    for (numInd in 0..nums.size-1) {
		var num = nums[numInd]
		if (part == 1 && num == "zero") {
		    break
		}
		// find the first
		pos = line.indexOf(num)
		if (pos >= 0 && pos < firstPos) {
		    first = numInd % 10
		    firstPos = pos
		}
		// find the last
		pos = line.lastIndexOf(num)
		if (pos >= 0 && pos > lastPos) {
		    last = numInd % 10
		    lastPos = pos
		}
	    }
	    answer += first * 10 + last
	}
	println("part$part = $answer")
    }
}
