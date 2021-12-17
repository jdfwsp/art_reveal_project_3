package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	generateSet()
}

func generateSet() {
	l1 := "abcd"
	for i := 0; i < 4; i++ {
		for j := 0; j < 4; j++ {
			for k := 0; k < 4; k++ {
				for l := 0; l < 4; l++ {
					file := fmt.Sprintf("%v%v%v%v", string(l1[i]), string(l1[j]), string(l1[k]), string(l1[l]))
					getSVGCode(file)
				}
			}
		}
	}
}

func getSVGCode(f string) {
	svgCode, _ := ioutil.ReadFile("layers/opening")
	s := string(svgCode)
	for i := 0; i < 4; i++ {
		layer := fmt.Sprintf("layers/%d/%v", i+1, string(f[i]))
		ll, _ := ioutil.ReadFile(layer)
		l := string(ll)
		s = s + l
	}
	s = s + "</svg>"
	outputFileName := fmt.Sprintf("output/%s.svg", f)
	os.WriteFile(outputFileName, []byte(s), 0444)
}
