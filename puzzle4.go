package main

import (
	"crypto/md5"
	"fmt"
	"io"
	"bytes"
)

var secret_key string = "iwrupvqb"

func checknum(num int) {
	h := md5.New()
	var snum = fmt.Sprintf("%d", num)
	io.WriteString(h, secret_key)
	io.WriteString(h, snum)
	var buffer []byte = h.Sum(nil)

	// used to find part2 of this problem
	var found3 = false

	// they at least must meet this condition
	if buffer[0] == 0  && buffer[1]==0 {

		// this is 6 zeros
		if buffer[2]==0 {
			found3 = true
		}

		// checking for 5 zeros a really
		// cheesey way
		var ts string = shex(h.Sum(nil),16)
		if ts[0:5] == "00000" {
			if (found3) {
				fmt.Println("*3",num, ts)
			} else {
				fmt.Println(num, ts)
			}
			
		}
	}


}

func shex(ibuffer []byte, num int) string {
	var buffer bytes.Buffer
	for i:=0;i<num;i++ {
		buffer.WriteString(fmt.Sprintf("%0.2x",ibuffer[i]))
	}
	return buffer.String()
}

func main() {
	fmt.Println("Starting...")
	var i int
	for i = 0; i < 10000000; i++ {
		checknum(i)
	}

}
