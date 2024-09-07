import (
	"container/heap"
	"strings"
)

type CharFreq struct {
	char  rune
	count int
}

type PriorityQueue []CharFreq

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {

	return pq[i].count > pq[j].count
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PriorityQueue) Push(x interface{}) {
	*pq = append(*pq, x.(CharFreq))
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	*pq = old[0 : n-1]
	return item
}

func frequencySort(s string) string {
	
	count := make(map[rune]int)
	for _, char := range s {
		count[char]++
	}

	
	pq := &PriorityQueue{}
	heap.Init(pq)

	
	for char, cnt := range count {
		heap.Push(pq, CharFreq{char, cnt})
	}

	
	var result strings.Builder
	for pq.Len() > 0 {
		item := heap.Pop(pq).(CharFreq)
		result.WriteString(strings.Repeat(string(item.char), item.count))
	}

	return result.String()
}
